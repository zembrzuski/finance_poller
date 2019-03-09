import requests
import src.config.local as config
import src.service.helper.company_converter as company_converter
import src.repository.company_repository as company_repository

def main():
    companies_array = ','.join(config.companies)
    companies_retrieved = requests.get(config.yahoo_url_for_polling.format(companies_array)).json()

    companies_to_persist = list(map(
        lambda x: company_converter.convert_company_from_yahoo_to_elasticsearch_entity(x),
        companies_retrieved['quoteResponse']['result']))

    persistence_result = list(map(
        lambda x: company_repository.persist_company_on_elasticsearch(x),
        companies_to_persist))

    print(companies_retrieved)


if __name__ == '__main__':
    main()
