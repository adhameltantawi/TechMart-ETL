"""load.py - Milestone 3: write the output and prove the arithmetic.

The class structure is GIVEN. You complete save() and reconcile().
"""
from pathlib import Path
import pandas as pd
from logging import Logger

class Loader:
    """Write the clean DataFrame to CSV, then reconcile the row counts."""

    def __init__(self, df: pd.DataFrame , out_path, log: Logger):
        # GIVEN: the constructor stores the table, the path and the logger.
        self._df = df                    # private attribute
        self._out_path = Path(out_path)  # private attribute
        self._log = log                  # private attribute

    # ---------------- public methods (you complete these) ----------------
    def save(self):
        """Write the clean DataFrame to self._out_path. Return the Path.

        Steps:
          1. Create the parent folder:
                 self._out_path.parent.mkdir(parents=True, exist_ok=True)
          2. Write the CSV:
                 self._df.to_csv(self._out_path, index=False)
          3. Return self._out_path

        HINT: always pass index=False, so the CSV has no extra index column.
        """
        self._out_path.parent.mkdir(parents=True,exist_ok=True)
        self._df.to_csv(self._out_path, index= False)
        self._log.info("Save: %s", self._out_path)
        
    def reconcile(self, n_in, n_kept, n_dropped):
        """Prove rows_in == rows_kept + rows_dropped. Return True.

        If the numbers do not add up, raise RuntimeError.
        If they do, log the one line that proves it:
            self._log.info("reconcile: %d in = %d kept + %d dropped", ...)
        """
        if n_in != n_kept + n_dropped:
            raise RuntimeError("Row count miss match")
        self._log.info("reconcile: %d in %d kept + %d dropped",n_in , n_kept, n_dropped )