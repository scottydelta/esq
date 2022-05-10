from esq import generate_es_query


def get_count(elasticsearch_client, index_name, filters, use_body):
    try:
        _count = elasticsearch_client.count(index=index_name)
        return dict(count=_count.get("count", 0))
    except ValueError as e:
        return []


def get_docs(elasticsearch_client, index_name, data_fields, filters, size, use_body):
    try:
        fields = data_fields.split(",")
        query = generate_es_query.docs_query_generator(fields, filters, size)
        if use_body:
            resp = elasticsearch_client.search(index=index_name, body=query)
        else:
            resp = elasticsearch_client.search(index=index_name, query=query)
        if "id" in fields:
            return_data = [{**obj["_source"], "id": obj["_id"]}
                           for obj in resp["hits"]["hits"]]
        else:
            return_data = [obj["_source"] for obj in resp["hits"]["hits"]]
        return return_data
    except (KeyError, AttributeError, ValueError) as e:
        return []


def get_aggregation(elasticsearch_client, index_name, data_field, data_type, filters, size, use_body):
    try:
        if data_type == "label_value":
            query = generate_es_query.label_value_query_generator(
                filters, data_field, size)
            if use_body:
                resp = elasticsearch_client.search(
                    index=index_name, body=query)
            else:
                resp = elasticsearch_client.search(
                    index=index_name, query=query)
            return_data = resp["aggregations"]["result"]["buckets"]
            return [dict(label=data["key"], value=data["doc_count"]) for data in return_data]
        elif data_type == "coordinates":
            query = generate_es_query.coordinates_query_generator(
                filters, data_field, size)
            if use_body:
                resp = elasticsearch_client.search(
                    index=index_name, body=query)
            else:
                resp = elasticsearch_client.search(
                    index=index_name, query=query)
            return_data = resp["hits"]["hits"]
            return [
                dict(
                    label=data["fields"]["username"][0],
                    value=[
                        float(format(float(coord.strip()), ".6f"))
                        for coord in data["fields"]["coordinates.coordinates"][0].split(",")
                    ][::-1],
                )
                for data in return_data
            ]
        elif data_type == "timeseries":
            query = generate_es_query.timeseries_query_generator(
                filters, data_field)
            if use_body:
                resp = elasticsearch_client.search(
                    index=index_name, body=query)
            else:
                resp = elasticsearch_client.search(
                    index=index_name, query=query)
            return_data = resp["aggregations"]["result"]["buckets"]
            return [dict(label=data["key"], value=data["doc_count"]) for data in return_data]
    except (KeyError, AttributeError, ValueError) as e:
        return []
