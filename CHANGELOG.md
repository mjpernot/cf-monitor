# Changelog
All notable changes to this project will be documented in this file.

The format is based on "Keep a Changelog".  This project adheres to Semantic Versioning.


## [0.3.0] - 2021-12-20
- Field release.

### Changed
- Documentation updates.


## [0.2.0] - 2020-05-14
### Added
- Added -y option to allow flavor IDs for the ProgramLock.

### Fixed
- service_cmd:  Fixed handling subprocess line from SonarQube scan finding.
- kill_process:  Fixed handling subprocess line from SonarQube scan finding.
- main: Fixed handling command line arguments from SonarQube scan finding.
- email_admin:  Fixed problem with mutable default arguments issue.
- kill_process:  Fixed problem with mutable default arguments issue.
- monitor:  Fixed problem with mutable default arguments issue.
- run_program:  Fixed problem with mutable default arguments issue.

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

