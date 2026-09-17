import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from configuration import load_config


class ConfigurationTests(unittest.TestCase):
    def test_relative_paths_use_config_directory_and_env_can_override(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            config = root / "config.json"
            config.write_text(json.dumps({
                "downloads_dir": "downloads", "source_log": "system.log",
                "app_log": "logs/app.log", "log_level": "info",
            }))
            override = root / "other.log"
            with patch.dict(os.environ, {"TOOLKIT_SOURCE_LOG": str(override)}, clear=True):
                settings = load_config(config)
            self.assertEqual(settings["downloads_dir"], root / "downloads")
            self.assertEqual(settings["source_log"], override)
            self.assertEqual(settings["log_level"], "INFO")


if __name__ == "__main__":
    unittest.main()
