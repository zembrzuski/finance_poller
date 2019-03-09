import src.config.local as config
import requests


def import_a_company(company_code, from_epoch, to_epoch, crumb, cookie):
    yahoo_historical_url = config.yahoo_historical_url.format(company_code, from_epoch, to_epoch, crumb)
    headers = {'cookie': cookie}
    response = requests.get(yahoo_historical_url, headers=headers).content.decode('utf-8')

    print(response)


def import_chunks_historical(companies, from_epoch, to_epoch, crumb, cookie):
    algow = list(map(
        lambda x: import_a_company(x, from_epoch, to_epoch, crumb, cookie),
        companies))

    print(algow)
