import requests
import src.config.config as config
import datetime
import pytz


def process_datetime(raw):
    local = pytz.timezone("America/Sao_Paulo")
    my_datetime_brt = datetime.datetime.fromtimestamp(raw)
    local_dt = local.localize(my_datetime_brt, is_dst=None)
    brt_datetime = local_dt.astimezone(pytz.utc)

    formatted = brt_datetime.strftime("%Y-%m-%dT%H:%M:%S.000")
    print(formatted)


def process_a_company(company):
    process_datetime(company['regularMarketTime']['raw'])
    print('oi')
    pass


def main():
    companies_array = ','.join(config.companies)
    resp = requests.get(config.yahoo_url_for_polling.format(companies_array)).json()

    for company in resp['quoteResponse']['result']:
        process_a_company(company)

    print(resp)


if __name__ == '__main__':
    main()
