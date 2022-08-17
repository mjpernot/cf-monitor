#!/usr/bin/python
# Classification (U)

"""Program:  monitor.py

    Description:  Unit testing of monitor in cf_monitor.py.

    Usage:
        test/unit/cf_monitor/monitor.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

# Third-party
import mock

# Local
sys.path.append(os.getcwd())
import cf_monitor
import version

__version__ = version.__version__


class ArgParser(object):

    """Class:  ArgParser

    Description:  Class stub holder for gen_class.ArgParser class.

    Methods:
        __init__
        arg_exist

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.cmdline = None
        self.args_array = dict()

    def arg_exist(self, arg):

        """Method:  arg_exist

        Description:  Method stub holder for gen_class.ArgParser.arg_exist.

        Arguments:

        """

        return True if arg in self.args_array else False


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_kill_process
        test_code_detected
        test_monitor_timeout_detected
        test_monitor_code_detected
        test_no_code_detected

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        class CfgTest(object):

            """Class:  CfgTest

            Description:  Class which is a representation of a cfg module.

            Methods:
                __init__

            """

            def __init__(self):

                """Method:  __init__

                Description:  Initialization instance of the CfgTest class.

                Arguments:

                """

                self.url = "url"
                self.read_timeout = 100
                self.connect_timeout = 150
                self.code_list = [502, 503]
                self.service = "service"
                self.down_msg = "down_msg"
                self.start_sleep = 1

        self.cfg = CfgTest()
        self.args = ArgParser()
        self.args2 = ArgParser()
        self.args2.args_array = {"-M": True}

    @mock.patch("cf_monitor.kill_process", mock.Mock(return_value=True))
    @mock.patch("cf_monitor.find_process", mock.Mock(return_value=[111]))
    @mock.patch("cf_monitor.time.sleep", mock.Mock(return_value=True))
    @mock.patch("cf_monitor.email_admin", mock.Mock(return_value=True))
    @mock.patch("cf_monitor.get_code", mock.Mock(return_value=502))
    @mock.patch("cf_monitor.service_cmd")
    def test_kill_process(self, mock_cmd):

        """Function:  test_kill_process

        Description:  Test with code detected with kill process.

        Arguments:

        """

        mock_cmd.side_effect = [True, "up_msg", "down_msg", True]

        self.assertFalse(cf_monitor.monitor(self.args, self.cfg))

    @mock.patch("cf_monitor.time.sleep", mock.Mock(return_value=True))
    @mock.patch("cf_monitor.email_admin", mock.Mock(return_value=True))
    @mock.patch("cf_monitor.get_code", mock.Mock(return_value=502))
    @mock.patch("cf_monitor.service_cmd")
    def test_code_detected(self, mock_cmd):

        """Function:  test_code_detected

        Description:  Test with code detected with reboot.

        Arguments:

        """

        mock_cmd.side_effect = [True, "down_msg", True]

        self.assertFalse(cf_monitor.monitor(self.args, self.cfg))

    @mock.patch("cf_monitor.email_admin", mock.Mock(return_value=True))
    @mock.patch("cf_monitor.get_code", mock.Mock(return_value="A Timeout."))
    def test_monitor_timeout_detected(self):

        """Function:  test_monitor_timeout_detected

        Description:  Test with timeout while monitoring.

        Arguments:

        """

        self.assertFalse(cf_monitor.monitor(self.args2, self.cfg))

    @mock.patch("cf_monitor.email_admin", mock.Mock(return_value=True))
    @mock.patch("cf_monitor.get_code", mock.Mock(return_value=502))
    def test_monitor_code_detected(self):

        """Function:  test_monitor_code_detected

        Description:  Test with code detected while monitoring.

        Arguments:

        """

        self.assertFalse(cf_monitor.monitor(self.args2, self.cfg))

    @mock.patch("cf_monitor.get_code", mock.Mock(return_value=404))
    def test_no_code_detected(self):

        """Function:  test_no_code_detected

        Description:  Test with no code detected.

        Arguments:

        """

        self.assertFalse(cf_monitor.monitor(self.args, self.cfg))


if __name__ == "__main__":
    unittest.main()
