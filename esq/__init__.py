"""Top-level package for esq."""

__author__ = """Vikash Bajaj"""
__email__ = 'esq@vikashbajaj.com'
__version__ = '1.0.2'

from .fetch_es_data import (fetch_aggr_data)
"""Main module."""


class Esq:

    def __init__(self, elasticsearch_client):
        try:
            if elasticsearch_client.ping():
                self.elasticsearch_client = elasticsearch_client
            else:
                raise ConnectionError("Cannot connect to the Elasticsearch, \
                        check the Elasticsearch object and try again.")
        except:
            raise ConnectionError("Cannot connect to the Elasticsearch, \
                    check the Elasticsearch object and try again.")

    def get_aggr_data(self,
                      index,
                      data_type,
                      data_field,
                      size=100,
                      filters=[]):
        return fetch_aggr_data(self.elasticsearch_client, index, data_type,
                               data_field, size, filters)
