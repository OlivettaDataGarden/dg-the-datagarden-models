from typing import Optional

from pydantic import Field

from datagarden_models.models.base import DataGardenSubModel
from datagarden_models.models.demographics.base_demographics import Age, AgeGroup


class FertilityV1Legends:
	TOTAL_BIRTHS = "Total number of births in the population."
	AGE_UNKNOWN = "Number of births with unknown age of the mother."
	BIRTHS_BY_AGE = "Number of births categorized by age of the mother."
	AVERAGE_AGE_MOTHER = "Average age of mothers at childbirth."
	BIRTHS_BY_AGE_GROUP = "Number of births categorized by age group of the mother."
	MEDIAN_AGE_MOTHER = "Median age of mothers at childbirth."
	FERTILITY_RATE = "Overall fertility rate per woman."
	FERTILITY_RATE_BY_AGE = "Fertility rates categorized by age of the mother."
	FERTILITY_RATE_BY_AGE_GROUP = (
		"Fertility rates categorized by age group of the mother."
	)
	BIRTH_RATE = "Crude birth rate in number of births per 1000 people."
	BIRTHS_SURVIVING_FIRST_YEAR = "Number of births surviving the first year of life."
	NET_REPRODUCTION_RATE = "surviving daughters per woman."
	SEX_RATIO_AT_BIRTH = "Sex ratio at birth (boys per 100 girls)."


L = FertilityV1Legends


class Fertility(DataGardenSubModel):
	total_births: Optional[float] = Field(default=None, description=L.TOTAL_BIRTHS)
	age_unknown: int | None = Field(default=None, description=L.AGE_UNKNOWN)
	births_by_age: Age | None = Field(default=None, description=L.BIRTHS_BY_AGE)
	births_by_age_group: AgeGroup | None = Field(
		default=None, description=L.BIRTHS_BY_AGE_GROUP
	)
	average_age_mother: float | None = Field(
		default=None, description=L.AVERAGE_AGE_MOTHER
	)
	median_age_mother: float | None = Field(
		default=None, description=L.MEDIAN_AGE_MOTHER
	)
	fertility_rate: float | None = Field(default=None, description=L.FERTILITY_RATE)
	fertility_rate_by_age: Age | None = Field(
		default=None, description=L.FERTILITY_RATE_BY_AGE
	)
	fertility_rate_by_age_group: AgeGroup | None = Field(
		default=None, description=L.FERTILITY_RATE_BY_AGE_GROUP
	)
	birth_rate: float | None = Field(default=None, description=L.BIRTH_RATE)
	births_surviving_first_year: float | None = Field(
		default=None, description=L.BIRTHS_SURVIVING_FIRST_YEAR
	)
	net_reproduction_rate: float | None = Field(
		default=None, description=L.NET_REPRODUCTION_RATE
	)
	sex_ratio_at_birth: float | None = Field(
		default=None, description=L.SEX_RATIO_AT_BIRTH
	)


class FertilityV1Keys:
	TOTAL_BIRTHS = "total_births"
	AGE_UNKNOWN = "age_unknown"
	BIRTHS_BY_AGE = "births_by_age"
	BIRTHS_BY_AGE_GROUP = "births_by_age_group"
	AVERAGE_AGE_MOTHER = "average_age_mother"
	MEDIAN_AGE_MOTHER = "median_age_mother"
	FERTILITY_RATE = "fertility_rate"
	FERTILITY_RATE_BY_AGE = "fertility_rate_by_age"
	FERTILITY_RATE_BY_AGE_GROUP = "fertility_rate_by_age_group"
	BIRTH_RATE = "birth_rate"
	BIRTHS_SURVIVING_FIRST_YEAR = "births_surviving_first_year"
	NET_REPRODUCTION_RATE = "net_reproduction_rate"
	SEX_RATIO_AT_BIRTH = "sex_ratio_at_birth"
