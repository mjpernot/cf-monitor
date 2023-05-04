#!/bin/bash
# Unit testing program for the program module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file
#   is located at.

echo ""
echo "Unit testing..."
/usr/bin/python3 test/unit/cf_monitor/email_admin.py
/usr/bin/python3 test/unit/cf_monitor/find_process.py
/usr/bin/python3 test/unit/cf_monitor/get_code.py
/usr/bin/python3 test/unit/cf_monitor/help_message.py
/usr/bin/python3 test/unit/cf_monitor/kill_process.py
/usr/bin/python3 test/unit/cf_monitor/main.py
/usr/bin/python3 test/unit/cf_monitor/monitor.py
/usr/bin/python3 test/unit/cf_monitor/run_program.py
/usr/bin/python3 test/unit/cf_monitor/service_cmd.py
