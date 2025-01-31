import pytest
import sys
import os
from datetime import datetime
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from src.utils import calculate_age, days_since_last_consult


def test_calculate_age():
    assert calculate_age("2000-01-01") == datetime.today().year - 2000
    assert calculate_age("invalid_date") is None
    assert calculate_age(None) is None

def test_days_since_last_consult():
    today = datetime.today().strftime("%Y-%m-%d")
    assert days_since_last_consult(today) == 0
    assert days_since_last_consult("2000-01-01") > 8000
    assert days_since_last_consult("invalid_date") is None
    assert days_since_last_consult(None) is None
