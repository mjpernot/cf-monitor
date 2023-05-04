# Classification (U)

"""Program:  service_cmd.py

    Description:  Unit testing of service_cmd in cf_monitor.py.

    Usage:
        test/unit/cf_monitor/service_cmd.py

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
import version

__version__ = version.__version__


class Popen(object):

    """Class:  Popen

    Description:  Class stub holder for subprocess.Popen class.

    Methods:
        __init__
        communicate

    """

    def __init__(self, cmd, stdout):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.cmd = cmd
        self.stdout = stdout
        self.msg = "Message"
        self.status = True

    def communicate(self):

        """Method:  communicate

        Description:  communicate method.

        Arguments:

        """

        return self.msg, self.status


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_service_cmd

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.service = "service"
        self.arg = "args"
        self.cmd = "to_line"
        self.popen = Popen(self.cmd, True)
        self.results = "Message"

    @mock.patch("cf_monitor.subprocess")
    def test_service_cmd(self, mock_sub):

        """Function:  test_service_cmd

        Description:  Test service_cmd function.

        Arguments:

        """

        mock_sub.Popen.return_value = self.popen
        mock_sub.PIPE.return_value = True

        self.assertEqual(cf_monitor.service_cmd(self.service, self.arg),
                         self.results)


if __name__ == "__main__":
    unittest.main()
