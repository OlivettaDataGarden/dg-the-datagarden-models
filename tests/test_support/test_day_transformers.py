from datetime import date, datetime

from datagarden_models.support.date_handler.day_normalizer import DayPeriodTransformer

DT = DayPeriodTransformer()


def test_period_year_to_date_transformer():
    first_quarter = DT.period_start_datetime("2024-10-01")
    assert first_quarter.year == 2024
    assert first_quarter.month == 10
    assert first_quarter.day == 1


def test_period_year_to_str_transformer():
    first_quarter = DT.period_start_str("2024-10-01")
    assert first_quarter == "2024-10-01"


def test_period_date_to_str_transformer():
    first_quarter = DT.period_start_str(date(2024, 10, 1))
    assert first_quarter == "2024-10-01"


def test_period_datetime_to_period_type_str():
    first_quarter = DT.period_start_str(datetime(2024, 10, 1))
    assert first_quarter == "2024-10-01"
