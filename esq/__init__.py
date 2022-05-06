"""Top-level package for esq."""

__author__ = """Vikash Bajaj"""
__email__ = 'contact@vikashbajaj.com'
__version__ = '0.1.11'


import json
from .es_queries_generator import (
    label_value_query_generator,
    coordinates_query_generator,
    timeseries_query_generator,
    docs_query_generator,
)


"""Main module."""
class esq:  
      
    def __init__(self, elasticsearch_client):  
        self.elasticsearch_client = elasticsearch_client  
      


