# Classification (U)

"""Program:  find_process.py

    Description:  Unit testing of find_process in cf_monitor.py.

    Usage:
        test/unit/cf_monitor/find_process.py

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


class ProcessIter3(object):

    """Class:  ProcessIter

    Description:  Class stub holder for psutil.process_iter class.

    Methods:
        __init__
        as_dict

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.attrs = None
        self.proc = {"cmdline": ["cmd", "java_proc", "bs_proc", "start_arg",
                                 "cf_dir"],
                     "pid": 12345}

    def as_dict(self, attrs):

        """Method:  as_dict

        Description:  as_dict method.

        Arguments:

        """

        self.attrs = attrs

        return self.proc


class Psutil3(object):

    """Class:  Psutil

    Description:  Class stub holder for psutil class.

    Methods:
        __init__
        process_iter

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.process_iter_list = [ProcessIter3(), ProcessIter3()]


class ProcessIter2(object):

    """Class:  ProcessIter

    Description:  Class stub holder for psutil.process_iter class.

    Methods:
        __init__
        as_dict

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.attrs = None
        self.proc = {"cmdline": ["cmd", "java_proc", "bs_proc", "start_arg",
                                 "cf_dir"],
                     "pid": 11111}

    def as_dict(self, attrs):

        """Method:  as_dict

        Description:  as_dict method.

        Arguments:

        """

        self.attrs = attrs

        return self.proc


class Psutil2(object):

    """Class:  Psutil

    Description:  Class stub holder for psutil class.

    Methods:
        __init__
        process_iter

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.process_iter_list = [ProcessIter2()]


class ProcessIter(object):

    """Class:  ProcessIter

    Description:  Class stub holder for psutil.process_iter class.

    Methods:
        __init__
        as_dict

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.attrs = None
        self.proc = {"cmdline": ['cmd']}

    def as_dict(self, attrs):

        """Method:  as_dict

        Description:  as_dict method.

        Arguments:

        """

        self.attrs = attrs

        return self.proc


class Psutil(object):

    """Class:  Psutil

    Description:  Class stub holder for psutil class.

    Methods:
        __init__
        process_iter

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.process_iter_list = [ProcessIter()]


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_multiple_finds
        test_finds
        test_no_finds

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

                self.java_proc = "java_proc"
                self.bs_proc = "bs_proc"
                self.start_arg = "start_arg"
                self.cf_dir = "cf_dir"

        self.cfg = CfgTest()
        self.psutil = Psutil()
        self.psutil2 = Psutil2()
        self.psutil3 = Psutil3()
        self.results = [11111]
        self.results2 = [12345, 12345]

    @mock.patch("cf_monitor.psutil")
    def test_multiple_finds(self, mock_psutil):

        """Function:  test_multiple_finds

        Description:  Test with multiple finds.

        Arguments:

        """

        mock_psutil.process_iter.return_value = self.psutil3.process_iter_list

        self.assertEqual(cf_monitor.find_process(self.cfg), self.results2)

    @mock.patch("cf_monitor.psutil")
    def test_finds(self, mock_psutil):

        """Function:  test_finds

        Description:  Test with one process in list and finds an entry.

        Arguments:

        """

        mock_psutil.process_iter.return_value = self.psutil2.process_iter_list

        self.assertEqual(cf_monitor.find_process(self.cfg), self.results)

    @mock.patch("cf_monitor.psutil")
    def test_no_finds(self, mock_psutil):

        """Function:  test_no_finds

        Description:  Test with one process in list, but no finds.

        Arguments:

        """

        mock_psutil.process_iter.return_value = self.psutil.process_iter_list

        self.assertEqual(cf_monitor.find_process(self.cfg), [])


if __name__ == "__main__":
    unittest.main()
