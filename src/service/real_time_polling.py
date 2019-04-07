import src.repository.filesystem_helper as filesystem_helper
import src.service.helper.datetime_helper as date_helper
import src.repository.company_repository as company_repository
import numpy as np
import src.strategy.macd_strategy as macd_strategy
import src.strategy.buy_and_hold_strategy as buy_and_hold_strategy
import src.strategy.rsi_strategy as rsi_strategy
import src.strategy.random_strategy as random_strategy
import src.strategy.macd_and_rsi_strategy as macd_and_rsi_strategy


def get_historical_data(company_code, today_string):
    historical_data = filesystem_helper.load_historical_data(company_code)

    prices = historical_data['Adj Close'].values
    dates = np.array(list(map(lambda x: date_helper.parse_date_to_datetime(x), historical_data['Date'])))

    # remove 'today' from historical data if 'today' is present in the dataset
    if today_string == date_helper.format_date(dates[-1]):
        prices = prices[0:-1]
        dates = dates[0:-1]

    return dates, prices


def enrich_historical_data_with_today_price(dates, prices, today_datetime, today_information):
    today_price = float(today_information['regularMarketPrice']['raw'])

    # regularMarketTime

    prices_appended = np.append(prices, today_price)
    dates_appended = np.append(dates, today_datetime)

    return dates_appended, prices_appended


def get_beautiful_data(company_code):
    today_datetime = date_helper.today_date()
    today_string = date_helper.format_date(today_datetime)

    dates, prices = get_historical_data(company_code, today_string)

    today_information = company_repository.retrieve_company_quote_on_elasticsearch(company_code, today_string)

    if today_information:
        dates, prices = enrich_historical_data_with_today_price(dates, prices, today_datetime, today_information)

    return dates, prices


def do_polling(company_code):
    print('processing {}'.format(company_code))

    dates, prices = get_beautiful_data(company_code)

    # random_strategy.execute(company_code, dates, prices)
    # buy_and_hold_strategy.execute(company_code, dates, prices)
    macd_strategy.execute(company_code, dates, prices)
    rsi_strategy.execute(company_code, dates, prices)
    # macd_and_rsi_strategy.execute(company_code, dates, prices)

    print('finished {}'.format(company_code))
