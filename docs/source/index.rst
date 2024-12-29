=====================
the-datagarden-models
=====================

The-datagarden-models package is supporting package for the-datagarden api (see `The DataGarden Website <https://www.the-datagarden.io>`_) and
the-datagarden package (see `the-datagarden package <https://pypi.org/project/the-datagarden/>`_). The-datagarden api and package
are developed to give data professionals easy access to regional data from public sources without having to understand the sources, api's and data formats
from those public data sources.

This includes data from sources like United Nations, World Bank, World Health Organization, Eurostat but also local sources like the
Dutch Central Bureau of Statistics (CBS) and the UK Office for National Statistics (ONS). Obviously new sources and data from existing sources
are added by the DataGarden team.

The data retrieved from the different sources are converted in single generic data model in different themes like demographics, economics, health, social environment, etc.
The user of TheDataGarden API therefor does not need to worrie about the difference in models and datastructure from the original data source procviders.
For each theme there is a single Pydantic model created that can be used to work with the data returned by the-datagarden api.

This contains all the Pydantic models for the data returned by the-datagarden api and can be used to work with the data
returned by the api in a more pythonic way than only using the json.

A quick example
---------------
If you have a user account at the-datagarden.io, you can start using the SDK right away:

.. code-block:: python

    # Retrieve a country object from the datagarden API
    >>> from the-datagarden import TheDataGardenAPI
    >>> the_datagarden_api = TheDataGardenAPI(email='your-email@example.com', password='your-password')
    >>> nl = the_datagarden_api.netherlands()
    >>> nl_demographics = nl.demographics(from_period="2010-01-01", source="united nations")
    >>> nl_demographics
        TheDataGardenRegionalDataModel : Demographics : (count=15)

this returns a `TheDataGardenRegionalDataModel` containimg the demographics data in this case 15 records.
Each of those records will contain a the standardized Demographics Data object for the Netherlands for each
year since 2010.


Read more
---------

* `The DataGarden Website <https://www.the-datagarden.io>`_
* `API Documentation <https://www.the-datagarden.io/api-docs>`_
* `Documentation on the Datagarden Models <https://www.the-datagarden.io/data-docs>`_
* `GitHub Repository for the-datagarden-models <https://github.com/MaartendeRuyter/dg-the-datagarden-models>`_

Access to The DataGarden API
----------------------------
To use the DataGarden SDK, you need access to the The DataGarden API. Simply register for free at https://www.the-datagarden.io
and you will have an inital free access account to the API with access to country and continent data.

Visit https://www.the-datagarden.io to register for free.
