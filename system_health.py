import os
import platform
import sys
import psutil  # type: ignore[import-not-found]



def get_system_info():
    print(f"Platform: {platform.platform()}")
    print(f"Python Version: {sys.version}")
    print(f"CPU Count: {psutil.cpu_count()}")
    print(f"Memory Available: {psutil.virtual_memory().available}")
    print(f"Memory Total: {psutil.virtual_memory().total}")