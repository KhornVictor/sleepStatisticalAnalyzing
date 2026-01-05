from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
raw_path = BASE_DIR.parent / "database" / "raw" / "sleep_data.csv"
output_path = BASE_DIR.parent / "database" / "processed" / "sleep_data_clean.csv"
output_path.parent.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(raw_path, sep=';')

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

df["sleep_quality"] = df["sleep_quality"].str.rstrip('%').astype(float)

def to_minutes(val: str) -> float | None:
    if pd.isna(val):
        return None
    text = str(val)
    if text.count(":") == 1:
        text = text + ":00"
    td = pd.to_timedelta(text, errors="coerce")
    return td.total_seconds() / 60 if pd.notna(td) else None

def sleep_duration_minutes(start: str, end: str) -> float | None:
    start_ts = pd.to_datetime(start, errors="coerce")
    end_ts = pd.to_datetime(end, errors="coerce")
    if pd.isna(start_ts) or pd.isna(end_ts):
        return None
    delta = end_ts - start_ts
    if delta.total_seconds() < 0:
        delta += pd.Timedelta(days=1)
    return delta.total_seconds() / 60

df["time_in_bed_min"] = df["time_in_bed"].apply(to_minutes)
df["sleep_duration_min"] = df.apply(
    lambda row: sleep_duration_minutes(row["start"], row["end"]), axis=1
)
df["heart_rate"] = pd.to_numeric(df["heart_rate"], errors="coerce")
df["heart_rate"].fillna(df["heart_rate"].median(), inplace=True)

df = df[["start", "end", "time_in_bed", "heart_rate", "time_in_bed_min"]]

df.to_csv(output_path, index=False)
print(f"Data cleaned and saved to {output_path}")
