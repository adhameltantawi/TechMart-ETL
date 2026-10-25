"""main.py - the entry point. Four lines of glue, and that is the point.

main.py does no work itself: it builds the objects, calls them in order, and
translates a failure into an exit code. Everything you complete lives in
extract.py, transform.py and load.py.
"""
import logging
import sys
from pathlib import Path

from extract import Extractor
from transform import Transformer
from load import Loader

# The three paths. A later milestone turns these into command-line flags.
INPUT_PATH = "input/orders_sample.csv"
OUTPUT_PATH = "output/orders_clean.csv"
LOG_PATH = "output/etl.log"


def setup_logging(path):
    """Send every log line to a file, at INFO level and above."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        handlers=[logging.FileHandler(path, encoding="utf-8")],
    )
    return logging.getLogger("etl")


def main():
    log = setup_logging(LOG_PATH)
    try:
        log.info("=" * 46)
        log.info("ETL START")

        # 1) EXTRACT -------------------------------------------------
        extractor = Extractor(INPUT_PATH)
        raw = extractor.read()
        n_in = len(raw)
        log.info("extract: read %d rows", n_in)

        # 2) TRANSFORM -----------------------------------------------
        transformer = Transformer(raw, log)
        clean = transformer.run()

        # 3) LOAD + RECONCILE ----------------------------------------
        loader = Loader(clean, OUTPUT_PATH, log)
        loader.save()
        loader.reconcile(n_in, len(clean), n_in - len(clean))

        log.info("ETL DONE -> %s", OUTPUT_PATH)
        return 0

    except FileNotFoundError as exc:
        log.error("%s", exc)
        return 1
    except RuntimeError as exc:
        log.error("%s", exc)
        return 2


if __name__ == "__main__":
    sys.exit(main())
