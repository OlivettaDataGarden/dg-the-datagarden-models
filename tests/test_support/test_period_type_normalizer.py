import pytest

from datagarden_models.support.date_handler.period_type_normalizer import (
	PeriodTypeNormalizer,
)


class TestPeriodTypeNormalizer:
	@pytest.fixture
	def normalizer(self):
		return PeriodTypeNormalizer

	@pytest.mark.parametrize(
		"input_period,expected",
		[
			("year", "year"),
			("y", "year"),
			("yearly", "year"),
			("YEAR", "year"),
			("quarter", "quarter"),
			("q", "quarter"),
			("quarterly", "quarter"),
			("QUARTER", "quarter"),
			("month", "month"),
			("m", "month"),
			("monthly", "month"),
			("MONTH", "month"),
			("week", "week"),
			("w", "week"),
			("weekly", "week"),
			("WEEK", "week"),
			("day", "day"),
			("d", "day"),
			("daily", "day"),
			("DAY", "day"),
		],
	)
	def test_normalize_valid_periods(self, normalizer, input_period, expected):
		assert normalizer.normalize(input_period) == expected

	@pytest.mark.parametrize(
		"invalid_input",
		[
			"invalid",
			"yearly123",
			"",
			"minutes",
			"hours",
		],
	)
	def test_normalize_invalid_periods(self, normalizer, invalid_input):
		with pytest.raises(ValueError) as exc_info:
			normalizer.normalize(invalid_input)
		assert str(exc_info.value) == f"Invalid period type: {invalid_input}"
