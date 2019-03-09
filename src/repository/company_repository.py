import src.repository.elasticsearch_helper as elasticsearch_helper


def persist_company_on_elasticsearch(company):
    response = elasticsearch_helper.persist(
        index=company['symbol'].replace('.', '').lower(),
        type='quotes',
        payload=company,
        id=company['datetime'])

    return response.status_code, company['symbol']
