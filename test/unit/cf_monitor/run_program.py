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
import version

__version__ = version.__version__


class ArgParser(object):

    """Class:  ArgParser

    Description:  Class stub holder for gen_class.ArgParser class.

    Methods:
        __init__
        get_val

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.cmdline = None
        self.args_array = dict()

    def get_val(self, skey, def_val=None):

        """Method:  get_val

        Description:  Method stub holder for gen_class.ArgParser.get_val.

        Arguments:

        """

        return self.args_array.get(skey, def_val)


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

        self.host = "hostname"


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_programlock_false
        test_run_monitor

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.cfg = CfgTest()
        self.args = ArgParser()
        self.args.args_array = {"-c": "config_file", "-d": "config"}

    @mock.patch("cf_monitor.monitor", mock.Mock(return_value=True))
    @mock.patch("cf_monitor.gen_libs.load_module")
    def test_run_monitor(self, mock_cfg):

        """Function:  test_run_monitor

        Description:  Test with executing monitor function.

        Arguments:

        """

        mock_cfg.return_value = self.cfg

        self.assertFalse(cf_monitor.run_program(self.args))


if __name__ == "__main__":
    unittest.main()
