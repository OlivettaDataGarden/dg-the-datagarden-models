from .day_normalizer import DayPeriodTransformer
from .month_normalizer import MonthPeriodTransformer
from .quarter_normalizer import QuarterPeriodTransformer
from .week_normalizer import WeekPeriodTransformer
from .year_normalizer import YearPeriodTransformer

PERIOD_TYPES = {
    "year": "year",
    "quarter": "quarter",
    "month": "month",
    "week": "week",
    "day": "day",
    "y": "year",
    "q": "quarter",
    "m": "month",
    "w": "week",
    "d": "day",
}


class GetPeriodTypeTransformer:
    """
    Get the period transformer for a given period type.

    Period types are:
        - year
        - quarter
        - month
        - week
        - day
    and can be abbreviated to:
        - y, q, m, w, d

    period types are case insensitive.

    Methods:
        - get_transformer(period_type: str) -> PeriodTransformer
        returns the transformer for the given period type.
    """

    @staticmethod
    def get_transformer(period_type):
        period_type = PERIOD_TYPES.get(period_type.lower())
        match period_type:
            case "year":
                return YearPeriodTransformer()
            case "quarter":
                return QuarterPeriodTransformer()
            case "month":
                return MonthPeriodTransformer()
            case "week":
                return WeekPeriodTransformer()
            case "day":
                return DayPeriodTransformer()
            case _:
                raise ValueError(f"Unsupported period type: {period_type}")
