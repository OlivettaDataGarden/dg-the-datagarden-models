from pydantic import Field

from datagarden_models.models.base import DataGardenSubModel
from datagarden_models.models.demographics.base_demographics import AgeGenderStatistics


class Isced2011EducationLevelKeys:
	ISCED_2011_5TO8_PERCENTAGE = "isced_2011_5to8_percentage"
	ISCED_2011_5_COUNT = "isced_2011_5_count"
	ISCED_2011_6_COUNT = "isced_2011_6_count"
	ISCED_2011_7_COUNT = "isced_2011_7_count"
	ISCED_2011_8_COUNT = "isced_2011_8_count"


class Isced2011EducationLevelLegends:
	ISCED_2011_5TO8_PERCENTAGE = (
		"Percentage of age gender of age gender group with Level 5 up to "
		"and including level 8 of the "
		"ISCED 2011 International Standard Classification of Education."
	)
	ISCED_2011_5_COUNT = (
		"Count for age gender of age gender group with Level 5 "
		"(Short cycle tertiary) education of the "
		"ISCED 2011 International Standard Classification of Education."
	)
	ISCED_2011_6_COUNT = (
		"Count for age gender of age gender group with Level 6 "
		"(Bachelor's or equivalent level) education of the "
		"ISCED 2011 International Standard Classification of Education."
	)
	ISCED_2011_7_COUNT = (
		"Count for age gender of age gender group with Level 7 "
		"(Master's or equivalent level) education level of the "
		"ISCED 2011 International Standard Classification of Education."
	)
	ISCED_2011_8_COUNT = (
		"Count for age gender of age gender group with Level 8 "
		"(Doctoral or equivalent level) education level of the "
		"ISCED 2011 International Standard Classification of Education."
	)


L2 = Isced2011EducationLevelLegends


class Isced2011EducationLevel(DataGardenSubModel):
	isced_2011_5to8_percentage: AgeGenderStatistics = Field(
		default_factory=AgeGenderStatistics, description=L2.ISCED_2011_5TO8_PERCENTAGE
	)
	isced_2011_5_count: AgeGenderStatistics = Field(
		default_factory=AgeGenderStatistics, description=L2.ISCED_2011_5_COUNT
	)
	isced_2011_6_count: AgeGenderStatistics = Field(
		default_factory=AgeGenderStatistics, description=L2.ISCED_2011_6_COUNT
	)
	isced_2011_7_count: AgeGenderStatistics = Field(
		default_factory=AgeGenderStatistics, description=L2.ISCED_2011_7_COUNT
	)
	isced_2011_8_count: AgeGenderStatistics = Field(
		default_factory=AgeGenderStatistics, description=L2.ISCED_2011_8_COUNT
	)


class EducationV1Legends:
	ISCED_2011_BY_AGE_GENDER = (
		"Percentage or count of and age gender group with a given education level. "
		"see https://uis.unesco.org/sites/default/files/documents/international-standard-classification-of-education-isced-2011-en.pdf"
		" for detailed explenation of the education levels."
	)


L3 = EducationV1Legends


class Education(DataGardenSubModel):
	isced_2011_by_age_gender: Isced2011EducationLevel = Field(
		default_factory=Isced2011EducationLevel, description=L3.ISCED_2011_BY_AGE_GENDER
	)


class EducationV1Keys(
	Isced2011EducationLevelKeys,
):
	ISCED_2011_BY_AGE_GENDER = "isced_2011_by_age_gender"
