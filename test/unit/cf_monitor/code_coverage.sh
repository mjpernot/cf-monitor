#!/bin/bash
# Unit test code coverage for program module.
# This will run the Python code coverage module against all unit test modules.
# This will show the amount of code that was tested and which lines of code
#   that was skipped during the test.

coverage erase

echo ""
echo "Running unit test modules in conjunction with coverage"
coverage run -a --source=cf_monitor test/unit/cf_monitor/email_admin.py
coverage run -a --source=cf_monitor test/unit/cf_monitor/find_process.py
coverage run -a --source=cf_monitor test/unit/cf_monitor/get_code.py
coverage run -a --source=cf_monitor test/unit/cf_monitor/help_message.py
coverage run -a --source=cf_monitor test/unit/cf_monitor/kill_process.py
coverage run -a --source=cf_monitor test/unit/cf_monitor/service_cmd.py

echo ""
echo "Producing code coverage report"
coverage combine
coverage report -m
