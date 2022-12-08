# Classification (U)

"""Program:  kill_process.py

    Description:  Unit testing of kill_process in cf_monitor.py.

    Usage:
        test/unit/cf_monitor/kill_process.py

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


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_multiple_list
        test_one_in_list
        test_empty_list

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.pid_list = [1]
        self.pid_list2 = [1, 2]

    @mock.patch("cf_monitor.subprocess.call", mock.Mock(return_value=True))
    def test_multiple_list(self):

        """Function:  test_multiple_list

        Description:  Test with multiple items in list.

        Arguments:

        """

        self.assertFalse(cf_monitor.kill_process(self.pid_list2))

    @mock.patch("cf_monitor.subprocess.call", mock.Mock(return_value=True))
    def test_one_in_list(self):

        """Function:  test_one_in_list

        Description:  Test with one item in list.

        Arguments:

        """

        self.assertFalse(cf_monitor.kill_process(self.pid_list))

    @mock.patch("cf_monitor.subprocess.call", mock.Mock(return_value=True))
    def test_empty_list(self):

        """Function:  test_kill_process

        Description:  Test with empty list.

        Arguments:

        """

        self.assertFalse(cf_monitor.kill_process([]))


if __name__ == "__main__":
    unittest.main()
