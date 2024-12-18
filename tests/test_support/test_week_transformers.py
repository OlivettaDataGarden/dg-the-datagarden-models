import pytest

from datagarden_models.support.date_handler.week_normalizer import WeekPeriodTransformer

WT = WeekPeriodTransformer()


def test_period_w1_to_date_transformer():
    first_week = WT.period_start_datetime("2024-W1")
    assert first_week.year == 2024
    assert first_week.month == 1
    assert first_week.day == 1


def test_period_w1_to_period_type_str():
    week = WT.date_to_period_type_str("2024-W1")
    assert week == "2024W01"


def test_period_10_10_to_period_type_str():
    week = WT.date_to_period_type_str("2024-10-10")
    assert week == "2024W41"


def test_period_w2_to_date_transformer():
    first_week = WT.period_start_datetime("2024-W2")
    assert first_week.year == 2024
    assert first_week.month == 1
    assert first_week.day == 8


def test_period_w52_to_date_transformer():
    first_week = WT.period_start_datetime("2024-W52")
    assert first_week.year == 2024
    assert first_week.month == 12
    assert first_week.day == 23


def test_period_w53_to_date_transformer():
    with pytest.raises(ValueError) as error:
        WT.period_start_datetime("2024-W53")
    assert str(error.value) == "Could not create Week date from 2024-W53"


def test_period_date_str_to_date_transformer():
    first_week = WT.period_start_datetime("2024-01-05")
    assert first_week.year == 2024
    assert first_week.month == 1
    assert first_week.day == 1


def test_period_date_str_0110_to_date_transformer():
    first_week = WT.period_start_datetime("2024-01-10")
    assert first_week.year == 2024
    assert first_week.month == 1
    assert first_week.day == 8


def test_format_week_str_2024_W2():
    week = WT._format_week_str("2024-W2")
    assert week == "2024-02"


def test_format_week_str_2024_W02():
    week = WT._format_week_str("2024-W02")
    assert week == "2024-02"


def test_format_week_str_2024_W12():
    week = WT._format_week_str("2024-W12")
    assert week == "2024-12"


def test_format_week_str_01_2024():
    week = WT._format_week_str("01-2024")
    assert week == "2024-01"


def test_format_week_str_1_2024():
    week = WT._format_week_str("1-2024")
    assert week == "2024-01"


def test_format_week_str_w01_2024():
    week = WT._format_week_str("W01-2024")
    assert week == "2024-01"


def test_format_week_str_W1_2024():
    week = WT._format_week_str("W1-2024")
    assert week == "2024-01"


def test_format_week_str_2024_2():
    week = WT._format_week_str("2024-W2")
    assert week == "2024-02"


def test_format_week_str_2024_02():
    week = WT._format_week_str("2024-W02")
    assert week == "2024-02"


def test_format_week_str_2024W2():
    week = WT._format_week_str("2024-W2")
    assert week == "2024-02"


def test_format_week_str_2024W02():
    week = WT._format_week_str("2024-W02")
    assert week == "2024-02"
