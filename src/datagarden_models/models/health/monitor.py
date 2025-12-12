from pydantic import Field

from datagarden_models.models.base import DataGardenSubModel
from datagarden_models.models.demographics.base_demographics import AgeStatistics


class HealthMonitorKeys:
	BY_AGE_GROUP = "by_age_group"


class HealthMonitorLegends:
	BY_AGE_GROUP = "Health monitor data by age group"


L = HealthMonitorLegends


class HealthMonitor(DataGardenSubModel):
	by_age_group: AgeStatistics = Field(
		default_factory=AgeStatistics, description=L.BY_AGE_GROUP
	)
