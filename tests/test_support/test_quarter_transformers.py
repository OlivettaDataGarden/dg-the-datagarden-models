from datetime import datetime

from datagarden_models.support.date_handler.quarter_normalizer import (
	QuarterPeriodTransformer,
)

QT = QuarterPeriodTransformer()


def test_period_q1_to_date_transformer():
	first_quarter = QT.period_start_datetime("2024-Q1")
	assert first_quarter.year == 2024
	assert first_quarter.month == 1
	assert first_quarter.day == 1


def test_period_q1_to_str_transformer():
	first_quarter = QT.period_start_str("2024-Q1")
	assert first_quarter == "2024-01-01"


def test_period_q1_to_period_type_str_transformer():
	first_quarter = QT.date_to_period_type_str("2024-Q1")
	assert first_quarter == "2024Q1"


def test_date_to_period_type_str_transformer():
	first_quarter = QT.date_to_period_type_str(datetime(2024, 5, 10, 0, 0, 0))
	assert first_quarter == "2024Q2"


def test_date_str_to_period_type_str_transformer():
	first_quarter = QT.date_to_period_type_str("2024-09-10")
	assert first_quarter == "2024Q3"


def test_period_datetime_to_date_transformer():
	first_quarter = QT.period_start_datetime(datetime(2024, 2, 2, 12, 0, 0))
	assert first_quarter.year == 2024
	assert first_quarter.month == 1
	assert first_quarter.day == 1


def test_format_qrt_str_Q1_2024():
	formatted_period = QT._format_quarter_str("Q1-2024")
	assert formatted_period == "2024-1"


def test_format_qrt_str_1_2024():
	formatted_period = QT._format_quarter_str("1-2024")
	assert formatted_period == "2024-1"


def test_format_qrt_str_2024_1():
	formatted_period = QT._format_quarter_str("2024-1")
	assert formatted_period == "2024-1"


def test_format_qrt_str_2024Q1():
	formatted_period = QT._format_quarter_str("2024Q1")
	assert formatted_period == "2024-1"


def test_format_qrt_str_2024_Q1():
	formatted_period = QT._format_quarter_str("2024-Q1")
	assert formatted_period == "2024-1"


def test_format_qrt_str_2024_Q2():
	formatted_period = QT._format_quarter_str("2024Q2")
	assert formatted_period == "2024-2"


def test_format_qrt_str_2024_with_space():
	formatted_period = QT._format_quarter_str(" 2024Q3 ")
	assert formatted_period == "2024-3"


def test_format_qrt_str_2024_Q4():
	formatted_period = QT._format_quarter_str("2024Q4")
	assert formatted_period == "2024-4"


def test_try_date_str_to_datetime_2024_01_01():
	formatted_period = QT._try_date_str_to_datetime("2024-01-01")
	assert formatted_period == datetime(2024, 1, 1, 0, 0, 0)


def test_try_date_str_to_datetime_10_01_2024():
	formatted_period = QT._try_date_str_to_datetime("10-01-2024")
	assert formatted_period == datetime(2024, 1, 10, 0, 0, 0)


def test_try_date_str_to_datetime_2024_01_01_with_space():
	formatted_period = QT._try_date_str_to_datetime(" 2024-01-01 ")
	assert formatted_period == datetime(2024, 1, 1, 0, 0, 0)


def test_try_date_str_to_datetime_with_random_str():
	formatted_period = QT._try_date_str_to_datetime(" 01-01 ")
	assert formatted_period is None


def test_str_to_date_2024_Q1():
	formatted_period = QT._str_to_date("2024-Q1")
	assert formatted_period == datetime(2024, 1, 1, 0, 0, 0)


def test_str_to_date_2024_Q2():
	formatted_period = QT._str_to_date("2024-04-01")
	assert formatted_period == datetime(2024, 4, 1, 0, 0, 0)


def test_str_to_date_2024_Q3():
	formatted_period = QT._str_to_date("01-09-2024")
	assert formatted_period == datetime(2024, 7, 1, 0, 0, 0)


def test_str_to_date_2024_Q3_str():
	formatted_period = QT._str_to_date("2024-Q3")
	assert formatted_period == datetime(2024, 7, 1, 0, 0, 0)
