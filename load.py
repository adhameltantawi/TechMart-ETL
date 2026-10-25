"""load.py - Milestone 3: write the output and prove the arithmetic.

The class structure is GIVEN. You complete save() and reconcile().
"""
from pathlib import Path


class Loader:
    """Write the clean DataFrame to CSV, then reconcile the row counts."""

    def __init__(self, df, out_path, log):
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
        raise NotImplementedError("TODO(STUDENT): implement Loader.save()")

    def reconcile(self, n_in, n_kept, n_dropped):
        """Prove rows_in == rows_kept + rows_dropped. Return True.

        If the numbers do not add up, raise RuntimeError.
        If they do, log the one line that proves it:
            self._log.info("reconcile: %d in = %d kept + %d dropped", ...)
        """
        raise NotImplementedError("TODO(STUDENT): implement Loader.reconcile()")
