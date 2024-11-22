from pydantic import BaseModel, Field


class DataGardenModelLegends:
    DATA_IS_PROJECTION = "data is identified by the source as a projection."
    # DATA_IS_DERIVED = \
    # "data is derived by the datagarden from different sources and possibly machine learning models"


class MetadataModel(BaseModel):
    data_is_projection: bool = Field(default=False, description=DataGardenModelLegends.DATA_IS_PROJECTION)
    # data_is_derived: bool = Field(default=False, description=DataGardenModelLegends.DATA_IS_DERIVED)
