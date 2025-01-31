import os
import pandas as pd
from utils import calculate_age, days_since_last_consult

def process_file(input_path, output_path, country):
    print(f"Processing file for {country}...")
    try:
        # Load the data
        df = pd.read_csv(input_path)
        print(f"Initial data from {input_path}:\n{df.head()}\n")

        # Handle different schemas for each country
        if country == "India":
            df.rename(columns={
                "ID": "id", "Name": "name", "DOB": "dob", 
                "VaccinationType": "vaccination_type", "VaccinationDate": "vaccination_date", 
                "Free or Paid": "payment_type"
            }, inplace=True)
        elif country == "Australia":
            df.rename(columns={
                "Unique ID": "id", "Patient Name": "name", "Date of Birth": "dob",
                "Vaccine Type": "vaccination_type", "Date of Vaccination": "vaccination_date"
            }, inplace=True)
        elif country == "USA":
            df.rename(columns={
                "ID": "id", "Name": "name", "VaccinationType": "vaccination_type", 
                "VaccinationDate": "vaccination_date"
            }, inplace=True)
            df["dob"] = None  # USA dataset has no DOB

        # Standardize date formats
        df["dob"] = pd.to_datetime(df["dob"], errors="coerce", format="%Y-%m-%d")
        df["vaccination_date"] = pd.to_datetime(df["vaccination_date"], errors="coerce")

        print(f"Data after standardizing dates for {country}:\n{df.head()}\n")

        # Add derived columns
        df["age"] = df["dob"].apply(calculate_age)
        df["days_since_last_vaccination"] = df["vaccination_date"].apply(days_since_last_consult)

        print(f"Data after adding derived columns for {country}:\n{df.head()}\n")

        # Remove invalid or unnecessary rows if needed
        df.dropna(subset=["vaccination_date"], inplace=True)

        # Save the cleaned data
        df.to_csv(output_path, index=False)
        print(f"File processed and saved to {output_path}.")
    except Exception as e:
        print(f"Error processing file for {country}: {e}")


def main():
    # Define input and output file paths
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_dir = os.path.join(base_dir, "../data")
    output_dir = os.path.join(base_dir, "../output")
    
    # File paths for each country
    files = {
        "India": {"input": os.path.join(input_dir, "ind.csv"), "output": os.path.join(output_dir, "cleaned_ind.csv")},
        "Australia": {"input": os.path.join(input_dir, "aus.csv"), "output": os.path.join(output_dir, "cleaned_aus.csv")},
        "USA": {"input": os.path.join(input_dir, "usa.csv"), "output": os.path.join(output_dir, "cleaned_usa.csv")}
    }

    # Process each file
    for country, paths in files.items():
        process_file(paths["input"], paths["output"], country)

if __name__ == "__main__":
    main()
