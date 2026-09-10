import os
import shutil
from pathlib import Path


from pathlib import Path
import shutil

folder = Path("downloads")

for file in folder.iterdir():

    if file.suffix == ".pdf":
        destination = folder / "Documents"

        destination.mkdir(exist_ok=True)

        shutil.move(file, destination / file.name)
    elif file.suffix == ".jpg" or file.suffix == ".png":   
        destination = folder / "Images"

        destination.mkdir(exist_ok=True)

        shutil.move(file, destination / file.name) 
    