from datetime import date, datetime

from datagarden_models.support.date_handler.year_normalizer import YearPeriodTransformer

YT = YearPeriodTransformer()


def test_period_year_to_date_transformer():
    first_quarter = YT.period_start_datetime("2024")
    assert first_quarter.year == 2024
    assert first_quarter.month == 1
    assert first_quarter.day == 1


def test_period_year_to_str_transformer():
    first_quarter = YT.period_start_str("2024")
    assert first_quarter == "2024-01-01"


def test_period_date_year_to_str_transformer():
    first_quarter = YT.period_start_str(date(2024, 10, 10))
    assert first_quarter == "2024-01-01"


def test_year_str_to_date_2024_01_01():
    year = YT._str_to_date("2024-01-01")
    assert year == datetime(2024, 1, 1)


def test_year_str_to_date_2024():
    year = YT._str_to_date("2024-01-01")
    assert year == datetime(2024, 1, 1)


def test_year_str_to_date_1_1_2024():
    year = YT._str_to_date("1-1-2024")
    assert year == datetime(2024, 1, 1)


def test_is_valid_year_str():
    assert YT.validate("2024")


def test_is_valid_year_date():
    assert YT.validate(date(2024, 1, 1))


def test_is_valid_year_datetime():
    assert YT.validate(datetime(2024, 1, 1))


def test_is_invalid_year_str_invalid():
    assert not YT.validate("202-01-01")
