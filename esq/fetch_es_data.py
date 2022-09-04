from .es_queries_generator import (label_value_query_generator)
import json


def fetch_aggr_data(es_client, data_source, data_type, data_field, size,
                    filters):
    try:
        if data_type == "keyword/text":
            resp = es_client.search(index=data_source,
                                    body=label_value_query_generator(
                                        filters, data_field, size))
            return_data = resp["aggregations"]["result"]["buckets"]
            return [
                dict(label=data["key"], value=data["doc_count"])
                for data in return_data
            ]
        elif data_type == "coordinates":
            req = requests.post(es_query_uri,
                                json.dumps(
                                    coordinates_query_generator(
                                        filters, data_field, size)),
                                headers=headers)
            resp = req.json()
            return_data = resp["hits"]["hits"]
            return [
                dict(
                    label=data["fields"]["username"][0],
                    value=[
                        float(format(float(coord.strip()), ".6f")) for coord in
                        data["fields"]["coordinates.coordinates"][0].split(",")
                    ][::-1],
                ) for data in return_data
            ]
        elif data_type == "timeseries":
            req = requests.post(
                es_query_uri,
                json.dumps(timeseries_query_generator(filters, data_field)),
                headers=headers)
            resp = req.json()
            return_data = resp["aggregations"]["result"]["buckets"]
            return [
                dict(label=data["key"], value=data["doc_count"])
                for data in return_data
            ]
        else:
            pass
    except Exception as e:
        print(e)
        return []
