from typing import Optional

from pydantic import Field

from datagarden_models.models.base import DataGardenSubModel
from datagarden_models.models.demographics.base_demographics import (
	AgeGender,
	AgeGenderGroup,
)


class LifeExpectancyAtBirthLegends:
	MALE = (
		"Male Life expectancy at birth for birthyear of record period. "
		"In years expected to live when born."
	)
	FEMALE = (
		"Female Life expectancy at birth for birthyear of record period. "
		"In years expected to live when born."
	)
	TOTAL = (
		"Total Life expectancy at birth for birthyear of record period. "
		"In years expected to live when born."
	)


LEB = LifeExpectancyAtBirthLegends


class LifeExpectancyAtBirth(DataGardenSubModel):
	male: Optional[float] = Field(default=None, description=LEB.MALE)
	female: Optional[float] = Field(default=None, description=LEB.FEMALE)
	total: Optional[float] = Field(default=None, description=LEB.TOTAL)


class LifeExpectancyV1Keys:
	LIFE_EXPECTANCY_AT_BIRTH = "life_expectancy_at_birth"
	REMAINING_LIFE_EXPECTANCY_BY_AGE = "remaining_life_expectancy_by_age"
	REMAINING_LIFE_EXPECTANCY_BY_AGE_GROUP = "remaining_life_expectancy_by_age_group"


class LifeExpectancyV1Legends:
	LIFE_EXPECTANCY_AT_BIRTH = (
		"Life expectancy per age or age group at birth. "
		"In years expected to live when born"
	)
	REMAINING_LIFE_EXPECTANCY_BY_AGE = (
		"Life expectancy per age and grender. "
		"In years expected to live as of current age"
	)
	REMAINING_LIFE_EXPECTANCY_BY_AGE_GROUP = (
		"Life expectancy per age group and grender. "
		"In years expected to live as of current age by age group"
	)


L = LifeExpectancyV1Legends


class LifeExpectancy(DataGardenSubModel):
	life_expectancy_at_birth: LifeExpectancyAtBirth = Field(
		default_factory=LifeExpectancyAtBirth, description=L.LIFE_EXPECTANCY_AT_BIRTH
	)

	remaining_life_expectancy_by_age: AgeGender = Field(
		default_factory=AgeGender,
		description=L.REMAINING_LIFE_EXPECTANCY_BY_AGE,
	)
	remaining_life_expectancy_by_age_group: AgeGenderGroup = Field(
		default_factory=AgeGenderGroup,
		description=L.REMAINING_LIFE_EXPECTANCY_BY_AGE_GROUP,
	)
