from typing import Literal

PeriodType = Literal["year", "quarter", "month", "week", "day"]


class PeriodTypeNormalizer:
    def normalize(self, period_type: str) -> PeriodType:
        lower_period_type = period_type.lower()
        match lower_period_type:
            case "year" | "y" | "yearly":
                return "year"
            case "quarter" | "q" | "quarterly":
                return "quarter"
            case "month" | "m" | "monthly":
                return "month"
            case "week" | "w" | "weekly":
                return "week"
            case "day" | "d" | "daily":
                return "day"
            case _:
                raise ValueError(f"Invalid period type: {period_type}")
