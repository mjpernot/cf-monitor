# Changelog
All notable changes to this project will be documented in this file.

The format is based on "Keep a Changelog".  This project adheres to Semantic Versioning.


## [1.0.2] - 2024-03-05
- Updated to work in Red Hat 8
- Updated python-lib to v3.0.3

### Changed
- main, service_cmd, kill_process: Removed gen_libs.get_inst call.
- Set simplejson to 3.12.0 for Python 3.
- Set chardet to 3.0.4 for Python 2.
- Documentation updates.


## [1.0.1] - 2022-12-08
- Updated to work in Python 3 too
- Upgraded python-lib to v2.9.4

### Changed
- Converted imports to use Python 2.7 or Python 3.


## [1.0.0] - 2022-06-28
- General release
- Upgrade python-lib to v2.9.3

### Changed
- main, run_program, monitor, email_admin: Replaced the use of arg_parser (args_array) with gen_class.ArgParser class (args).


## [0.3.0] - 2021-12-20
- Field release.

### Changed
- Removed non-required \*\*kwargs from function parameter list.
- Documentation updates.


## [0.2.0] - 2020-05-14
### Added
- Added -y option to allow flavor IDs for the ProgramLock.

### Fixed
- service_cmd, kill_process, main:  Fixed handling subprocess line.
- email_admin, kill_process, monitor, run_program:  Fixed problem with mutable default arguments issue.

### Changed
- service_cmd:  Changed unused returning parameter to placeholder.
- run_program:  Removed ProgramLock from this function.
- main: Added ProgramLock to this function.
- main:  Refactored "if" statements.
- Documentation updates.


## [0.1.2] - 2018-11-09
### Changed
- email_admin:  Changed "EMAIL" to "email" for instance name.
- get_code:  Changed "CONN" to "conn" for instance name.
- Documentation update.


## [0.1.1] - 2018-09-05
### Changed
- get_code:  Added timeout option to "requests.get", exception handler, and return a status code or exception code.
- monitor:  Added check for Timeout status and pass timeout argument to get_code().


## [0.1.0] - 2018-08-23
- Initial Alpha release.

### Changed
- email_admin:  Added hostname to subject line of email.


## [0.0.1] - 2018-08-21
- Initial pre-alpha release.

