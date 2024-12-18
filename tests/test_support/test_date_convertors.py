from datetime import date, datetime, timedelta, timezone

import pytest

from datagarden_models.support.date_handler.helper import utc_datetime


def test_date_input():
    # Test with a simple date object
    input_date = date(2024, 3, 14)
    result = utc_datetime(input_date)

    assert isinstance(result, datetime)
    assert result.year == 2024
    assert result.month == 3
    assert result.day == 14
    assert result.hour == 0
    assert result.minute == 0
    assert result.second == 0
    assert result.tzinfo == timezone.utc


def test_datetime_input():
    # Test with naive datetime
    input_dt = datetime(2024, 3, 14, 15, 30)
    result = utc_datetime(input_dt)

    assert result.tzinfo == timezone.utc
    assert result.hour == 15
    assert result.minute == 30


def test_aware_datetime_input():
    # Test with timezone-aware datetime (non-UTC)
    est = timezone(offset=timedelta(hours=-5))
    input_dt = datetime(2024, 3, 14, 15, 30, tzinfo=est)
    print(input_dt)
    result = utc_datetime(input_dt)

    assert result.tzinfo == timezone.utc
    assert result.hour == 20  # 15 + 5 hours
    assert result.minute == 30


def test_invalid_string_format():
    # Test with invalid date string format
    with pytest.raises(TypeError, match="Invalid date format: 14-03-2024"):
        utc_datetime("14-03-2024")


def test_invalid_input_type():
    # Test with invalid input type
    with pytest.raises(TypeError):
        utc_datetime(123)
