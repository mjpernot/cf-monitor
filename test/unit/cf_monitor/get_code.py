# Classification (U)

"""Program:  get_code.py

    Description:  Unit testing of get_code in cf_monitor.py.

    Usage:
        test/unit/cf_monitor/get_code.py

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


class Requests(object):

    """Class:  Server

    Description:  Class stub holder for Requests class.

    Methods:
        __init__

    """

    def __init__(self, url, timeout):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.url = url
        self.timeout = timeout
        self.status_code = True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_successful_connection

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.url = "URL_String"
        self.requests = Requests(self.url, timeout=(None, None))

    @mock.patch("cf_monitor.requests.get")
    def test_successful_connection(self, mock_get):

        """Function:  test_successful_connection

        Description:  Test with no arguments.

        Arguments:

        """

        mock_get.return_value = self.requests

        self.assertTrue(cf_monitor.get_code(self.url))


if __name__ == "__main__":
    unittest.main()
