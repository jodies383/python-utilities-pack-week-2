"""Shared application logging setup."""

import logging


def configure_logging(settings):
    level = getattr(logging, settings["log_level"], None)
    if not isinstance(level, int):
        raise ValueError(f"Invalid log level: {settings['log_level']}")
    log_path = settings["app_log"]
    log_path.parent.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        level=level,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
        handlers=[logging.FileHandler(log_path, encoding="utf-8"), logging.StreamHandler()],
        force=True,
    )
