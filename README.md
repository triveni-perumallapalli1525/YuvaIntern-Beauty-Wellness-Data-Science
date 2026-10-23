# Beauty & Wellness Repeat Purchase Analysis

A beginner-friendly Python project prepared to support the YuvaIntern Data Science with Python Analyst Internship.

## Project purpose
This project demonstrates a basic workflow for exploring customer purchase patterns in the beauty and wellness sector. It creates summary tables and charts, and demonstrates a simple repeat-purchase classification baseline.

**Important:** The included dataset is synthetic sample data created for demonstration. It is not real customer data and must not be described as real market evidence. Replace it with a properly licensed public dataset before drawing real-world conclusions.

## Contents
- `data/sample_beauty_wellness_transactions.csv` — synthetic demonstration transactions
- `analysis.py` — data checks, exploratory summaries, charts, and optional baseline model
- `requirements.txt` — Python dependencies
- `outputs/` — generated charts and summary files (created when the script runs)

## Requirements
- Python 3.10 or newer
- pip

## Run on Windows (PowerShell)
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python analysis.py
```

If PowerShell blocks activation, run this only for the current terminal:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

## Outputs
Running `analysis.py` creates:
- `outputs/category_purchase_counts.png`
- `outputs/monthly_order_counts.png`
- `outputs/customer_summary.csv`
- `outputs/category_summary.csv`
- `outputs/model_metrics.txt` (only if a valid target can be constructed)

## Method overview
1. Load the CSV with pandas.
2. Check row counts, column types, missing values, and duplicate transactions.
3. Summarise transactions by product category and month.
4. Build customer-level features from historical transactions.
5. Demonstrate a simple baseline model when the target definition is feasible.
6. Report metrics cautiously and avoid treating synthetic data results as evidence about real customers.

## Data dictionary
- `transaction_id`: synthetic transaction identifier
- `customer_id`: synthetic customer identifier
- `transaction_date`: synthetic transaction date
- `product_category`: example beauty/wellness category
- `quantity`: units purchased
- `order_value`: synthetic order value in INR
- `discount_applied`: whether a synthetic discount was applied

## Limitations and responsible use
- Data is synthetic and for learning only.
- The small sample is not representative of any real company or population.
- Associations do not establish causation.
- A repeat-purchase label based on this small sample is only a demonstration and should not be used for business decisions.
- Use only datasets whose licences and terms permit your intended analysis.

## Internship alignment
This repository supports the Week 1 problem definition and provides a starter foundation for Weeks 2–6. Future reports should cite verified public data sources and clearly separate proposed methods from observed results.
