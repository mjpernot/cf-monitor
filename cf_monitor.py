#!/usr/bin/python
# Classification (U)

"""Program:  cf_monitor.py

    Description:  Monitor the status of a ColdFusion application.  This will
        include recycling the ColdFusion application if certain conditions are
        met.

    Usage:
        cf_monitor.py -c file -d path [-M] [-v | -h]

    Arguments:
        -M => Monitor only.
        -v => Display version of this program.
        -h => Help and usage message.

        NOTE 1:  -v and -h ovrrides all other options.

    Notes:
        Monitoring configuration file format (monitor.py).  The configuration
        file format:

            host = "HOSTNAME"
            # List of codes to check for
            code_list = [502, 503, CODE1]
            # URL Address to check
            url = "http://ADDRESS/"
            # Email address to administrator
            to_line = "EMAIL_ADDRESS@DOMAIN_NAME"
            # ColdFusion installation directory
            cf_dir = "INSTALL_DIR"
            # ColdFusion service name
            service = "SERVICE_NAME"

    Example:
        cf_monitor.py -c monitor -d config -M

"""

# Libraries and Global Variables

# Standard
import sys
import time
import getpass
import socket
import datetime
import psutil
import subprocess

# Third-party
import requests

# Local
import lib.arg_parser as arg_parser
import lib.gen_libs as gen_libs
import lib.gen_class as gen_class
import version

# Version
__version__ = version.__version__


def help_message(**kwargs):

    """Function:  help_message

    Description:  Displays the program's docstring which is the help and usage
        message when -h option is selected.

    Arguments:
        (input) **kwargs:
            None

    """

    print(__doc__)


def get_code(url, read_timeout=None, connect_timeout=None, **kwargs):

    """Function:  get_code

    Description:  Open a connection to a web server and return the status code.

    Arguments:
        (input) url -> Web url address.
        (input) read_timeout -> Number of seconds for a read timeout.
        (input) connect_timeout -> Number of seconds for a connect timeout.
        (input) **kwargs:
            None
        (output) status -> Status of the web server.

    """

    try:
        conn = requests.get(url, timeout=(connect_timeout, read_timeout))
        status = conn.status_code

    except requests.exceptions.ConnectTimeout:
        status = "Connect Timeout"

    except requests.exceptions.ReadTimeout:
        status = "Read Timeout"

    return status


def email_admin(args_array, cfg, code, **kwargs):

    """Function:  email_admin

    Description:  Email status code to administrators.

    Arguments:
        (input) args_array -> Dict of command line options and values.
        (input) cfg -> Configuration settings module.
        (input) code -> Status code.
        (input) **kwargs:
            None

    """

    host = socket.gethostname()
    frm_line = getpass.getuser() + "@" + host
    subj = host + "-> Coldfusion Status Code: " + str(code)
    dtg = datetime.datetime.strftime(datetime.datetime.now(),
                                     "%Y-%m-%d %H:%M:%S")
    line = " Detected %s status code during a status check.\n" % str(code)
    line2 = "Rebooting service..."

    email = gen_class.Mail(cfg.to_line, subj, frm_line)
    email.add_2_msg(dtg)
    email.add_2_msg(line)

    if "-M" not in args_array:
        email.add_2_msg(line2)

    email.send_mail()


def service_cmd(service, arg, **kwargs):

    """Function:  service_cmd

    Description:  Run the system service program with designated command.

    Arguments:
        (input) service -> Name of service.
        (input) arg -> Argument to run with service command.
        (input) **kwargs:
            None
        (output) msg -> Status return message from service command.

    """

    cmd = "/sbin/service"

    P1 = subprocess.Popen([cmd, service, arg], stdout=subprocess.PIPE)
    msg, status = P1.communicate()

    return msg


def kill_process(pid_list, **kwargs):

    """Function:  kill_process

    Description:  Run the system kill command against a process pid.

    Arguments:
        (input) pid_list -> List of pids to kill.
        (input) **kwargs:
            None

    """

    kill = "/usr/bin/kill"
    arg = "-9"

    for pid in pid_list:
        subprocess.call([kill, arg, str(pid)])


def find_process(cfg, **kwargs):

    """Function:  find_process

    Description:  Finds all processes that match the requirements and returns
        a list of pids.

    Arguments:
        (input) cfg -> Configuration settings module.
        (input) **kwargs:
            None
        (output) pid_list -> List of pids to kill.

    """

    pid_list = []

    for proc_dict in psutil.process_iter():
        proc = proc_dict.as_dict(attrs=['pid', 'cmdline'])

        # Add pid only for process that meets the search criteria.
        # This is based on the ColdFusion init.d program check.
        if [s for s in proc['cmdline'] if cfg.java_proc in s] \
           and [s for s in proc['cmdline'] if cfg.bs_proc in s] \
           and [s for s in proc['cmdline'] if cfg.start_arg in s] \
           and [s for s in proc['cmdline'] if cfg.cf_dir in s]:

            pid_list.append(proc['pid'])

    return pid_list


def monitor(args_array, cfg, **kwargs):

    """Function:  monitor

    Description:  Monitors the status of the ColdFusion app and takes
        appropriate actions when certain conditions are meet.

    Arguments:
        (input) args_array -> Dict of command line options and values.
        (input) cfg -> Configuration settings module.
        (input) **kwargs:
            None

    """

    code = get_code(cfg.url, cfg.read_timeout, cfg.connect_timeout)

    if code in cfg.code_list or "Timeout" in str(code):
        email_admin(args_array, cfg, code)

        if "-M" not in args_array:
            service_cmd(cfg.service, "stop")
            time.sleep(30)

            # Shutdown service via service or kill.
            while True:
                if service_cmd(cfg.service, "status").strip("\n") == \
                   cfg.down_msg:
                    break

                else:
                    pid_list = find_process(cfg)
                    kill_process(pid_list)

            service_cmd(cfg.service, "start")
            time.sleep(cfg.start_sleep)


def run_program(args_array, **kwargs):

    """Function:  run_program

    Description:  Creates class instance and controls flow of the program.
        Create a program lock to prevent other instantiations from running.

    Arguments:
        (input) args_array -> Dict of command line options and values.
        (input) **kwargs:
            None

    """

    cfg = gen_libs.load_module(args_array["-c"], args_array["-d"])

    try:
        PROG_LOCK = gen_class.ProgramLock(sys.argv, cfg.host)

        monitor(args_array, cfg)

        del PROG_LOCK

    except gen_class.SingleInstanceException:
        print("WARNING:  cf_monitor lock in place for: %s" % (cfg.host))


def main():

    """Function:  main

    Description:  Initializes program-wide used variables and processes command
        line arguments and values.

    Variables:
        dir_chk_list -> contains options which will be directories.
        opt_req_list -> contains options that are required for the program.
        opt_val_list -> contains options which require values.

    Arguments:
        (input) argv -> Arguments from the command line.

    """

    dir_chk_list = ["-d"]
    opt_req_list = ["-c", "-d"]
    opt_val_list = ["-c", "-d"]

    # Process argument list from command line.
    args_array = arg_parser.arg_parse2(sys.argv, opt_val_list)

    if not gen_libs.help_func(args_array, __version__, help_message):
        if not arg_parser.arg_require(args_array, opt_req_list) \
           and not arg_parser.arg_dir_chk_crt(args_array, dir_chk_list):
            run_program(args_array)


if __name__ == "__main__":
    sys.exit(main())
