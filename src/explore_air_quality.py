from pathlib import Path
import pandas as pd

#1. Loading Dataset 
PROJECT_ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = PROJECT_ROOT / "data" / "raw" / (
    "PRSA_Data_Aotizhongxin_20130301-20170228.csv"
)
if not CSV_PATH.is_file():
    raise FileNotFoundError(f"Dataset not found: {CSV_PATH}")
df = pd.read_csv(CSV_PATH)
print("DATASET LOADED")
print("Rows and columns:", df.shape)
print("Column names:", df.columns.tolist())     #Column Names 
print("First five rows:")
print(df.head())    #Top 5 Rows 

#2. Data types and missing values 
print("\nDATA TYPES")
print(df.dtypes)
print("\nMISSING VALUES PER COLUMN")
missing_counts = df.isna().sum()
print(missing_counts)
print("\nTOTAL MISSING CELLS")
print(missing_counts.sum())

#3. Statistical Summary of PM2.5 Column
print("\nPM2.5 SUMMARY")
print(df["PM2.5"].describe())
print("\nNUMBER OF DUPLICATE ROWS")
print(df.duplicated().sum())

# 4. Extractting timestamp from date and time 
df["timestamp"] = pd.to_datetime(
    df[["year", "month", "day", "hour"]]
)
print("\nTIME RANGE")
print("First timestamp:", df["timestamp"].min())
print("Last timestamp:", df["timestamp"].max())
print("Timestamps sorted:", df["timestamp"].is_monotonic_increasing)

#Writing data to the reports file 
report_path = PROJECT_ROOT / "reports" / "inspection_report.txt"
with report_path.open("w", encoding="utf-8") as report:
    report.write(f"Shape: {df.shape}\n")
    report.write("Missing values by column:\n")
    report.write(missing_counts.to_string())
    report.write("\n\nPM2.5 summary:\n")
    report.write(df["PM2.5"].describe().to_string())
    report.write("\n")