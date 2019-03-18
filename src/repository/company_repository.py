import src.repository.elasticsearch_helper as elasticsearch_helper


def persist_company_on_elasticsearch(company):
    response = elasticsearch_helper.persist(
        index=company['symbol'].replace('.', '').lower(),
        type_es='quotes',
        payload=company,
        id_es=company['datetime'][0:10])

    return response.status_code, company['symbol']


def retrieve_company_quote_on_elasticsearch(company_code, today):
    return elasticsearch_helper.retrieve_by_id(
        index=company_code.replace('.', '').lower(),
        type_es='quotes',
        id_es=today
    )


def retrieve_all_orders(company_code):
    return elasticsearch_helper.retrieve_all_by_index_and_group(
        index=company_code.replace('.', '').lower(),
        type_es='orders'
    )
