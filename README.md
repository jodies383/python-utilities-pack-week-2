# Python OS Automation Utilities

Three small scripts for organising files, analysing logs, and checking host health.
This Week 3 version adds configuration, application logging, error handling, and tests.

## Requirements

Python 3.12+ and `psutil` for the health checker.

```sh
python3 -m pip install -r requirements.txt
python3 -m unittest discover -s tests -v
```

## Configuration

Edit `config/config.json` for default paths and log level. Relative paths are resolved
from the config file's directory, so the defaults point to this repository's
`downloads/`, `system.log`, and `logs/app.log`. The application creates the app log
directory; create the downloads directory and source log before running their scripts.

For another environment, set `TOOLKIT_CONFIG` to a different JSON file, or override
individual values with `TOOLKIT_DOWNLOADS_DIR`, `TOOLKIT_SOURCE_LOG`,
`TOOLKIT_APP_LOG`, and `TOOLKIT_LOG_LEVEL`. Absolute paths are recommended for
environment overrides. No host-specific path is hard-coded in the scripts.

## Usage

```sh
python3 file_organiser.py
python3 log_analyser.py
python3 system_health.py
```

The organiser moves PDF files to `Documents/` and JPEG/PNG files to `Images/`.
It leaves other files and same-named destination files alone. The analyser reports
valid IPv4 address counts and the number of lines containing `ERROR`. The health
checker prints platform, Python version, CPU count, and memory values in bytes.
All three commands write operational messages to the configured app log.

See [WEEK3_REPORT.md](WEEK3_REPORT.md) for the debugging and configuration report.
