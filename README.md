# Sleep Analysis Project

This project analyzes sleep quality, sleep duration, and heart rate using Python.  
It is based on a personal sleep tracking dataset and includes data cleaning, visualization, and basic statistical analysis.

## Project Goals
- Explore patterns between sleep duration, sleep quality, and heart rate
- Visualize sleep patterns using plots
- Perform basic linear regression to analyze correlations
- Optionally investigate effects of sleep notes like coffee, tea, or stress

---

## Project Structure

```
sleep_analysis_project/
│
├── data/
│ ├── raw/
│ └── processed/
│
├── notebooks/
│ ├── 01_data_exploration.ipynb
│ └── 02_analysis.ipynb
│
├── scripts/
│ ├── data_cleaning.py
│ └── analysis.py
│
├── results/
│ ├── plots/
│ └── summary_tables/
│
├── reports/
│ └── project_report.pdf 
├── requirements.txt 
└── README.md
```

## Structure Detail
- `data/` - raw and processed datasets
- `notebooks/` - Jupyter notebooks for analysis
- `scripts/` - Python scripts for cleaning and analysis
- `results/` - figures and tables
- `reports/` - final report

---

## Create Environment

``` bash
python -m venv .env
```

## Requirements

- Python 3.10+  
- Packages: pandas, numpy, matplotlib, seaborn, statsmodels, jupyter

Install required packages using:

```bash
python -m pip install -r requirements.txt
```

## How to Run
1. Activate Python environment
```bash
# Linux / Mac
source venv/bin/activate

# Windows
venv\Scripts\activate
```
2. Run dataclean to prepare the dataset
```bash
python scripts/data_cleaning.py

```
3. Open notebooks for exploration and analysis