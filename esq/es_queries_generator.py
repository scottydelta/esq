def filter_query_generator(filters):
    processed_filters = filters
    query_obj = {
        "bool": {
            "must": [],
            "filter": [],
            "should": [],
            "must_not": []
        }
    }
    bool_type = "filter"
    if (len(filters)
            == 1) and (filters[0]["filter_data_field"] == "label_value") and (
                len(filters[0]["filter_value"].split(",")) > 1):
        bool_type = "should"
        filter_field = filters[0]["filter_field"]
        processed_filters = [{
            'filter_data_field': 'label_value',
            'filter_field': filter_field,
            'filter_value': item
        } for item in filters[0]["filter_value"].split(",")]
    for elem in processed_filters:
        if elem.get("filter_data_field") == "label_value":
            filter_query = {
                "match_phrase": {
                    "%s" % (elem["filter_field"], ):
                    "%s" % (elem["filter_value"], )
                }
            }
        elif elem.get("filter_data_field") == "timeseries":
            filter_query = {
                "range": {
                    "%s" % (elem["filter_field"], ): {
                        "gte": "%s" % (elem["filter_value"].split(",")[0], ),
                        "lte": "%s" % (elem["filter_value"].split(",")[1], ),
                    }
                }
            }
        elif elem.get("filter_data_field") == "coordinates":
            filter_query = {
                "geo_bounding_box": {
                    "%s.coordinates" % (elem["filter_field"], ): {
                        "top_left": [
                            float(format(float(coord.strip()), ".6f"))
                            for coord in elem["filter_value"].split(",")[:2]
                        ],
                        "bottom_right": [
                            float(format(float(coord.strip()), ".6f"))
                            for coord in elem["filter_value"].split(",")[2:]
                        ],
                    }
                }
            }
        else:
            filter_query = None
        if filter_query is not None:
            query_obj["bool"][bool_type].append(filter_query)
    return query_obj


def label_value_query_generator(filters, keyword_field, size):

    keyword_query = {
        "aggs": {
            "result": {
                "terms": {
                    "field": "%s" % (keyword_field, ),
                    "order": {
                        "_count": "desc"
                    },
                    "size": size
                }
            }
        },
        "size": 0,
    }
    keyword_query["query"] = filter_query_generator(filters)
    return keyword_query


def coordinates_query_generator(filters, coordinates_field, size):

    coordinates_query = {
        "docvalue_fields":
        ["%s.coordinates" % (coordinates_field, ), "username"],
        "size": size,
        "stored_fields": ["%s.coordinates" % (coordinates_field, )],
        "script_fields": {},
        "query": {
            "bool": {
                "must": [],
                "filter": [
                    {
                        "match_all": {}
                    },
                    {
                        "bool": {
                            "should": [{
                                "exists": {
                                    "field": "coordinates.type"
                                }
                            }],
                            "minimum_should_match": 1
                        }
                    },
                ],
            }
        },
    }
    return coordinates_query


def timeseries_query_generator(filters, timeseries_field):

    timeseries_query = {
        "aggs": {
            "result": {
                "date_histogram": {
                    "field": "%s" % (timeseries_field, ),
                    "fixed_interval": "1h",
                    "time_zone": "Asia/Calcutta",
                    "min_doc_count": 1,
                }
            }
        },
        "size":
        0,
        "stored_fields": ["*"],
        "docvalue_fields": [{
            "field": "%s" % (timeseries_field, ),
            "format": "date_time"
        }],
    }
    timeseries_query["query"] = filter_query_generator(filters)
    return timeseries_query


def docs_query_generator(requested_data_fields, filters, size):
    docs_query = {
        "_source": requested_data_fields,
        "size": size,
        "sort": {
            "created_utc": "desc"
        },
    }
    docs_query["query"] = filter_query_generator(filters)
    return docs_query


def label_value_query_generator(filters, keyword_field, size):

    keyword_query = {
        "aggs": {
            "result": {
                "terms": {
                    "field": "%s" % (keyword_field, ),
                    "order": {
                        "_count": "desc"
                    },
                    "size": size
                }
            }
        },
        "size": 0,
    }
    keyword_query["query"] = filter_query_generator(filters)
    return keyword_query
