from typing import Optional

from pydantic import Field

from datagarden_models.models.base import DataGardenSubModel


class VaccinationCoverageKeys:
    GRADE_PER_TYPE = "grade_per_type"


class VaccinationCoverageLegends:
    GRADE_PER_TYPE = "Grade of vaccination per WHO type of vaccine."


L = VaccinationCoverageLegends


class VaccinationCoverage(DataGardenSubModel):
    grade_per_type: Optional[dict[str, float]] = Field(default=None, description=L.GRADE_PER_TYPE)
