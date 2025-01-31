from datetime import datetime
import pandas as pd

def calculate_age(dob):
    """
    Calculate the age based on the given date of birth (dob).
    Handles missing or invalid values gracefully.
    """
    if pd.isnull(dob):
        return None  # Return None for missing dates
    try:
        dob = str(dob)  # Ensure dob is a string
        dob = datetime.strptime(dob, '%Y-%m-%d')
        today = datetime.today()
        return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    except ValueError:
        return None  # Return None for invalid date formats

def days_since_last_consult(last_consulted_date):
    """
    Calculate the number of days since the last consultation.
    Handles missing or invalid values gracefully.
    """
    if pd.isnull(last_consulted_date):
        return None  # Return None for missing dates
    try:
        last_consulted_date = str(last_consulted_date)  # Ensure it's a string
        last_consulted_date = datetime.strptime(last_consulted_date, '%Y-%m-%d')
        today = datetime.today()
        return (today - last_consulted_date).days
    except ValueError:
        return None  # Return None for invalid date formats
