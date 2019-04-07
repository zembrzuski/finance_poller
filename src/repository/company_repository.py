import src.repository.elasticsearch_helper as elasticsearch_helper
import src.service.helper.datetime_helper as datetime_helper


def persist_company_quote_on_elasticsearch(company):
    response = elasticsearch_helper.persist(
        index=company_slug(company['symbol']),
        type_es='quotes',
        payload=company,
        id_es=company['datetime'][0:10])

    return response.status_code, company['symbol']


def persist_an_order(company, strategy, price, date, order):
    return elasticsearch_helper.post_an_order(
        company_slug(company),
        strategy,
        price,
        datetime_helper.utcdatetime_to_elasticsearch_format(date),
        order
    )


def retrieve_company_quote_on_elasticsearch(company_code, today):
    return elasticsearch_helper.retrieve_by_id(
        index=company_slug(company_code),
        type_es='quotes',
        id_es=today
    )


def retrieve_last_order_for_company_and_strategy(company, strategy):
    last_order = elasticsearch_helper.retrieve_last_order_for_a_company_and_strategy(company_slug(company), strategy)

    if last_order.status_code == 404:
        return None

    hits = last_order.json()['hits']['hits']

    return hits[0]['_source'] if len(hits) > 0 else None


def company_slug(company):
    return company.replace('.', '').lower()
