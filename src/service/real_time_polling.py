import src.repository.filesystem_helper as filesystem_helper
import src.service.helper.datetime_helper as date_helper
import src.repository.company_repository as company_repository
import numpy as np


def do_polling(company_code):
    historical_data = filesystem_helper.load_historical_data(company_code)

    prices = historical_data['Adj Close'].values
    dates = np.array(list(map(lambda x: date_helper.parse_date_to_datetime(x), historical_data['Date'])))

    today_formatted = '2019-03-08'   # fake date
    today_information = company_repository.retrieve_company_quote_on_elasticsearch(company_code, today_formatted)

    today_price = float(today_information['regularMarketPrice']['raw'])

    today = date_helper.today_date()

    prices_appended = np.append(prices, today_price)
    dates_appended = np.append(dates, today)

    print('oi')
    # append today's price
    # compute indicators
    # apply rule to buy or sell
    print(company_code)
