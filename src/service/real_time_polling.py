import src.repository.filesystem_helper as filesystem_helper
import src.service.helper.datetime_helper as date_helper
import numpy as np


def do_polling(company_code):
    historical_data = filesystem_helper.load_historical_data(company_code)

    prices = historical_data['Adj Close'].values
    dates = np.array(list(map(lambda x: date_helper.parse_date_to_datetime(x), historical_data['Date'])))

    # read historical data from disk
    # append today's price
    # compute indicators
    # apply rule to buy or sell
    print(company_code)
