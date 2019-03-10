import pandas
import src.config.local as config


def persist_on_disk_a_company(company):
    f = open('{}/{}.csv'.format(config.data_local_storage_filepath, company['company_code']), "w+")
    f.write(company['historical_data'])
    f.close()

    return company['company_code'], True


def load_historical_data(company_code):
    csv = pandas.read_csv('{}/{}.csv'.format(config.data_local_storage_filepath, company_code).format(company_code))
    return csv.dropna()

