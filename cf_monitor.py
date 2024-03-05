#!/usr/bin/python
# Classification (U)

"""Program:  cf_monitor.py

    Description:  Monitor the status of a ColdFusion application.  This will
        include recycling the ColdFusion application if certain conditions are
        met.

    Usage:
        cf_monitor.py -c file -d path [-M] [-y flavor_id] [-v | -h]

    Arguments:
        -c file => Configuration file.  Required argument.
        -d dir_path => Directory path for option '-c'.  Required argument.

        -M => Monitor only.

        -y value => A flavor id for the program lock.  To create unique lock.
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
from __future__ import print_function
from __future__ import absolute_import

# Standard
import sys
import time
import getpass
import socket
import datetime
import subprocess
import psutil
import requests

# Local
try:
    from .lib import gen_libs
    from .lib import gen_class
    from . import version

except (ValueError, ImportError) as err:
    import lib.gen_libs as gen_libs
    import lib.gen_class as gen_class
    import version

__version__ = version.__version__


def help_message():

    """Function:  help_message

    Description:  Displays the program's docstring which is the help and usage
        message when -h option is selected.

    Arguments:

    """

    print(__doc__)


def get_code(url, read_timeout=None, connect_timeout=None):

    """Function:  get_code

    Description:  Open a connection to a web server and return the status code.

    Arguments:
        (input) url -> Web url address
        (input) read_timeout -> Number of seconds for a read timeout
        (input) connect_timeout -> Number of seconds for a connect timeout
        (output) status -> Status of the web server

    """

    try:
        conn = requests.get(url, timeout=(connect_timeout, read_timeout))
        status = conn.status_code

    except requests.exceptions.ConnectTimeout:
        status = "Connect Timeout"

    except requests.exceptions.ReadTimeout:
        status = "Read Timeout"

    return status


def email_admin(args, cfg, code):

    """Function:  email_admin

    Description:  Email status code to administrators.

    Arguments:
        (input) args -> ArgParser class instance
        (input) cfg -> Configuration settings module
        (input) code -> Status code

    """

    host = socket.gethostname()
    frm_line = getpass.getuser() + "@" + host
    subj = host + "-> Coldfusion Status Code: " + str(code)
    dtg = datetime.datetime.strftime(
        datetime.datetime.now(), "%Y-%m-%d %H:%M:%S")
    line = " Detected %s status code during a status check.\n" % str(code)
    line2 = "Rebooting service..."

    email = gen_class.Mail(cfg.to_line, subj, frm_line)
    email.add_2_msg(dtg)
    email.add_2_msg(line)

    if args.arg_exist("-M"):
        email.add_2_msg(line2)

    email.send_mail()


def service_cmd(service, arg):

    """Function:  service_cmd

    Description:  Run the system service program with designated command.

    Arguments:
        (input) service -> Name of service
        (input) arg -> Argument to run with service command
        (output) msg -> Status return message from service command

    """

    cmd = "/sbin/service"

    proc1 = subprocess.Popen([cmd, service, arg], stdout=subprocess.PIPE)
    msg, _ = proc1.communicate()

    return msg


def kill_process(pid_list):

    """Function:  kill_process

    Description:  Run the system kill command against a process pid.

    Arguments:
        (input) pid_list -> List of pids to kill

    """

    pid_list = list(pid_list)
    kill = "/usr/bin/kill"
    arg = "-9"

    for pid in pid_list:
        subprocess.call([kill, arg, str(pid)])


def find_process(cfg):

    """Function:  find_process

    Description:  Finds all processes that match the requirements and returns
        a list of pids.

    Arguments:
        (input) cfg -> Configuration settings module
        (output) pid_list -> List of pids to kill

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


def monitor(args, cfg):

    """Function:  monitor

    Description:  Monitors the status of the ColdFusion app and takes
        appropriate actions when certain conditions are meet.

    Arguments:
        (input) args -> ArgParser class instance
        (input) cfg -> Configuration settings module

    """

    code = get_code(cfg.url, cfg.read_timeout, cfg.connect_timeout)

    if code in cfg.code_list or "Timeout" in str(code):
        email_admin(args, cfg, code)

        if not args.arg_exist("-M"):
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


def run_program(args):

    """Function:  run_program

    Description:  Creates class instance and controls flow of the program.

    Arguments:
        (input) args -> ArgParser class instance

    """

    cfg = gen_libs.load_module(args.get_val("-c"), args.get_val("-d"))
    monitor(args, cfg)


def main():

    """Function:  main

    Description:  Initializes program-wide used variables and processes command
        line arguments and values.

    Variables:
        dir_perms_chk -> contains options which will be directories and the
            octal permission settings
        opt_req_list -> contains options that are required for the program.
        opt_val_list -> contains options which require values.

    Arguments:
        (input) argv -> Arguments from the command line.

    """

    dir_perms_chk = {"-d": 5}
    opt_req_list = ["-c", "-d"]
    opt_val_list = ["-c", "-d", "-y"]

    # Process argument list from command line.
    args = gen_class.ArgParser(
        sys.argv, opt_val=opt_val_list, do_parse=True)

    if not gen_libs.help_func(args.get_args(), __version__, help_message)   \
       and args.arg_require(opt_req=opt_req_list)                           \
       and args.arg_dir_chk(dir_perms_chk=dir_perms_chk):

        try:
            proglock = gen_class.ProgramLock(
                sys.argv, args.get_val("-y", def_val=""))
            run_program(args)
            del proglock

        except gen_class.SingleInstanceException:
            print("WARNING:  lock in place for cf_monitor with id of: %s"
                  % (args.get_val("-y", def_val="")))


if __name__ == "__main__":
    sys.exit(main())
