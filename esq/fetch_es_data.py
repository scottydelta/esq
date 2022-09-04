from .es_queries_generator import (label_value_query_generator,
                                   coordinates_query_generator,
                                   timeseries_query_generator)
import json


def fetch_aggr_data(es_client, data_source, data_type, data_field, size,
                    filters):
    try:
        if data_type == "keyword/text":
            resp = es_client.search(index=data_source,
                                    body=label_value_query_generator(
                                        filters, data_field, size))
            return [
                dict(label=data["key"], value=data["doc_count"])
                for data in resp["aggregations"]["result"]["buckets"]
            ]
        elif data_type == "coordinates":
            resp = es_client.search(index=data_source,
                                    body=coordinates_query_generator(
                                        filters, data_field, size))
            return [
                dict(
                    label=data["fields"]["username"][0],
                    value=[
                        float(format(float(coord.strip()), ".6f")) for coord in
                        data["fields"]["coordinates.coordinates"][0].split(",")
                    ][::-1],
                ) for data in resp["hits"]["hits"]
            ]
        elif data_type == "timeseries":
            resp = es_client.search(index=data_source,
                                    body=timeseries_query_generator(
                                        filters, data_field))

            return [
                dict(label=data["key"], value=data["doc_count"])
                for data in resp["aggregations"]["result"]["buckets"]
            ]
        else:
            pass
    except Exception as e:
        print(e)
        return []
