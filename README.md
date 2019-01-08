# Python project for the monitoring of the status and health of a ColdFusion application.
# Classification (U)

# Description:
  This program is used to monitor the health of a ColdFusion application.  This includes checking for specific errors and initiating a recycle of the application.


###  This README file is broken down into the following sections:
  * Features
  * Prerequisites
  * Installation
  * Configuration
  * Program Description
  * Program Help Function
  * Help Message
  * Testing
    - Unit
    - Integration
    - Blackbox


# Features:
  * Monitor for specific error codes using request calls.
  * Initiating a recycle of the application under certain conditions.


# Prerequisites:
  * List of Linux packages that need to be installed on the server.
    - python-libs
    - python-devel
    - git
    - python-pip

  * Local class/library dependencies within the program structure.
    - lib/gen_class
    - lib/arg_parser
    - lib/gen_libs


# Installation:

Install the project using git.
  * Replace **{Python_Project}** with the baseline path of the python program.

```
umask 022
cd {Python_Project}
git clone git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/cf-monitor.git
```

Install/upgrade system modules.

```
cd cf-monitor
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

Install supporting classes and libraries.

```
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

# Configuration:

Create ColdFusion Monitoring configuration file.

```
cd config
cp monitor.py.TEMPLATE monitor.py
```

Make the appropriate changes to the environment.
  * Change these entries in the monitor.py file.  Add to or change codes in the default code_list variable.
    - host = "HOSTNAME"
    - code_list = [502, 503, CODE1]
    - url = "http://ADDRESS/"
    - to_line = "EMAIL_ADDRESS@DOMAIN_NAME"
    - cf_dir = "INSTALL_DIR"
    - service = "SERVICE_NAME"

```
vim monitor.py
```
Advance environment variables.
  * Normally these variables do not need to be changed.  Change at your own risk.
    - read_timeout = 200    -> Read timeout setting (in seconds) passed to the requests.get command.  "None" is for indefinite.
    - connect_timeout = 30  -> Connection timeout setting (in seconds) passed to the requests.get command.  "None" is for indefinite.
    - start_sleep = 900     -> Sleep time (in seconds) to wait after a restart before releasing the program lock.


# Program Descriptions:
### Program: cf_monitor.py
##### Description:  Monitor the health of a ColdFusion application.


# Program Help Function:

  All of the programs, except the command and class files, will have an -h (Help option) that will show display a help message for that particular program.  The help message will usually consist of a description, usage, arugments to the program, example, notes about the program, and any known bugs not yet fixed.  To run the help command:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
{Python_Project}/cf-monitor/cf_monitor.py -h
```


# Help Message:
  Below is the help message for each of the programs along with the current version for the program.  Recommend running the -h option on the command line to ensure you have the latest help message for the program.

    Program:  cf_monitor.py

    Description:  Monitor the status of a ColdFusion application.  This will
        include recycling the ColdFusion application if certain conditions are
        met.

    Usage:
        cf_monitor.py -c file -d path [-M] [-v | -h]

    Arguments:
        -M => Monitor only.
        -v => Display version of this program.
        -h => Help and usage message.

        NOTE 1:  -v and -h ovrrides all other options.

    Notes:
        Monitoring configuration file format (monitor.py).  The configuration
        file format:

            host = "HOSTNAME"
            # List of codes to check for
            code_list = [502, 503, CODE1]
            # URL Address to check
            url = "http://ADDRESS/"
            # Email address to administrator
            to_line = "EMAIL_ADDRESS@DOMAIN_NAME"
            # ColdFusion installation directory
            cf_dir = "INSTALL_DIR"
            # ColdFusion service name
            service = "SERVICE_NAME"

    Example:
        cf_monitor.py -c monitor -d config -M


# Testing:

# Unit Testing:

### Description: Testing consists of unit testing for the functions in the cf_monitor.py program.

### Installation:

Install the project using git.
  * Replace **{Python_Project}** with the baseline path of the python program.
  * Replace **{Branch_Name}** with the name of the Git branch being tested.  See Git Merge Request.

```
umask 022
cd {Python_Project}
git clone --branch {Branch_Name} git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/cf-monitor.git
```

Install/upgrade system modules.

```
cd cf-monitor
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

Install supporting classes and libraries.

```
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

# Unit test runs for cf_monitor.py:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd {Python_Project}/cf-monitor
```

### Unit:  help_message
```
   test/unit/cf_monitor/help_message.py
```

### Unit:  
```
   test/unit/cf_monitor/
```

### Unit:  
```
   test/unit/cf_monitor/
```

### Unit:  
```
   test/unit/cf_monitor/
```

### Unit:  
```
   test/unit/cf_monitor/
```

### Unit:  
```
   test/unit/cf_monitor/
```

### Unit:  run_program
```
   test/unit/cf_monitor/run_program.py
```

### Unit:  main
```
   test/unit/cf_monitor/main.py
```

### All unit testing
```
   test/unit/cf_monitor/unit_test_run.sh
```

### Code coverage program
```
   test/unit/cf_monitor/code_coverage.sh
```


# Integration Testing:

### Description: Testing consists of integration testing of functions in the cf_monitor.py program.

### Installation:

Install the project using git.
  * Replace **{Python_Project}** with the baseline path of the python program.
  * Replace **{Branch_Name}** with the name of the Git branch being tested.  See Git Merge Request.

```
umask 022
cd {Python_Project}
git clone --branch {Branch_Name} git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/cf-monitor.git
```

Install/upgrade system modules.

```
cd cf-monitor
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

Install supporting classes and libraries.

```
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

### Configuration:

None at this time.

# Integration test runs for cf_monitor.py:
  * These tests must be run as the root account:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
sudo bash
cd {Python_Project}/cf-monitor
```

### Integration:  
```
   test/integration/cf_monitor/
```

### Integration:  
```
   test/integration/cf_monitor/
```

### Integration:  
```
   test/integration/cf_monitor/
```

### Integration:  
```
   test/integration/cf_monitor/
```

### Integration:  
```
   test/integration/cf_monitor/
```

### Integration:  run_program
```
   test/integration/cf_monitor/run_program.py
```

### Integration:  main
```
   test/integration/cf_monitor/main.py
```

### All integration testing
```
   test/integration/cf_monitor/integration_test_run.sh
```

### Code coverage program
```
   test/integration/cf_monitor/code_coverage.sh
```


# Blackbox Testing:

### Description: Testing consists of blackbox testing of the cf_monitor.py program.

### Installation:

Install the project using git.
  * Replace **{Python_Project}** with the baseline path of the python program.
  * Replace **{Branch_Name}** with the name of the Git branch being tested.  See Git Merge Request.

```
umask 022
cd {Python_Project}
git clone --branch {Branch_Name} git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/cf-monitor.git
```

Install/upgrade system modules.

```
cd cf-monitor
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

Install supporting classes and libraries.

```
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

### Configuration:

None at this time.

# Blackbox test run for cf_monitor.py:
  * These tests must be run as the root account.
  * Replace **{Python_Project}** with the baseline path of the python program.

```
sudo bash
cd {Python_Project}/cf-monitor
test/blackbox/cf_monitor/blackbox_test.sh
```

