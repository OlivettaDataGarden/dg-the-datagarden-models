from typing import Optional

from pydantic import Field

from datagarden_models import DataGardenModel, DataGardenSubModel


class EconomicsData(DataGardenSubModel):
    unit: int = Field(default=1)
    currency: str = Field(default="EUR")
    value: Optional[float] = Field(default=None)

    class Meta(DataGardenSubModel.Meta):
        exclude_fields_in_has_values_check = ["unit", "reference_year", "currency"]


class MyModel(DataGardenSubModel):
    total: Optional[float] = Field(default=None)


class MySubModel(DataGardenSubModel):
    metric: Optional[EconomicsData] = Field(default_factory=EconomicsData)
    test: Optional[float] = Field(default=None)


class MySecondModel(DataGardenModel):
    my_sub_model: MySubModel = Field(default_factory=MySubModel)
    my_model: MyModel = Field(default_factory=MyModel)
    total: Optional[float] = Field(default=None)


def test_model_dump():
    model = MyModel(total=1)
    assert model.model_dump().get("total", None) == 1


def test_empty_model_dump():
    model = MyModel()
    assert "total" not in list(model.data_dump().keys())


def test_empty_model_has_no_values():
    model = MyModel()
    assert not model.has_values()


def test_non_empty_model_has_values():
    model = MyModel(total=1)
    assert model.has_values()


def test_nested_empty_sub_model_has_no_values():
    model = MySecondModel()
    assert not model.has_values()


def test_nested_non_empty_sub_model_has_values():
    model = MySecondModel(my_sub_model=MySubModel(metric=EconomicsData(value=1)))
    assert model.has_values()


def test_my_second_data_dump_empty():
    """
    This test is to check if the data_dump method is working correctly and does not include empty sub models
    """
    model = MySecondModel()
    assert "my_model" not in list(model.data_dump().keys())
    assert "my_sub_model" not in list(model.data_dump().keys())


def test_my_second_model_dump_empty():
    """
    This test is to check if the model_dump method is working correctly and includes empty sub models
    """
    model = MySecondModel()
    assert "my_model" in list(model.model_dump().keys())
    assert "my_sub_model" in list(model.model_dump().keys())


def test_my_second_data_dump_only_has_total():
    """
    This test is to check if the data_dump method is working correctly and does not include empty sub models
    """
    model = MySecondModel(total=1)
    assert "my_model" not in list(model.data_dump().keys())
    assert "my_sub_model" not in list(model.data_dump().keys())
    assert "total" in list(model.data_dump().keys())
    assert model.data_dump()["total"] == 1


def test_my_second_data_dump_has_economics_datal():
    """
    This test is to check if the data_dump method is working correctly and does not include empty sub models
    """
    model = MySecondModel(my_sub_model=MySubModel(metric=EconomicsData(value=1)))
    print(model.Meta.fields_to_include_in_data_dump)
    assert "my_model" not in list(model.data_dump().keys())
    assert "my_sub_model" in list(model.data_dump().keys())
    assert model.data_dump()["my_sub_model"]["metric"]["value"] == 1
    assert "total" not in list(model.data_dump().keys())
    data_dump = model.data_dump()
    data_dump.pop("datagarden_model_version")
    data_dump.pop("metadata")
    assert data_dump == {"my_sub_model": {"metric": {"currency": "EUR", "unit": 1, "value": 1.0}}}


def test_my_second_data_dump_has_no_economics_data():
    """
    This test is to check if the data_dump method is working correctly and does not include empty sub models
    """
    model = MySecondModel(my_sub_model=MySubModel(metric=EconomicsData()), total=1)
    assert "my_model" not in list(model.data_dump().keys())
    assert "my_sub_model" not in list(model.data_dump().keys())
    assert "total" in list(model.data_dump().keys())
    data_dump = model.data_dump()
    data_dump.pop("datagarden_model_version")
    data_dump.pop("metadata")
    assert data_dump == {"total": 1.0}


def test_my_second_data_dump_has_test_datal():
    """
    This test is to check if the data_dump method is working correctly and does not include empty sub models
    """
    model = MySecondModel(my_sub_model=MySubModel(test=1))
    assert "my_model" not in list(model.data_dump().keys())
    assert "my_sub_model" in list(model.data_dump().keys())
    assert model.data_dump()["my_sub_model"]["test"] == 1
    assert "total" not in list(model.data_dump().keys())
    data_dump = model.data_dump()
    data_dump.pop("datagarden_model_version")
    data_dump.pop("metadata")
    assert data_dump == {"my_sub_model": {"test": 1.0}}
