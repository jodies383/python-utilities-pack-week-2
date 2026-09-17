"""Move supported files into category directories."""

import logging
import shutil
from pathlib import Path

from app_logging import configure_logging
from configuration import load_config

LOGGER = logging.getLogger(__name__)
CATEGORIES = {".pdf": "Documents", ".jpg": "Images", ".jpeg": "Images", ".png": "Images"}


def organise_files(folder):
    folder = Path(folder)
    if not folder.is_dir():
        raise NotADirectoryError(f"Downloads directory does not exist: {folder}")
    moved = 0
    for source in folder.iterdir():
        if not source.is_file() or source.is_symlink():
            continue
        category = CATEGORIES.get(source.suffix.lower())
        if category is None:
            continue
        destination_dir = folder / category
        destination = destination_dir / source.name
        if destination.exists():
            LOGGER.warning("Skipping %s: destination exists", source)
            continue
        destination_dir.mkdir(exist_ok=True)
        try:
            shutil.move(str(source), str(destination))
        except OSError:
            LOGGER.exception("Could not move %s", source)
            continue
        LOGGER.info("Moved %s to %s", source, destination)
        moved += 1
    return moved


def main():
    try:
        settings = load_config()
        configure_logging(settings)
        print(f"Moved {organise_files(settings['downloads_dir'])} files")
    except (OSError, ValueError) as exc:
        LOGGER.error("File organiser failed: %s", exc)
        raise SystemExit(1) from exc


if __name__ == "__main__":
    main()
