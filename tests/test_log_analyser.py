import tempfile
import unittest
from pathlib import Path

from log_analyser import analyse_log


class LogAnalyserTests(unittest.TestCase):
    def test_counts_valid_addresses_and_error_lines(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "system.log"
            path.write_text(
                "INFO 192.168.1.1\n"
                "ERROR 10.0.0.2 192.168.1.1\n"
                "ERROR 999.1.1.1\n"
                "INFO no address\n",
                encoding="utf-8",
            )
            counts, errors = analyse_log(path)
            self.assertEqual(dict(counts), {"192.168.1.1": 2, "10.0.0.2": 1})
            self.assertEqual(errors, 2)

    def test_empty_log(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "empty.log"
            path.write_text("")
            self.assertEqual(analyse_log(path), ({}, 0))


if __name__ == "__main__":
    unittest.main()
