"""Load paths from JSON, with environment overrides for deployments."""

import json
import os
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent
DEFAULT_CONFIG = PROJECT_DIR / "config" / "config.json"
ENV_NAMES = {
    "downloads_dir": "TOOLKIT_DOWNLOADS_DIR",
    "source_log": "TOOLKIT_SOURCE_LOG",
    "app_log": "TOOLKIT_APP_LOG",
    "log_level": "TOOLKIT_LOG_LEVEL",
}


def load_config(config_path=None):
    """Resolve relative paths against the directory containing the config file."""
    path = Path(config_path or os.environ.get("TOOLKIT_CONFIG", DEFAULT_CONFIG)).expanduser().resolve()
    with path.open(encoding="utf-8") as file:
        settings = json.load(file)
    if not isinstance(settings, dict):
        raise ValueError("Configuration must be a JSON object")
    for key, env_name in ENV_NAMES.items():
        value = os.environ.get(env_name, settings.get(key))
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"Missing or invalid configuration: {key}")
        settings[key] = value
    for key in ("downloads_dir", "source_log", "app_log"):
        value = Path(settings[key]).expanduser()
        settings[key] = value if value.is_absolute() else (path.parent / value).resolve()
    settings["log_level"] = settings["log_level"].upper()
    return settings
