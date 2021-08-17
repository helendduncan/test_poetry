import sys
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib as plt

def reader(pth):
    #Read in the path to the (demo) file
    selected_file = Path(pth)
    if not selected_file.exists():
        raise IOError("Cannot find file")
    return f"Using file {selected_file}"
