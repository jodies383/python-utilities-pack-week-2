# Week 3 debugging and configuration report

## Introduction

This project extends the Week 2 file organiser, log analyser, and system health checker.
The goal was to make the scripts repeatable, diagnosable, and portable across machines.

## Problem identified and symptoms

- `log_analyser.py` searched the whole log for IP-like text, then tested `"ERROR" in ip` after the loop. It could not count error lines and an empty log left `ip` undefined.
- `file_organiser.py` assumed `downloads/` existed and moved files into a possibly existing name without checking for collisions. It had duplicate imports and ran at import time.
- `system_health.py` defined `get_system_info()` but never called it when run as a script. The README also named files using American spelling, while the actual filenames use British spelling. `requirements.txt` was referenced but absent.

## Troubleshooting process and root cause

I read each entry point and compared its behavior with the README. The analyser's loop variable was an address string, not a log line, so its error check was both misplaced and logically impossible for ordinary addresses. The organiser depended on the current working directory and had no collision check. The health script lacked a `__main__` entry point.

## Solution

The analyser now streams the log line by line, validates IPv4 addresses, and counts `ERROR` lines independently. The organiser is callable as a function, skips unsupported files and existing destinations, and logs move failures. The health checker now has a main entry point and reports a compact set of metrics. All scripts load JSON settings, accept environment overrides, and write application logs.

## Testing

`python3 -m unittest discover -s tests -v` is the test command. The tests cover file categorisation, collision protection, missing directories, valid and invalid IPs, error lines, empty logs, and configuration overrides. The system `python3` command stops at an unaccepted Xcode license prompt, so I ran the suite using Xcode's Python 3.9 interpreter. An end-to-end run also needs a local `downloads/` directory and `system.log` fixture.

## Prevention and configuration improvements

Tests exercise the bugs that were found. The README now uses the real filenames and explains required inputs. `config/config.json` holds paths and log level. The scripts resolve relative paths from the config file and report missing inputs clearly. Logs and local input data are excluded from Git.

## Cloud readiness and conclusion

A VM or container can provide its own config file or environment values without changing the code. The scripts still run as commands and do not include a deployment definition or scheduler. The main lesson was to turn observed failures into small, testable functions and explicit configuration instead of relying on the current working directory.
