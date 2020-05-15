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
import contextlib
import io

# Third-party
import mock

# Local
sys.path.append(os.getcwd())
import cf_monitor
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_help_true -> Test help if returns true.
        test_help_false -> Test help if returns false.
        test_arg_dir_true -> Test arg_dir_chk_crt if returns true.
        test_arg_dir_false -> Test arg_dir_chk_crt if returns false.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.args = {"-c": "config_file", "-d": "config_dir"}

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

    @mock.patch("cf_monitor.run_program")
    @mock.patch("cf_monitor.gen_libs.help_func")
    @mock.patch("cf_monitor.arg_parser")
    def test_require_false_chk_false(self, mock_arg, mock_help, mock_run):

        """Function:  test_require_false_chk_false

        Description:  Test main function with arg_require returns False and
            arg_dir_chk_crt returns False.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_dir_chk_crt.return_value = False
        mock_run.return_value = True

        self.assertFalse(cf_monitor.main())


if __name__ == "__main__":
    unittest.main()
