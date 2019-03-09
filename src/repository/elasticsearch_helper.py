import requests
import src.config.local as config


def persist(index, type, payload, id):
    persistence_address = '{}/{}/{}/{}'.format(config.elasticsearch_address, index, type, id)
    post_response = requests.post(persistence_address, json=payload)

    return post_response
