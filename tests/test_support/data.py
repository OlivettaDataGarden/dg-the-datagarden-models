# ruff: noqa: E501

COUNTRY_STATS_DATA = {
	"0": {
		"count": 1,
		"region_type": "country",
		"access_level": "A",
		"region_level": 0,
		"with_geojson": 1,
		"regional_data_stats": {
			"Health": {
				"count": 35,
				"sources": {
					"UNICEF": (
						"5e5db495c6f7bbdf5c47a3ae11515386d5c8aa465036959cff1eaf4377901159"
					),
					"Eurostat": (
						"74d562e420b0137309bd9308af9a531f538b673063399cf617c4ae7edd3f3e41"
					),
				},
				"to_period": "2023-01-01 00:00:00+00:00",
				"from_period": "2000-01-01 00:00:00+00:00",
				"period_type": ["Y"],
			},
			"Economics": {
				"count": 103,
				"sources": {
					"UNCTAD": "e4f89bd08ff66a258ee29884634f0535327e82f93d0e07524c2c2737576ba603",
					"Eurostat": "74d562e420b0137309bd9308af9a531f538b673063399cf617c4ae7edd3f3e41",
				},
				"to_period": "2023-01-01 00:00:00+00:00",
				"from_period": "1975-01-01 00:00:00+00:00",
				"period_type": ["Y"],
			},
			"Demographics": {
				"count": 185,
				"sources": {
					"Eurostat": "74d562e420b0137309bd9308af9a531f538b673063399cf617c4ae7edd3f3e41",
					"United Nations": "03ecc1f78b968ecd6cd5156b1e36fe6d196a1c4dad750b19082fcef77443cb4e",
				},
				"to_period": "2100-01-01 00:00:00+00:00",
				"from_period": "1950-01-01 00:00:00+00:00",
				"period_type": ["Y"],
			},
		},
	},
	"1": {
		"count": 4,
		"region_type": "region",
		"access_level": "B",
		"region_level": 1,
		"with_geojson": 4,
		"regional_data_stats": {
			"Health": {
				"count": 44,
				"sources": {
					"Eurostat": "74d562e420b0137309bd9308af9a531f538b673063399cf617c4ae7edd3f3e41"
				},
				"to_period": "2021-01-01 00:00:00+00:00",
				"from_period": "2011-01-01 00:00:00+00:00",
				"period_type": ["Y"],
			},
			"Weather": {
				"count": 1663,
				"sources": {
					"Datagarden regional weather average for period": "651fe7527ba49b26d04ba0efb60d61c20623bd0ede885865798c4e31adc26002",
					"Datagarden regional average weather observations": "381446f192c65fb2fdef13468d81a88df029af764a9d8cc69d57d9ccf24ff58f",
				},
				"to_period": "2024-12-15 00:00:00+00:00",
				"from_period": "2024-01-01 00:00:00+00:00",
				"period_type": ["D", "M", "Q", "W"],
			},
			"Economics": {
				"count": 112,
				"sources": {
					"Eurostat": "74d562e420b0137309bd9308af9a531f538b673063399cf617c4ae7edd3f3e41"
				},
				"to_period": "2022-01-01 00:00:00+00:00",
				"from_period": "1995-01-01 00:00:00+00:00",
				"period_type": ["Y"],
			},
			"Demographics": {
				"count": 136,
				"sources": {
					"Eurostat": "74d562e420b0137309bd9308af9a531f538b673063399cf617c4ae7edd3f3e41"
				},
				"to_period": "2023-01-01 00:00:00+00:00",
				"from_period": "1990-01-01 00:00:00+00:00",
				"period_type": ["Y"],
			},
		},
	},
	"2": {
		"count": 12,
		"region_type": "province",
		"access_level": "B",
		"region_level": 2,
		"with_geojson": 12,
		"regional_data_stats": {
			"Health": {
				"count": 132,
				"sources": {
					"Eurostat": "74d562e420b0137309bd9308af9a531f538b673063399cf617c4ae7edd3f3e41"
				},
				"to_period": "2021-01-01 00:00:00+00:00",
				"from_period": "2011-01-01 00:00:00+00:00",
				"period_type": ["Y"],
			},
			"Weather": {
				"count": 4972,
				"sources": {
					"Datagarden regional weather average for period": "651fe7527ba49b26d04ba0efb60d61c20623bd0ede885865798c4e31adc26002",
					"Datagarden regional average weather observations": "381446f192c65fb2fdef13468d81a88df029af764a9d8cc69d57d9ccf24ff58f",
				},
				"to_period": "2024-12-15 00:00:00+00:00",
				"from_period": "2024-01-01 00:00:00+00:00",
				"period_type": ["D", "M", "Q", "W"],
			},
			"Economics": {
				"count": 336,
				"sources": {
					"Eurostat": "74d562e420b0137309bd9308af9a531f538b673063399cf617c4ae7edd3f3e41"
				},
				"to_period": "2022-01-01 00:00:00+00:00",
				"from_period": "1995-01-01 00:00:00+00:00",
				"period_type": ["Y"],
			},
			"Demographics": {
				"count": 408,
				"sources": {
					"Eurostat": "74d562e420b0137309bd9308af9a531f538b673063399cf617c4ae7edd3f3e41"
				},
				"to_period": "2023-01-01 00:00:00+00:00",
				"from_period": "1990-01-01 00:00:00+00:00",
				"period_type": ["Y"],
			},
		},
	},
	"3": {
		"count": 40,
		"region_type": "corop region",
		"access_level": "C",
		"region_level": 3,
		"with_geojson": 40,
		"regional_data_stats": {
			"Weather": {
				"count": 14403,
				"sources": {
					"Datagarden regional weather average for period": "651fe7527ba49b26d04ba0efb60d61c20623bd0ede885865798c4e31adc26002",
					"Datagarden regional average weather observations": "381446f192c65fb2fdef13468d81a88df029af764a9d8cc69d57d9ccf24ff58f",
				},
				"to_period": "2024-12-15 00:00:00+00:00",
				"from_period": "2024-01-01 00:00:00+00:00",
				"period_type": ["D", "M", "Q", "W"],
			},
			"Economics": {
				"count": 1120,
				"sources": {
					"Eurostat": "74d562e420b0137309bd9308af9a531f538b673063399cf617c4ae7edd3f3e41"
				},
				"to_period": "2022-01-01 00:00:00+00:00",
				"from_period": "1995-01-01 00:00:00+00:00",
				"period_type": ["Y"],
			},
			"Demographics": {
				"count": 1133,
				"sources": {
					"Eurostat": "74d562e420b0137309bd9308af9a531f538b673063399cf617c4ae7edd3f3e41"
				},
				"to_period": "2022-01-01 00:00:00+00:00",
				"from_period": "1990-01-01 00:00:00+00:00",
				"period_type": ["Y"],
			},
		},
	},
	"4": {
		"count": 355,
		"region_type": "city",
		"access_level": "C",
		"region_level": 4,
		"with_geojson": 355,
		"regional_data_stats": {
			"Health": {
				"count": 6365,
				"sources": {
					"RIVM": "c03303dca8ffad75aa858a49b668f564f0b9bfe6b6d5dfa1ad51e0e783e2690c"
				},
				"to_period": "2024-01-01 00:00:00+00:00",
				"from_period": "2006-01-01 00:00:00+00:00",
				"period_type": ["Y"],
			}
		},
	},
	"5": {
		"count": 3964,
		"region_type": "postcode-4",
		"access_level": "D",
		"region_level": 5,
		"with_geojson": 3963,
		"regional_data_stats": {
			"Household": {
				"count": 19806,
				"sources": {
					"CBS": "265d1922c3eeb74f91219896acce253e5ad6956eaf85755381b3869014c53d06"
				},
				"to_period": "2023-01-01 00:00:00+00:00",
				"from_period": "2019-01-01 00:00:00+00:00",
				"period_type": ["Y"],
			},
			"Demographics": {
				"count": 19806,
				"sources": {
					"CBS": "265d1922c3eeb74f91219896acce253e5ad6956eaf85755381b3869014c53d06"
				},
				"to_period": "2023-01-01 00:00:00+00:00",
				"from_period": "2019-01-01 00:00:00+00:00",
				"period_type": ["Y"],
			},
		},
	},
}


REGION_STATS_DATA = COUNTRY_STATS_DATA["1"]
CITY_STATS_DATA = COUNTRY_STATS_DATA["4"]
