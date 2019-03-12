import requests
import src.config.local as config


def persist(index, type_es, payload, id_es):
    persistence_address = '{}/{}/{}/{}'.format(config.elasticsearch_address, index, type_es, id_es)
    post_response = requests.post(persistence_address, json=payload)

    return post_response


def retrieve_by_id(index, type_es, id_es):
    persistence_address = '{}/{}/{}/{}'.format(config.elasticsearch_address, index, type_es, id_es)
    return requests.get(persistence_address).json()['_source']


def retrieve_all_by_index_and_group(index, type_es):
    persistence_address = '{}/{}/{}'.format(config.elasticsearch_address, index, type_es)
    return requests.get(persistence_address).json()['hits']['hits']


def retrieve_max_element_given_a_field(index, type_es, field):
    query_address = '{}/{}/{}/_search'.format(config.elasticsearch_address, index, type_es)

    query = {
        "query": {"match_all": {}},
        "sort": {field: {"order": "desc"}},
        "size": 1
    }

    return requests.post(query_address, json=query)
