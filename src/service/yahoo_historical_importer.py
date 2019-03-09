import src.config.local as config
import requests


def import_a_company(company_code, from_epoch, to_epoch, crumb, cookie):
    yahoo_historical_url = config.yahoo_historical_url.format(company_code, from_epoch, to_epoch, crumb)
    headers = {'cookie': cookie}
    response = requests.get(yahoo_historical_url, headers=headers).content.decode('utf-8')

    print(response)


def import_chunks(companies, from_epoch, to_epoch, crumb, cookie):
    return list(map(
        lambda company: import_a_company(company, from_epoch, to_epoch, crumb, cookie),
        companies))


def import_historical_data(companies_chunks):
    print('visit this site, please: \n https://finance.yahoo.com/quote/PETR4.SA?p=PETR4.SA&.tsrc=fin-srch')
    print('click historical data')
    print('click apply')
    print('click download data')
    print('at network inspection console, look for PETR4.SA?period1=XXXXXXXXXXXXXXXX')
    from_epoch = 1262311200
    to_epoch = 1893463200
    crumb = input('then, type the crumb property on the request address. It is something like U4e8eDQi/yI\n')
    cookie = input('the, type the cookie parameter (look on the headers of the request)\n')

    return list(map(
        lambda x: import_chunks(x, from_epoch, to_epoch, crumb, cookie),
        companies_chunks))
