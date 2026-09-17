"""Report basic host health information."""

import logging
import platform
import sys

from app_logging import configure_logging
from configuration import load_config

LOGGER = logging.getLogger(__name__)


def get_system_info():
    import psutil

    memory = psutil.virtual_memory()
    return {
        "Platform": platform.platform(),
        "Python Version": sys.version.split()[0],
        "CPU Count": psutil.cpu_count(),
        "Memory Available (bytes)": memory.available,
        "Memory Total (bytes)": memory.total,
    }


def main():
    try:
        configure_logging(load_config())
        for label, value in get_system_info().items():
            print(f"{label}: {value}")
        LOGGER.info("System health check completed")
    except (OSError, ValueError, ImportError) as exc:
        LOGGER.error("System health check failed: %s", exc)
        raise SystemExit(1) from exc


if __name__ == "__main__":
    main()
