# Classification (U)

"""Program:  main.py

    Description:  Unit testing of main in cf_monitor.py.

    Usage:
        test/unit/cf_monitor/main.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest
import mock

# Local
sys.path.append(os.getcwd())
import cf_monitor
import lib.gen_libs as gen_libs
import version

__version__ = version.__version__


class ArgParser(object):

    """Class:  ArgParser

    Description:  Class stub holder for gen_class.ArgParser class.

    Methods:
        __init__
        arg_dir_chk
        arg_require
        get_args
        get_val
        arg_parse2

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.cmdline = None
        self.args_array = dict()
        self.opt_req = None
        self.opt_req2 = True
        self.dir_perms_chk = None
        self.dir_perms_chk2 = True
        self.argparse2 = True

    def arg_dir_chk(self, dir_perms_chk):

        """Method:  arg_dir_chk

        Description:  Method stub holder for gen_class.ArgParser.arg_dir_chk.

        Arguments:

        """

        self.dir_perms_chk = dir_perms_chk

        return self.dir_perms_chk2

    def arg_require(self, opt_req):

        """Method:  arg_require

        Description:  Method stub holder for gen_class.ArgParser.arg_require.

        Arguments:

        """

        self.opt_req = opt_req

        return self.opt_req2

    def get_args(self):

        """Method:  get_args

        Description:  Method stub holder for gen_class.ArgParser.get_args.

        Arguments:

        """

        return self.args_array

    def get_val(self, skey, def_val):

        """Method:  get_val

        Description:  Method stub holder for gen_class.ArgParser.get_val.

        Arguments:

        """

        return self.args_array.get(skey, def_val)

    def arg_parse2(self):

        """Method:  arg_parse2

        Description:  Method stub holder for gen_class.ArgParser.arg_parse2.

        Arguments:

        """

        return self.argparse2


