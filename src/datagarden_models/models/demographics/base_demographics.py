import re
from pydantic import Field, RootModel, field_validator

from datagarden_models.models.base import DataGardenSubModel


class DemographicsBaseKeys:
	MALE = "male"
	FEMALE = "female"


class DemographicsBaseLegends:
	AGE_GENDER_MALE = "Number of males. In number of individuals per single age."
	AGE_GENDER_FEMALE = "Number of females. In number of individuals per single age."
	AGE_GENDER_TOTAL = (
		"Total number of individuals. In number of individuals per single age."
	)
	AGE_GENDER_GROUP_MALE = "Number of males. In number of individuals per age group."
	AGE_GENDER_GROUP_FEMALE = (
		"Number of females. In number of individuals per age group."
	)
	AGE_GENDER_GROUP_TOTAL = (
		"Total number of individuals. In number of individuals per age group."
	)


L = DemographicsBaseLegends


class Age(RootModel[dict[str, int]]):
	root: dict[str, int]

	@field_validator("root", mode="after")
	@classmethod
	def validate_dict(cls, v: dict[str, int]) -> dict[str, int]:
		"""Validate keys and values."""
		if not v:
			return v
		# Pattern for AGE-0 through AGE-99 or AGE-100+
		age_pattern = re.compile(r"^AGE-(?:[0-9]|[1-9][0-9]|100\+)$")

		for key, value in v.items():
			# Validate key format
			if not age_pattern.match(key):
				raise ValueError(
					f"Invalid key '{key}'. Keys must be in format "
					f"'AGE-0' through 'AGE-99' or 'AGE-100+'."
				)

			# Validate value
			if not isinstance(value, int):
				raise ValueError(
					f"Value for key '{key}' must be an integer, "
					f"got {type(value).__name__}"
				)

		return v


class AgeGender(DataGardenSubModel):
	male: Age | None = Field(default=None, description=L.AGE_GENDER_MALE)
	female: Age | None = Field(default=None, description=L.AGE_GENDER_FEMALE)
	total: Age | None = Field(default=None, description=L.AGE_GENDER_TOTAL)


class AgeGroup(RootModel[dict[str, int]]):
	root: dict[str, int]

	@field_validator("root", mode="after")
	@classmethod
	def validate_age_group_dict(cls, v: dict[str, int]) -> dict[str, int]:
		"""
		Validate that dict keys are in format AGE-{start}-TO-{end} where start is 0-99
		and end is 2-100+ and values are integers.
		"""
		if not v:
			return v

		# Pattern for AGE-{0-99}-TO-{2-100+}
		# First number: 0-99 (single digit 0-9 or two digits 10-99)
		# Second number: 2-100+ (2-9, 10-99, or 100+)
		age_pattern = re.compile(r"^AGE-(\d{1,2})-TO-(\d{1,2}|100\+)$")

		for key, value in v.items():
			# Validate key format
			match = age_pattern.match(key)
			if not match:
				raise ValueError(
					f"Invalid key '{key}'. Keys must be in format "
					f"'AGE-{{0-99}}-TO-{{2-100+}}'"
				)

			# Extract and validate start and end values
			start_str, end_str = match.groups()
			start = int(start_str)

			# Validate start is 0-99
			if start < 0 or start > 99:
				raise ValueError(
					f"Invalid start age '{start}' in key '{key}'. "
					f"Start must be between 0 and 99."
				)

			# Validate end
			if end_str == "100+":
				end = 100  # Treat 100+ as 100 for comparison
			else:
				end = int(end_str)
				# Validate end is 2-100
				if end < 2 or end > 100:
					raise ValueError(
						f"Invalid end age '{end_str}' in key '{key}'. "
						"End must be between 2 and 100+."
					)

			# Validate that end >= start (logical range validation)
			if end < start:
				raise ValueError(
					f"Invalid range in key '{key}'. End age ({end_str}) "
					f"must be >= start age ({start})."
				)

			# Validate value is integer
			if not isinstance(value, int):
				raise ValueError(
					f"Value for key '{key}' must be an integer, "
					f"got {type(value).__name__}"
				)

		return v


class AgeGenderGroup(DataGardenSubModel):
	male: AgeGroup = Field(default=None, description=L.AGE_GENDER_GROUP_MALE)
	female: AgeGroup = Field(default=None, description=L.AGE_GENDER_GROUP_FEMALE)
	total: AgeGroup = Field(default=None, description=L.AGE_GENDER_GROUP_TOTAL)
