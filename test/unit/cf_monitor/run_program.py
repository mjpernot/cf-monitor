#!/usr/bin/python
# Classification (U)

"""Program:  run_program.py

    Description:  Unit testing of run_program in cf_monitor.py.

    Usage:
        test/unit/cf_monitor/run_program.py

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
import lib.gen_libs as gen_libs
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_programlock_false -> Test with ProgramLock returns False.
        test_run_monitor -> Test with executing monitor function.

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
                __init__ -> Initialize configuration environment.

            """

            def __init__(self):

                """Method:  __init__

                Description:  Initialization instance of the CfgTest class.

                Arguments:

                """

                self.host = "hostname"

        self.cfg = CfgTest()
        self.args_array = {"-c": "config_file", "-d": "config"}

    @mock.patch("cf_monitor.monitor", mock.Mock(return_value=True))
    @mock.patch("cf_monitor.gen_libs.load_module")
    def test_run_monitor(self, mock_cfg):

        """Function:  test_run_monitor

        Description:  Test with executing monitor function.

        Arguments:

        """

        mock_cfg.return_value = self.cfg

        self.assertFalse(cf_monitor.run_program(self.args_array))


if __name__ == "__main__":
    unittest.main()
