# TechMart ETL — Project 1

A beginner ETL tool: read a messy CSV, clean it with pandas, write a clean CSV.
It uses only the simple ideas from Sessions 01–05: functions, `logging`, `regex`,
**simple OOP** (`__init__`, `self`, private `_names`) and **pandas**.

## The one sentence

```
python main.py
```

reads `input/orders_sample.csv`, cleans it, and writes `output/orders_clean.csv`.

## The four files

| File | Job | What **you** complete |
|------|-----|-----------------------|
| `main.py` | glue: build the objects, call them in order | nothing — it is given |
| `extract.py` | read the CSV into a DataFrame | `Extractor.read()` |
| `transform.py` | the four cleanups | `_dedupe`, `_clean_amount`, `_clean_dates`, `_clean_keys` |
| `load.py` | write the CSV + reconcile | `save()`, `reconcile()` |

The structure (classes, `__init__`, method names, the order of the steps) is
given. Search the code for **`TODO(STUDENT)`** — those are the missing parts.

## Run it

```
python main.py
```

Every step is logged to `output/etl.log` at INFO and above. Exit codes:
`0` success · `1` bad input (missing file) · `2` rows do not add up.

## The answer you are aiming for

```
4,240 rows in  =  3,915 kept  +  325 dropped
325 dropped    =  120 duplicate order_id  +  205 unreadable amounts
```

When the log shows `reconcile: 4240 in = 3915 kept + 325 dropped`, you are done.
If the numbers do not add up, the tool exits non-zero — that is the point.

## Verify (the four checks)

1. **Idempotency** — run it twice; the two output files must be byte-identical.
2. **Reconciliation** — `4240 = 3915 + 325`, every single run.
3. **A hand-checked sample** — open 10 output rows against the 10 raw rows.
4. **A failure that fails** — point it at a missing file and confirm exit code 1.

## The four cleanups (in this order — the order matters)

1. **dedupe** — drop duplicate `order_id`, keep the first, log the count.
2. **amount** — make it numeric; drop rows whose amount is unreadable.
3. **dates** — parse all five formats into one `datetime` column (unreadable → `NaT`).
4. **keys** — normalise `city`, fill missing `customer_id` with `GUEST`.

## Setup

```
python -m venv .venv
# Windows:  .venv\Scripts\activate     macOS/Linux:  source .venv/bin/activate
pip install -r requirements.txt
```
