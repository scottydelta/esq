# esq

[![Build Status](https://img.shields.io/pypi/v/esq.svg)](https://pypi.python.org/pypi/esq) [![[pypi]](https://github.com/scottydelta/esq/actions/workflows/python-publish.yml/badge.svg)](https://github.com/scottydelta/esq/actions/workflows/python-publish.yml) [![Documentation Status](https://readthedocs.org/projects/esq/badge/?version=latest)](https://esq.readthedocs.io/en/latest/?version=latest)

[Install](<#quick install>) - [Usage](#usage)

A python package that provides GraphQL API for Elasticsearch and makes it easier to query data from without writing complex queries.

## Quick Install

    pip install esq

## Usage

```python
from esq import Esq
from elasticsearch import Elasticsearch


# init your Elasticsearch client object here
es_client = Elasticsearch()

# init your Esq object here
esq = Esq(es_client)

# now you can start making queries

```


