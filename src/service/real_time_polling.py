import src.repository.filesystem_helper as filesystem_helper
import src.service.helper.datetime_helper as date_helper
import src.repository.company_repository as company_repository
import numpy as np
import src.strategy.macd_strategy as macd_strategy
import src.service.helper.trade_service as trade_service
from talib import MACD, RSI


def get_historical_data(company_code, today_string):
    historical_data = filesystem_helper.load_historical_data(company_code)

    prices = historical_data['Adj Close'].values
    dates = np.array(list(map(lambda x: date_helper.parse_date_to_datetime(x), historical_data['Date'])))

    # remove 'today' from historical data if 'today' is present in the dataset
    if today_string == date_helper.format_date(dates[-1]):
        prices = prices[0:-1]
        dates = dates[0:-1]

    return dates, prices


def enrich_historical_data_with_today_price(dates, prices, company_code, today_string, today_datetime):
    today_information = company_repository.retrieve_company_quote_on_elasticsearch(company_code, today_string)
    today_price = float(today_information['regularMarketPrice']['raw'])

    prices_appended = np.append(prices, today_price)
    dates_appended = np.append(dates, today_datetime)

    return dates_appended, prices_appended


def get_beautiful_data(company_code):
    today_datetime = date_helper.today_date()
    today_string = date_helper.format_date(today_datetime)

    dates, prices = get_historical_data(company_code, today_string)
    dates, prices = enrich_historical_data_with_today_price(dates, prices, company_code, today_string, today_datetime)

    return dates, prices


def do_polling(company_code):
    # TODO nem sempre preciso de todo o histórico. muitas vezes, como no caso do macd, só preciso dos últimos dados.
    dates, prices = get_beautiful_data(company_code)

    random_strategy(company_code)
    buy_and_hold_strategy(company_code)
    macd_strategy(company_code)
    rsi_strategy(company_code)
    macd_and_rsi_strategy(company_code)

    macd, macdsignal, macdhist = MACD(prices, fastperiod=12, slowperiod=26, signalperiod=9)
    rsi = RSI(prices, timeperiod=14)

    current_position = trade_service.retrieve_position_for_a_company(company_code)

    macd_strategy.compute_macd_strategy(company_code, macdsignal)

    print(company_code)
