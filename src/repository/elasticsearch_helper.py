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


def retrieve_last_order_for_a_company_and_strategy(company, strategy):
    query_address = '{}/{}/{}/_search'.format(config.elasticsearch_address, 'orders', 'orders')

    query = {
        "query": {
            "bool": {
                "must": [
                    {"term": {"company": company}},
                    {"term": {"strategy": strategy}}
                ]
            }
        },
        "sort": {"date": {"order": "desc"}},
        "size": 1
    }

    return requests.post(query_address, json=query)


def post_an_order(company, strategy, price, date, order):
    query_address = '{}/{}/{}'.format(config.elasticsearch_address, 'orders', 'orders')

    payload = {
        'company': company,
        'strategy': strategy,
        'price': price,
        'date': date,
        'order': order
    }

    return requests.post(query_address, json=payload)
