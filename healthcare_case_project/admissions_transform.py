import pandas as pd
from datetime import datetime

# Input & Output filenames
INPUT_CSV = "patient_admissions.csv"
OUTPUT_CSV = "transformed_admissions.csv"

def main():
    # 1. Load Dataset
    df = pd.read_csv(INPUT_CSV)

    # 2. Check Data Quality
    print("\n=== Missing Values per Column ===")
    print(df.isna().sum())
    print("\n=== Data Types ===")
    print(df.dtypes)
    print("\n=== Duplicate Admissions (same PatientID + AdmissionDate) ===")
    print(df.duplicated(subset=["PatientID", "AdmissionDate"]).sum())

    # 3. Handle Missing Values
    df["Diagnosis"].fillna("Unknown", inplace=True)
    today = pd.to_datetime(datetime.today().date())
    df["DischargeDate"].fillna(today, inplace=True)

    # 4. Convert Data Types
    df["AdmissionDate"] = pd.to_datetime(df["AdmissionDate"])
    df["DischargeDate"] = pd.to_datetime(df["DischargeDate"])

    # 5. Create Derived Column: StayDuration
    df["StayDuration"] = (df["DischargeDate"] - df["AdmissionDate"]).dt.days

    # 6. Filter Data: Cardiology with stay > 5
    cardiology_long = df[(df["Department"] == "Cardiology") & (df["StayDuration"] > 5)]
    print("\n=== Cardiology patients with StayDuration > 5 ===")
    print(cardiology_long)

    # 7. Group & Aggregate
    dept_counts = df.groupby("Department")["PatientID"].count()
    dept_avg_stay = df.groupby("Department")["StayDuration"].mean()
    print("\n=== Admissions per Department ===")
    print(dept_counts)
    print("\n=== Average Stay Duration per Department ===")
    print(dept_avg_stay)

    # 8. Sort Data: By StayDuration
    df_sorted = df.sort_values(by="StayDuration", ascending=False)

    # 9. Remove Duplicates
    df_final = df_sorted.drop_duplicates(subset=["PatientID", "AdmissionDate"])

    # 10. Export Transformed Data
    df_final.to_csv(OUTPUT_CSV, index=False)
    print(f"\n✅ Cleaned file saved as: {OUTPUT_CSV}")

if __name__ == "__main__":
    main()

