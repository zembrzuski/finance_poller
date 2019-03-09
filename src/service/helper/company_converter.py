import src.service.helper.datetime_helper as datetime_helper
import copy


def convert_company_from_yahoo_to_elasticsearch_entity(company):
    utc_datetime = datetime_helper.convert_from_epoch_to_utcdatetime(company['regularMarketTime']['raw'])
    datetime_formatted = datetime_helper.utcdatetime_to_elasticsearch_format(utc_datetime)

    element_to_persist = copy.deepcopy(company)
    element_to_persist['datetime'] = datetime_formatted

    return element_to_persist