class ProgramLock(object):

    """Class:  ProgramLock

    Description:  Class stub holder for gen_class.ProgramLock class.

    Methods:
        __init__

    """

    def __init__(self, cmdline, flavor):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.cmdline = cmdline
        self.flavor = flavor


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_arg_parse2_false
        test_arg_parse2_true
        test_help_true
        test_help_false
        test_arg_req_false
        test_arg_req_true
        test_arg_dir_false
        test_arg_dir_true
        test_run_program
        test_programlock_true
        test_programlock_false
        test_programlock_id

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.args = ArgParser()
        self.args2 = ArgParser()
        self.args.args_array = {"-c": "config_file", "-d": "config_dir"}
        self.args2.args_array = {
            "-c": "config_file", "-d": "config_dir", "-y": "Flavor"}
        self.proglock = ProgramLock(["cmdline"], "FlavorID")

    @mock.patch("cf_monitor.gen_class.ArgParser")
    def test_arg_parse2_false(self, mock_arg):

        """Function:  test_arg_parse2_false

        Description:  Test arg_parse2 returns false.

        Arguments:

        """

        self.args.argparse2 = False

        mock_arg.return_value = self.args

        self.assertFalse(cf_monitor.main())

    @mock.patch("cf_monitor.gen_libs.help_func")
    @mock.patch("cf_monitor.gen_class.ArgParser")
    def test_arg_parse2_true(self, mock_arg, mock_help):

        """Function:  test_arg_parse2_true

        Description:  Test arg_parse2 returns true.

        Arguments:

        """

        mock_arg.return_value = self.args
        mock_help.return_value = True

        self.assertFalse(cf_monitor.main())

    @mock.patch("cf_monitor.gen_libs.help_func")
    @mock.patch("cf_monitor.gen_class.ArgParser")
    def test_help_true(self, mock_arg, mock_help):

        """Function:  test_status_true

        Description:  Test main function with Help_Func returns True.

        Arguments:

        """

        mock_arg.return_value = self.args
        mock_help.return_value = True

        self.assertFalse(cf_monitor.main())

    @mock.patch("cf_monitor.gen_libs.help_func")
    @mock.patch("cf_monitor.gen_class.ArgParser")
    def test_help_false(self, mock_arg, mock_help):

        """Function:  test_status_false

        Description:  Test main function with Help_Func returns False.

        Arguments:

        """

        self.args.opt_req2 = False

        mock_arg.return_value = self.args
        mock_help.return_value = False

        self.assertFalse(cf_monitor.main())

    @mock.patch("cf_monitor.gen_libs.help_func")
    @mock.patch("cf_monitor.gen_class.ArgParser")
    def test_arg_req_false(self, mock_arg, mock_help):

        """Function:  test_arg_req_false

        Description:  Test arg_require if returns false.

        Arguments:

        """

        self.args.opt_req2 = False

        mock_arg.return_value = self.args
        mock_help.return_value = False

        self.assertFalse(cf_monitor.main())

    @mock.patch("cf_monitor.gen_libs.help_func")
    @mock.patch("cf_monitor.gen_class.ArgParser")
    def test_arg_req_true(self, mock_arg, mock_help):

        """Function:  test_arg_req_true

        Description:  Test arg_require if returns true.

        Arguments:

        """

        self.args.dir_perms_chk2 = False

        mock_arg.return_value = self.args
        mock_help.return_value = False

        self.assertFalse(cf_monitor.main())

    @mock.patch("cf_monitor.gen_libs.help_func")
    @mock.patch("cf_monitor.gen_class.ArgParser")
    def test_arg_dir_false(self, mock_arg, mock_help):

        """Function:  test_arg_dir_false

        Description:  Test arg_dir_chk if returns false.

        Arguments:

        """

        self.args.dir_perms_chk2 = False

        mock_arg.return_value = self.args
        mock_help.return_value = False

        self.assertFalse(cf_monitor.main())

    @mock.patch("cf_monitor.run_program", mock.Mock(return_value=True))
    @mock.patch("cf_monitor.gen_class.ProgramLock")
    @mock.patch("cf_monitor.gen_libs.help_func")
    @mock.patch("cf_monitor.gen_class.ArgParser")
    def test_arg_dir_true(self, mock_arg, mock_help, mock_lock):

        """Function:  test_arg_dir_true

        Description:  Test arg_dir_chk if returns true.

        Arguments:

        """

        mock_arg.return_value = self.args
        mock_help.return_value = False
        mock_lock.return_value = self.proglock

        self.assertFalse(cf_monitor.main())

    @mock.patch("cf_monitor.run_program", mock.Mock(return_value=True))
    @mock.patch("cf_monitor.gen_class.ProgramLock")
    @mock.patch("cf_monitor.gen_libs.help_func")
    @mock.patch("cf_monitor.gen_class.ArgParser")
    def test_run_program(self, mock_arg, mock_help, mock_lock):

        """Function:  test_run_program

        Description:  Test run_program function.

        Arguments:

        """

        mock_arg.return_value = self.args
        mock_help.return_value = False
        mock_lock.return_value = self.proglock

        self.assertFalse(cf_monitor.main())

    @mock.patch("cf_monitor.run_program", mock.Mock(return_value=True))
    @mock.patch("cf_monitor.gen_class.ProgramLock")
    @mock.patch("cf_monitor.gen_libs.help_func")
    @mock.patch("cf_monitor.gen_class.ArgParser")
    def test_programlock_true(self, mock_arg, mock_help, mock_lock):

        """Function:  test_programlock_true

        Description:  Test with ProgramLock returns True.

        Arguments:

        """

        mock_arg.return_value = self.args
        mock_help.return_value = False
        mock_lock.return_value = self.proglock

        self.assertFalse(cf_monitor.main())

    @mock.patch("cf_monitor.run_program", mock.Mock(return_value=True))
    @mock.patch("cf_monitor.gen_class.ProgramLock")
    @mock.patch("cf_monitor.gen_libs.help_func")
    @mock.patch("cf_monitor.gen_class.ArgParser")
    def test_programlock_false(self, mock_arg, mock_help, mock_lock):

        """Function:  test_programlock_false

        Description:  Test with ProgramLock returns False.

        Arguments:

        """

        mock_arg.return_value = self.args
        mock_help.return_value = False
        mock_lock.side_effect = \
            cf_monitor.gen_class.SingleInstanceException

        with gen_libs.no_std_out():
            self.assertFalse(cf_monitor.main())

    @mock.patch("cf_monitor.run_program", mock.Mock(return_value=True))
    @mock.patch("cf_monitor.gen_class.ProgramLock")
    @mock.patch("cf_monitor.gen_libs.help_func")
    @mock.patch("cf_monitor.gen_class.ArgParser")
    def test_programlock_id(self, mock_arg, mock_help, mock_lock):

        """Function:  test_programlock_id

        Description:  Test ProgramLock with flavor ID.

        Arguments:

        """

        mock_arg.return_value = self.args2
        mock_help.return_value = False
        mock_lock.return_value = self.proglock

        self.assertFalse(cf_monitor.main())


if __name__ == "__main__":
    unittest.main()
