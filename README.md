# esq

[![Build Status](https://img.shields.io/pypi/v/esq.svg)](https://pypi.python.org/pypi/esq) [![[pypi]](https://github.com/scottydelta/esq/actions/workflows/python-publish.yml/badge.svg)](https://github.com/scottydelta/esq/actions/workflows/python-publish.yml) [![Documentation Status](https://readthedocs.org/projects/esq/badge/?version=latest)](https://esq.readthedocs.io/en/latest/?version=latest)

[Install](#install) - [Init](#init) - [Usage](#usage) - [Documentation](#documentation)

A python package that provides GraphQL API for Elasticsearch and makes it easier to query data without writing complex queries.

## Install

    pip install esq

## Init

```python
>>> from esq import Esq
>>> from elasticsearch import Elasticsearch

# init your Elasticsearch client object here
>>> ELASTICSEARCH_URI = "http://localhost:9200"
>>> es_client = Elasticsearch([ELASTICSEARCH_URI])

# init your Esq object here
>>> esq = Esq(es_client)

# now you can start making queries
```

## Usage

```python
# to get aggregation on sentiment field on your twitter index, you can simply do:
>>> sentiments = esq.get_aggr_data(index='twitter',
                        data_type='keyword/text', #data_type is an enum('keyword/text', 'coordinates', 'timeseries')
                        data_field='sentiment')

>>> print(sentiments)
[{'label': 'positive', 'value': 9}, {'label': 'neutral', 'value': 7}, {'label': 'negative', 'value': 1}]
```

## Documentation

[Read the full documentation here](https://esq.readthedocs.io/en/latest/?version=latest)
