import src.config.local as config
import requests


def import_historical_data(company_code, from_epoch, to_epoch, crumb, cookie):
    yahoo_historical_url = config.yahoo_historical_url.format(company_code, from_epoch, to_epoch, crumb)
    headers = {'cookie': cookie}
    response = requests.get(yahoo_historical_url, headers=headers).content.decode('utf-8')

    print(response)
