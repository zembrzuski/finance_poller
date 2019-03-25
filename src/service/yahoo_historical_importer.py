import src.config.local as config
import src.repository.filesystem_helper as filesystem_helper
import requests
import datetime


def retrieve_company_historical_data_from_yahoo(company_code, from_epoch, to_epoch, crumb, cookie):
    print('retrieving ' + company_code)
    yahoo_historical_url = config.yahoo_historical_url.format(company_code, from_epoch, to_epoch, crumb)
    headers = {'cookie': cookie}
    response = requests.get(yahoo_historical_url, headers=headers).content.decode('utf-8')

    return {
        'company_code': company_code,
        'historical_data': response
    }


def import_chunks(companies, from_epoch, to_epoch, crumb, cookie):
    historical_data = list(map(
        lambda company: retrieve_company_historical_data_from_yahoo(company, from_epoch, to_epoch, crumb, cookie),
        companies
    ))

    return list(map(
        lambda company: filesystem_helper.persist_on_disk_a_company(company),
        historical_data
    ))


def import_historical_data(companies_chunks):
    january_first_2010 = 1262311200
    now_epoch = int(datetime.datetime.now().timestamp())
    print('from epoch: {}'.format(january_first_2010))
    print('to epoch: {}'.format(now_epoch))
    print('visit this site, please: \n https://finance.yahoo.com/quote/PETR4.SA?p=PETR4.SA&.tsrc=fin-srch')
    print('click historical data')
    print('click apply')
    print('click download data')
    print('at network inspection console, look for PETR4.SA?period1=XXXXXXXXXXXXXXXX')

    crumb = input('then, type the crumb property on the request address. It is something like U4e8eDQi/yI\n')
    cookie = input('the, type the cookie parameter (look on the headers of the request)\n')

    return list(map(
        lambda x: import_chunks(x, january_first_2010, now_epoch, crumb, cookie),
        companies_chunks
    ))
