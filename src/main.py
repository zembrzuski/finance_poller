import requests
import src.config.config as config
import src.service.helper.datetime_helper as datetime_helper



def process_a_company(company):
    utc_datetime = datetime_helper.convert_from_epoch_to_utcdatetime(company['regularMarketTime']['raw'])
    datetime_formatted = datetime_helper.utcdatetime_to_elasticsearch_format(utc_datetime)
    print(datetime_formatted)


def main():
    companies_array = ','.join(config.companies)
    resp = requests.get(config.yahoo_url_for_polling.format(companies_array)).json()

    for company in resp['quoteResponse']['result']:
        process_a_company(company)

    print(resp)


if __name__ == '__main__':
    main()
