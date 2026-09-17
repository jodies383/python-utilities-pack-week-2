"""Summarise valid IPv4 addresses and error lines in a log file."""

import ipaddress
import logging
import re
from collections import Counter

from app_logging import configure_logging
from configuration import load_config

LOGGER = logging.getLogger(__name__)
IP_CANDIDATE = re.compile(r"(?<![\w.])(?:\d{1,3}\.){3}\d{1,3}(?![\w.])")


def analyse_log(path):
    counts = Counter()
    error_lines = 0
    with open(path, encoding="utf-8", errors="replace") as log_file:
        for line in log_file:
            if "ERROR" in line:
                error_lines += 1
            for candidate in IP_CANDIDATE.findall(line):
                try:
                    address = ipaddress.IPv4Address(candidate)
                except ipaddress.AddressValueError:
                    continue
                counts[str(address)] += 1
    return counts, error_lines


def main():
    try:
        settings = load_config()
        configure_logging(settings)
        counts, error_lines = analyse_log(settings["source_log"])
        for address, count in counts.most_common():
            print(f"{address}: {count}")
        print(f"ERROR lines: {error_lines}")
        LOGGER.info("Analysed %s: %d IP occurrences, %d error lines", settings["source_log"], sum(counts.values()), error_lines)
    except (OSError, ValueError) as exc:
        LOGGER.error("Log analyser failed: %s", exc)
        raise SystemExit(1) from exc


if __name__ == "__main__":
    main()
