"""transform.py - Milestone 2: the four cleanups, in order.

The class structure and the ORDER of the steps are GIVEN.
You complete each private step (the four _clean* methods).

The order is not arbitrary:
  1. dedupe   -> a row is never counted twice
  2. amount   -> coerce to numbers, drop what cannot be read
  3. dates    -> turn the five date formats into one datetime column
  4. keys     -> city casing + customer_id, so grouping works later
"""
import re

import pandas as pd


class Transformer:
    """Clean the raw DataFrame. DataFrame in, DataFrame out."""

    def __init__(self, df: pd.DataFrame, log: Logger):
        # GIVEN: the constructor stores the working table and the logger.
        self._df = df        # private attribute
        self._log = log      # private attribute

    # ---------------- public method (given) ----------------
    def run(self):
        """Run the four cleanups in order and return the clean DataFrame."""
        self._dedupe()
        self._clean_amount()
        self._clean_dates()
        self._clean_keys()
        self._log.info("transform: %d rows out", len(self._df))
        return self._df

    # ---------------- private steps (you complete these) ----------------
    def _dedupe(self):
        """Remove duplicate order_id rows. Keep the first. Log the count.

        HINT: df.drop_duplicates(subset=["order_id"], keep="first")
              Then .copy() so pandas stops warning about a view.
              Log with self._log.info("dedupe: %d -> %d", before, after).
        """
        before = len(self._df)
        self._df = self._df.drop_duplicates(subset=["order_id"], keep="first")
        after = len(self._df)
        self._log.info("dedupe: %d -> %d", before,after)


    def parse_amount(text):
      text = str(text).strip()
      text = re.sub(r"[A-Za-z]","",text)
      if not re.fullmatch(r"[\d,]+(\.\d+)?", text):
          return None

      return float(text.replace(",", "")) 

    def _clean_amount(self):
        """Make `amount` a number and drop rows whose amount is unreadable.

        The raw column mixes: "EGP 12,450.00", "USD 30.00", "n/a",
        "pending", "one thousand", "EGP 12.450.00", "EGP 1,2x0.00".

        Rules:
          - allow an optional leading currency word (letters + spaces)
          - then only digits and commas, with at most ONE decimal dot
          - anything else is unreadable -> drop the row
          - remove the commas, then convert to float

        HINT: re.fullmatch(r"[\\d,]+(\\.\\d+)?", rest)
              Use .map() to clean the column, then .dropna(subset=["amount"]).
      """
        before = len(self._df)
        self._df["amount"] = self._df["amount"].map(self.parse_amount)
        self._df = self._df.dropna(subset='amount').copy()
        after = len(self._df)
        self._log.info("clean_amount: %d -> %d", before,after)

    def _clean_dates(self):
        """Turn `order_date` into real datetimes. Keep NaT for unreadable ones.

        Formats found in the file:
          "2025-01-04"   ISO
          "04/01/2025"   EU (dd/mm/yyyy)
          "01-04-2025"   US (mm-dd-yyyy)
          "45661"        Excel day-count  -> 1899-12-30 + 45661 days
          "Jan 4, 2025"  written month
          "20250104"     compact
          "garbage", "0000-00-00"  -> NaT (kept, not dropped)

        Steps:
          1. find the numeric day-counts (between 20000 and 60000)
          2. convert them to "YYYY-MM-DD"
          3. pd.to_datetime(col, format="mixed", errors="coerce")

        HINT: pd.to_datetime(..., format="mixed", errors="coerce")
        """
        col = self._df['order_date'].astype("string").str.strip()
        numeric = pd.to_numeric(col, errors="coerce")

        mask = numeric.between(20000,60000)
        col.loc[mask] = (
            pd.to_datetime(
                numeric.loc[mask],
                unit = "D",
                origin = "1899-12-30",
            ).dt.strftime("%Y-%m-%d")
        )
        mask_compact = col.str.fullmatch(r"\d{8}", na=False)
        col.loc[mask_compact] = (
            col.loc[mask_compact].str[:4] 
            + "-" 
            + col.loc[mask_compact].str[4:6] 
            + "-" 
            + col.loc[mask_compact].str[6:]
        )

        self._df["order_date"] = pd.to_datetime(col,format = "mixed",dayfirst=True, errors="coerce")
        self._log.info("dates: %d unreadable kept as NaT",self._df["order_date"].isna().sum())

    def _clean_keys(self):
        """Normalise `city` and fill missing `customer_id` with "GUEST".

        HINT: .str.strip().str.title()   and   .fillna("GUEST")
        """
        raise NotImplementedError("TODO(STUDENT): implement Transformer._clean_keys()")
