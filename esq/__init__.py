"""Top-level package for esq."""

__author__ = """Vikash Bajaj"""
__email__ = 'esq@vikashbajaj.com'
__version__ = '1.0.1'


import json
from .es_queries_generator import (
    label_value_query_generator,
    coordinates_query_generator,
    timeseries_query_generator,
    docs_query_generator,
)


"""Main module."""


class Esq:

    def __init__(self, elasticsearch_client):
        self.elasticsearch_client = elasticsearch_client
