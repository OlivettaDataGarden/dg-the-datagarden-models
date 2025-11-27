from datetime import date, datetime

from datagarden_models.support.date_handler.month_normalizer import (
	MonthPeriodTransformer,
)

MT = MonthPeriodTransformer()


def test_period_month_to_date_transformer():
	first_quarter = MT.period_start_datetime("2024-01")
	assert first_quarter.year == 2024
	assert first_quarter.month == 1
	assert first_quarter.day == 1


def test_period_month_to_str_transformer():
	month = MT.period_start_str("2024-02")
	assert month == "2024-02-01"


def test_period_date_month_to_str_transformer():
	month = MT.period_start_str(date(2024, 10, 10))
	assert month == "2024-10-01"


def test_period_str_to_datetime_month_2024_03_10():
	period = MT.period_start_datetime("2024-03-10")
	assert period.year == 2024
	assert period.month == 3
	assert period.day == 1


def test_is_valid_month_str():
	assert MT.validate("2024-01")


def test_is_valid_d_m_y_str():
	assert MT.validate("01-01-2024")


def test_is_valid_month_date():
	assert MT.validate(date(2024, 1, 1))


def test_is_valid_month_datetime():
	assert MT.validate(datetime(2024, 1, 1))


def test_is_invalid_month_str_invalid():
	assert not MT.validate("202-01-01")


def test_str_to_date_2024_01():
	year = MT._str_to_date("2024-01")
	assert year == datetime(2024, 1, 1)


def test_month_str_to_date_1_1_2024():
	year = MT._str_to_date("1-1-2024")
	assert year == datetime(2024, 1, 1)


def test_month_str_to_date_2024_1_1():
	year = MT._str_to_date("2024-01-01")
	assert year == datetime(2024, 1, 1)


def test_date_to_period_type_str_2024_01():
	year = MT.date_to_period_type_str("2024-01")
	assert year == "2024M01"


def test_date_to_period_type_str_2024_01_01():
	year = MT.date_to_period_type_str(datetime(2024, 1, 1))
	assert year == "2024M01"


def test_date_to_period_type_str_10_04_2024():
	year = MT.date_to_period_type_str("10-04-2024")
	assert year == "2024M04"
