# Classification (U)

"""Program:  email_admin.py

    Description:  Unit testing of email_admin in cf_monitor.py.

    Usage:
        test/unit/cf_monitor/email_admin.py

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


class Mail(object):

    """Class:  Mail

    Description:  Class stub holder for gen_class.Mail class.

    Methods:
        __init__
        add_2_msg
        send_mail

    """

    def __init__(self, to_line, subj, frm_line):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.to_line = to_line
        self.subj = subj
        self.frm_line = frm_line
        self.data = None

    def add_2_msg(self, data):

        """Method:  add_2_msg

        Description:  add_2_msg method.

        Arguments:

        """

        self.data = data

    def send_mail(self):

        """Method:  send_mail

        Description:  send_mail method.

        Arguments:

        """

        return True


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

        self.to_line = ["Email_Addresses"]


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_not_monitoring
        test_monitor_only

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.cfg = CfgTest()
        self.args = ArgParser()
        self.args2 = ArgParser()
        self.args.args_array = {"-M": True}
        self.args2.args_array = {}
        self.code = 400
        self.to_line = "to_line"
        self.subj = "subj"
        self.frm_line = "frm_line"
        self.mail = Mail(self.to_line, self.subj, self.frm_line)

    @mock.patch("cf_monitor.gen_class.Mail")
    def test_not_monitoring(self, mock_mail):

        """Function:  test_not_monitoring

        Description:  Test with no -M in args_array.

        Arguments:

        """

        mock_mail.return_value = self.mail

        self.assertFalse(
            cf_monitor.email_admin(self.args2, self.cfg, self.code))

    @mock.patch("cf_monitor.gen_class.Mail")
    def test_monitor_only(self, mock_mail):

        """Function:  test_monitor_only

        Description:  Test with -M in args_array.

        Arguments:

        """

        mock_mail.return_value = self.mail

        self.assertFalse(
            cf_monitor.email_admin(self.args, self.cfg, self.code))


if __name__ == "__main__":
    unittest.main()
