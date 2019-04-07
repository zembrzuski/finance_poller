import pandas
import src.config.local as config
import os


def persist_on_disk_a_company(company):
    file_path = '{}/{}.csv'.format(config.data_local_storage_filepath, company['company_code'])

    if os.path.isfile(file_path):
        os.remove(file_path)

    f = open(file_path, "w+")
    f.write(company['historical_data'])
    f.close()

    return company['company_code'], True


def load_historical_data(company_code):
    csv = pandas.read_csv('{}/{}.csv'.format(config.data_local_storage_filepath, company_code).format(company_code))
    return csv.dropna()


def persist_on_disk_an_order(order):
    file_path = '{}/ALL_ORDERS.txt'.format(config.data_local_storage_filepath)

    f = open(file_path, "a")
    f.write(order + '\n')
    f.close()
