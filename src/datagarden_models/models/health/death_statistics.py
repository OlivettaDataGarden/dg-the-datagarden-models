from pydantic import Field

from datagarden_models.models.base import DataGardenSubModel
from datagarden_models.models.demographics.base_demographics import AgeGenderStatistics

from .base_health import ByGender


class DeathStatisticsKeys:
	DEATH_RATE_BY_IDC10 = "death_rate_idc10"


class DeathStatisticsLegends:
	DEATH_RATE_BY_IDC10 = (
		"Death rate by IDC10 categorization, see https://icd.who.int/browse10/2010/en"
		" (for detailed description of IDC10 categories (keys in this dataset))"
		" Death rate in deaths per 100.000 population."
	)
	DEATH_RATE_BY_GENDER = "Death rate by gender. In deaths per 100.000 population."
	DEATH_RATE_BY_AGE_GENDER = (
		"Death rate by age or age group and gender. In deaths per 100.000 population."
	)


L = DeathStatisticsLegends


class DeathRateIDC10(DataGardenSubModel):
	by_gender: ByGender = Field(
		default_factory=ByGender, description=L.DEATH_RATE_BY_GENDER
	)
	by_age_gender: AgeGenderStatistics = Field(
		default_factory=AgeGenderStatistics, description=L.DEATH_RATE_BY_AGE_GENDER
	)


class DeathStatistics(DataGardenSubModel):
	death_rate_idc10: ByGender = Field(
		default_factory=ByGender, description=L.DEATH_RATE_BY_IDC10
	)
