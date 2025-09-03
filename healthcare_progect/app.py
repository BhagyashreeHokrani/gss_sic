from flask import Flask, render_template
import pandas as pd
from datetime import datetime

app = Flask(__name__)

def transform_data():
    # 1. Load Dataset
    df = pd.read_csv("patient_admissions.csv")

    # 2. Handle Missing Values
    df["Diagnosis"] = df["Diagnosis"].fillna("Unknown")
    df["DischargeDate"] = df["DischargeDate"].fillna(datetime.today().strftime("%d-%m-%Y"))

    # 3. Data Type Conversion
    df["AdmissionDate"] = pd.to_datetime(df["AdmissionDate"], dayfirst=True, errors="coerce")
    df["DischargeDate"] = pd.to_datetime(df["DischargeDate"], dayfirst=True, errors="coerce")

    # 4. Create Derived Column
    df["StayDuration"] = (df["DischargeDate"] - df["AdmissionDate"]).dt.days

    # 5. Filter Data
    cardiology_patients = df[(df["Department"] == "Cardiology") & (df["StayDuration"] > 5)]

    # 6. Group and Aggregate
    admissions_per_dept = df.groupby("Department")["PatientID"].count().to_dict()
    avg_stay_per_dept = df.groupby("Department")["StayDuration"].mean().round(2).to_dict()

    # 7. Sort Data
    df = df.sort_values(by="StayDuration", ascending=False)

    # 8. Remove Duplicates
    df = df.drop_duplicates(subset=["PatientID", "AdmissionDate"], keep="first")

    # 9. Save Transformed Data
    df.to_csv("transformed_admissions.csv", index=False)

    return df, cardiology_patients, admissions_per_dept, avg_stay_per_dept


@app.route("/")
def index():
    df, cardiology_patients, admissions_per_dept, avg_stay_per_dept = transform_data()

    return render_template(
        "index.html",
        tables=df.to_html(classes="table table-bordered", index=False),
        cardiology=cardiology_patients.to_html(classes="table table-striped", index=False),
        admissions=admissions_per_dept,
        avg_stay=avg_stay_per_dept
    )


if __name__ == "__main__":
    app.run(debug=True)
