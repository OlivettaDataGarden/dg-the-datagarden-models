.. The-Datagarden-Models documentation master file, created by
   sphinx-quickstart on Sat Nov 23 11:12:08 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

=====================
The-Datagarden-Models
=====================


The-Datagarden-Models documentation
===================================

ode**The-Datagarden-Models** is a package provided by The-Datagarden.io to support its API with the Pydantics models compliant to the output of the API

.. start-badges

.. list-table::
    :widths: 8 50
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - |codecov|
    * - package
      - |version| |commits-since|

.. |docs| image:: https://readthedocs.org/projects/errors/badge/?style=flat
    :target: https://errors.readthedocs.io/
    :alt: Documentation Status

.. |codecov| image:: https://codecov.io/gh/MaartendeRuyter/errors/branch/master/graphs/badge.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/MaartendeRuyter/errors

.. |version| image:: https://img.shields.io/pypi/v/error-manager.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/error-manager

.. |commits-since| image:: https://img.shields.io/github/commits-since/MaartendeRuyter/errors/v0.1.0.svg
    :alt: Commits since latest release
    :target: https://github.com/MaartendeRuyter/errors/compare/v0.1.0...master



.. end-badges


error-manager main use cases
----------------------------
Main use case for the error-manager package is to implement a ``ListErrors`` class that can be used throughout
your project to define and access immutable standard error codes and descriptions ::

    # retrieve customer defined ErrorCode object form ``ListErrors`` class
    >>> from errors.error import ListErrors
    >>> ListErrors.API_GET_RETURNED_404
    ErrorCode(
        code='ER_API404_00001',
        description='API get request returned 404',
        error_data={})

    # add custom error data to error message when you want to persist or log the error
    # As the errorcode are immutable the add_error_data returns a new error (immutable) error code.
    >>> from errors.base import add_error_data
    >>> error_without_data = ListErrors.API_GET_RETURNED_404
    >>> error_with_data = add_error_data(error_without_data, {'url': 'www.bad_url.com'})
    >>> error_with_data
    ErrorCode(
        code='ER_API404_00001',
        description='API get request returned 404',
        error_data={'url': 'www.bad_url.com'})

This ErrorCode could be returned by the method performing the request so that
the logic calling this method is aware of the failing request.

In order to use a single type as return value the error-manager package introduces a `ReturnValue` class
that can hold the actual response, any possible downstream errors and the status of the return value. See
ReturnValue documentation.


.. toctree::
   :maxdepth: 1
   :caption: Contents:
