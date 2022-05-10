"""Top-level package for esq."""

__author__ = """Vikash Bajaj"""
__email__ = 'contact@vikashbajaj.com'
__version__ = '0.1.13'

import pkg_resources
import elasticsearch
import json
from esq import fetch_es_data


"""Main module."""


class esq:

    def __init__(self, elasticsearch_client):
        self.elasticsearch_client = elasticsearch_client
        # check elasticsearch package version
        elasticsearch_version = tuple(
            map(int, pkg_resources.get_distribution("elasticsearch").version.split(".")))
        if elasticsearch_version < (7, 14, 2):
            self.use_body = True
        else:
            self.use_body = False

    def get_count(self, index_name, filters={}):
        return fetch_es_data.get_count(self.elasticsearch_client, index_name, filters, self.use_body)

    def get_aggregation(self, index_name, data_field, data_type='label_value', filters={}, size=10):
        return fetch_es_data.get_aggregation(self.elasticsearch_client, index_name, data_field, data_type, filters, size, self.use_body)
