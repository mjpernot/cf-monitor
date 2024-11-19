# Python project for the monitoring of the status and health of a ColdFusion application.
# Classification (U)

# Description:
  Used to monitor the health of a ColdFusion application.  This includes checking for specific errors and initiating a recycle of the application.


###  This README file is broken down into the following sections:
  * Features
  * Prerequisites
  * Installation
  * Configuration
  * Program Help Function
  * Testing
    - Unit


# Features:
  * Monitor for specific error codes using request calls.
  * Initiating a recycle of the application under certain conditions.


# Prerequisites:
  * List of Linux packages that need to be installed on the server.
    - Centos 7 (Running Python 2.7):
      -> python-pip
      -> python-devel
    - Redhat 8 (Running Python 3.6):
      -> python3-pip
      -> python3-devel
      -> gcc


# Installation:

Install the project using git.
  * From here on out, any reference to **{Python_Project}** or **PYTHON_PROJECT** replace with the baseline path of the python program.

```
git clone git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/cf-monitor.git
cd cf-monitor
```

Install/upgrade system modules.

Centos 7 (Running Python 2.7):
```
sudo pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
```

Redhat 8 (Running Python 3.6):
NOTE: Install as the user that will run the program.

```
python -m pip install --user -r requirements3.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
```


Install supporting classes and libraries.

Centos 7 (Running Python 2.7):
```
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

Redhat 8 (Running Python 3.6):
```
python -m pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
```


# Configuration:

Make the appropriate changes to the environment.
  * Change these entries in the monitor.py file.  Add to or change codes in the default code_list variable.
    - host = "HOSTNAME"
    - code_list = [502, 503, CODE1]
    - url = "http://ADDRESS/"
    - to_line = "EMAIL_ADDRESS@DOMAIN_NAME"
    - cf_dir = "INSTALL_DIR"
    - service = "SERVICE_NAME"

  * Advance environment variables.  Normally these variables do not need to be changed.  Change at your own risk.
    - read_timeout = 200    -> Read timeout setting (in seconds) passed to the requests.get command.  "None" is for indefinite.
    - connect_timeout = 30  -> Connection timeout setting (in seconds) passed to the requests.get command.  "None" is for indefinite.
    - start_sleep = 900     -> Sleep time (in seconds) to wait after a restart before releasing the program lock.

```
cd config
cp monitor.py.TEMPLATE monitor.py
vim monitor.py
```


# Program Help Function:

  All of the programs, except the command and class files, will have an -h (Help option) that will show display a help message for that particular program.  The help message will usually consist of a description, usage, arugments to the program, example, notes about the program, and any known bugs not yet fixed.  To run the help command:

```
{Python_Project}/cf-monitor/cf_monitor.py -h
```


# Testing:

# Unit Testing:

### Installation:

Install the project using the procedures in the Installation section.

### Testing:

```
cd {Python_Project}/cf-monitor
test/unit/cf_monitor/unit_test_run3.sh
```

### Code Coverage:
```
cd {Python_Project}/cf-monitor
test/unit/cf_monitor/code_coverage.sh
```

