#!/usr/bin/python
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

# Third-party
import mock

# Local
sys.path.append(os.getcwd())
import cf_monitor
import lib.gen_libs as gen_libs
import version

__version__ = version.__version__


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
        test_help_true
        test_help_false
        test_arg_dir_true
        test_arg_dir_false
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

        self.args = {"-c": "config_file", "-d": "config_dir"}
        self.args2 = {"-c": "config_file", "-d": "config_dir", "-y": "Flavor"}
        self.proglock = ProgramLock(["cmdline"], "FlavorID")

    @mock.patch("cf_monitor.gen_libs.help_func")
    @mock.patch("cf_monitor.arg_parser.arg_parse2")
    def test_help_true(self, mock_arg, mock_help):

        """Function:  test_status_true

        Description:  Test main function with Help_Func returns True.

        Arguments:

        """

        mock_arg.return_value = self.args
        mock_help.return_value = True

        self.assertFalse(cf_monitor.main())

    @mock.patch("cf_monitor.gen_libs.help_func")
    @mock.patch("cf_monitor.arg_parser")
    def test_help_false(self, mock_arg, mock_help):

        """Function:  test_status_false

        Description:  Test main function with Help_Func returns False.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args
        mock_help.return_value = False
        mock_arg.arg_require.return_value = True

        self.assertFalse(cf_monitor.main())

    @mock.patch("cf_monitor.gen_libs.help_func")
    @mock.patch("cf_monitor.arg_parser")
    def test_require_true_chk_true(self, mock_arg, mock_help):

        """Function:  test_require_true_chk_true

        Description:  Test main function with arg_require returns True and
            arg_dir_chk_crt returns True.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args
        mock_help.return_value = False
        mock_arg.arg_require.return_value = True
        mock_arg.arg_dir_chk_crt.return_value = True

        self.assertFalse(cf_monitor.main())

    @mock.patch("cf_monitor.gen_libs.help_func")
    @mock.patch("cf_monitor.arg_parser")
    def test_require_false_chk_true(self, mock_arg, mock_help):

        """Function:  test_require_false_chk_true

        Description:  Test main function with arg_require returns False and
            arg_dir_chk_crt returns True.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_dir_chk_crt.return_value = True

        self.assertFalse(cf_monitor.main())

    @mock.patch("cf_monitor.gen_libs.help_func")
    @mock.patch("cf_monitor.arg_parser")
    def test_require_true_chk_false(self, mock_arg, mock_help):

        """Function:  test_require_true_chk_false

        Description:  Test main function with arg_require returns True and
            arg_dir_chk_crt returns False.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args
        mock_help.return_value = False
        mock_arg.arg_require.return_value = True
        mock_arg.arg_dir_chk_crt.return_value = False

        self.assertFalse(cf_monitor.main())

    @mock.patch("cf_monitor.run_program", mock.Mock(return_value=True))
    @mock.patch("cf_monitor.gen_class.ProgramLock")
    @mock.patch("cf_monitor.gen_libs.help_func")
    @mock.patch("cf_monitor.arg_parser")
    def test_require_false_chk_false(self, mock_arg, mock_help, mock_lock):

        """Function:  test_require_false_chk_false

        Description:  Test main function with arg_require returns False and
            arg_dir_chk_crt returns False.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_dir_chk_crt.return_value = False
        mock_lock.return_value = self.proglock

        self.assertFalse(cf_monitor.main())

    @mock.patch("cf_monitor.run_program", mock.Mock(return_value=True))
    @mock.patch("cf_monitor.gen_class.ProgramLock")
    @mock.patch("cf_monitor.gen_libs.help_func")
    @mock.patch("cf_monitor.arg_parser")
    def test_run_program(self, mock_arg, mock_help, mock_lock):

        """Function:  test_run_program

        Description:  Test run_program function.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_dir_chk_crt.return_value = False
        mock_lock.return_value = self.proglock

        self.assertFalse(cf_monitor.main())

    @mock.patch("cf_monitor.run_program", mock.Mock(return_value=True))
    @mock.patch("cf_monitor.gen_class.ProgramLock")
    @mock.patch("cf_monitor.gen_libs.help_func")
    @mock.patch("cf_monitor.arg_parser")
    def test_programlock_true(self, mock_arg, mock_help, mock_lock):

        """Function:  test_programlock_true

        Description:  Test with ProgramLock returns True.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_dir_chk_crt.return_value = False
        mock_lock.return_value = self.proglock

        self.assertFalse(cf_monitor.main())

    @mock.patch("cf_monitor.run_program", mock.Mock(return_value=True))
    @mock.patch("cf_monitor.gen_class.ProgramLock")
    @mock.patch("cf_monitor.gen_libs.help_func")
    @mock.patch("cf_monitor.arg_parser")
    def test_programlock_false(self, mock_arg, mock_help, mock_lock):

        """Function:  test_programlock_false

        Description:  Test with ProgramLock returns False.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_dir_chk_crt.return_value = False
        mock_lock.side_effect = \
            cf_monitor.gen_class.SingleInstanceException

        with gen_libs.no_std_out():
            self.assertFalse(cf_monitor.main())

    @mock.patch("cf_monitor.run_program", mock.Mock(return_value=True))
    @mock.patch("cf_monitor.gen_class.ProgramLock")
    @mock.patch("cf_monitor.gen_libs.help_func")
    @mock.patch("cf_monitor.arg_parser")
    def test_programlock_id(self, mock_arg, mock_help, mock_lock):

        """Function:  test_programlock_id

        Description:  Test ProgramLock with flavor ID.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args2
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_dir_chk_crt.return_value = False
        mock_lock.return_value = self.proglock

        self.assertFalse(cf_monitor.main())


if __name__ == "__main__":
    unittest.main()
