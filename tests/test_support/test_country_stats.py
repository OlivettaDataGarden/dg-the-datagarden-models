from copy import deepcopy

import pytest

from datagarden_models import CountryStats
from datagarden_models.support.country_stats import RegionData

from .data import CITY_STATS_DATA, COUNTRY_STATS_DATA, REGION_STATS_DATA


@pytest.fixture
def country_stats():
    return CountryStats(**COUNTRY_STATS_DATA)


@pytest.fixture
def city_stats():
    return RegionData(**CITY_STATS_DATA)


@pytest.fixture
def region_stats():
    return RegionData(**REGION_STATS_DATA)


def test_country_stats(country_stats):
    assert country_stats


def test_region_types_method(country_stats):
    assert "country" in country_stats.region_types
    assert "region" in country_stats.region_types
    assert "city" in country_stats.region_types


def test_getattr_valid_regions(country_stats):
    # Test accessing valid region types
    assert isinstance(country_stats.country, RegionData)
    assert isinstance(country_stats.region, RegionData)
    assert isinstance(country_stats.city, RegionData)


def test_getattr_invalid_region(country_stats):
    with pytest.raises(AttributeError) as exc_info:
        assert country_stats.invalid_region
    assert "'CountryStats' object has no attribute 'invalid_region'" in str(exc_info.value)


def test_city_stats(city_stats):
    assert city_stats


def test_city_stats_regional_data_models_stored_in_lowercase():
    test_data = deepcopy(CITY_STATS_DATA)
    health_data = test_data["regional_data_stats"]["Health"]
    test_data["regional_data_stats"]["UPPERCASE"] = deepcopy(health_data)
    city_stats = RegionData(**test_data)

    assert "UPPERCASE" not in city_stats.regional_data_models
    assert "uppercase" in city_stats.regional_data_models


def test_city_stats_region_type(city_stats):
    assert city_stats.region_type == "city"


def test_city_stats_region_data_models(city_stats):
    assert city_stats.regional_data_models == ["health"]


def test_province_stats_region_data_models(country_stats):
    assert sorted(country_stats.province.regional_data_models) == sorted(
        [
            "demographics",
            "economics",
            "health",
            "weather",
        ]
    )


def test_city_stats_health_attr(city_stats):
    assert city_stats.health


def test_region_stats_has_sources(region_stats):
    assert region_stats.health.sources
