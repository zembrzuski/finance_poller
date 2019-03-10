import requests
import src.config.local as config


def persist(index, type_es, payload, id_es):
    persistence_address = '{}/{}/{}/{}'.format(config.elasticsearch_address, index, type_es, id_es)
    post_response = requests.post(persistence_address, json=payload)

    return post_response


def retrieve_by_id(index, type_es, id_es):
    persistence_address = '{}/{}/{}/{}'.format(config.elasticsearch_address, index, type_es, id_es)
    return requests.get(persistence_address).json()['_source']
