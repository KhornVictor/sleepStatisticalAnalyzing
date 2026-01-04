from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
raw_path = BASE_DIR.parent / "database" / "raw" / "sleep_data.csv"
output_path = BASE_DIR.parent / "database" / "processed" / "sleep_data_clean.csv"
output_path.parent.mkdir(parents=True, exist_ok=True)

# Load raw data; the file uses semicolons as separators
df = pd.read_csv(raw_path, sep=';')

# Standardize column names
df.rename(
    columns={
        "Start": "start",
        "End": "end",
        "Sleep quality": "sleep_quality",
        "Time in bed": "time_in_bed",
        "Wake up": "wake_up",
        "Sleep Notes": "sleep_notes",
        "Heart rate": "heart_rate",
    },
    inplace=True,
)

# Clean and enrich fields
df["sleep_quality"] = df["sleep_quality"].str.rstrip('%').astype(float)

# Some rows are hh:mm without seconds; make them hh:mm:ss before conversion
def to_minutes(val: str) -> float | None:
    if pd.isna(val):
        return None
    text = str(val)
    if text.count(":") == 1:
        text = text + ":00"
    td = pd.to_timedelta(text, errors="coerce")
    return td.total_seconds() / 60 if pd.notna(td) else None

df["time_in_bed_min"] = df["time_in_bed"].apply(to_minutes)
df["heart_rate"] = pd.to_numeric(df["heart_rate"], errors="coerce")
df["heart_rate"].fillna(df["heart_rate"].median(), inplace=True)

# Persist cleaned dataset
df.to_csv(output_path, index=False)
print(f"Data cleaned and saved to {output_path}")
