"""extract.py - Milestone 1: read the raw file into a pandas DataFrame.

The class structure is GIVEN. You complete the method that reads the file.

OOP ideas used here (Session 04):
  - __init__  : the constructor. It runs when you create the object.
  - self      : the object itself; it holds the data.
  - _private  : a leading underscore means "internal - don't use it from outside".
"""
from pathlib import Path

import pandas as pd


class Extractor:
    """Read a CSV file and hand back a pandas DataFrame."""

    def __init__(self, path):
        # GIVEN: the constructor stores the path and prepares the result slot.
        self._path = Path(path)     # private attribute
        self._df = None             # private attribute: the DataFrame will go here

    # ---------------- public method (you complete this) ----------------
    def read(self):
        """Read the CSV at self._path and return the DataFrame.
        
        Steps to write:
          1. If the file is missing, raise FileNotFoundError(self._path).
          2. Read it with pandas:  df = pd.read_csv(self._path)
          3. Store it:            self._df = df
          4. Return it:           return se   lf._df

        HINT: pandas has pd.read_csv(path).  Path has .exists().
        """
        if not self._exists():
            raise FileNotFoundError(self._path)

        df = pd.read_csv(self._path)
        self._df = df
        return self._df
        raise NotImplementedError("TODO(STUDENT): implement Extractor.read()")
    # ---------------- private helper (already written) ----------------
    def _exists(self):
        """Private helper: True if the input file is really there."""
        return self._path.exists()
