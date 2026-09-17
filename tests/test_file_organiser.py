import tempfile
import unittest
from pathlib import Path

from file_organiser import organise_files


class FileOrganiserTests(unittest.TestCase):
    def test_moves_supported_files_and_preserves_existing_destination(self):
        with tempfile.TemporaryDirectory() as directory:
            folder = Path(directory)
            (folder / "report.PDF").write_text("new")
            (folder / "photo.jpg").write_text("image")
            (folder / "notes.txt").write_text("keep")
            (folder / "Documents").mkdir()
            (folder / "Documents" / "report.PDF").write_text("old")
            self.assertEqual(organise_files(folder), 1)
            self.assertEqual((folder / "Documents" / "report.PDF").read_text(), "old")
            self.assertTrue((folder / "report.PDF").exists())
            self.assertTrue((folder / "Images" / "photo.jpg").exists())
            self.assertTrue((folder / "notes.txt").exists())

    def test_missing_folder_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(NotADirectoryError):
                organise_files(Path(directory) / "missing")


if __name__ == "__main__":
    unittest.main()
