import datetime
import pytz

sao_paulo_datetime = pytz.timezone("America/Sao_Paulo")


def convert_from_epoch_to_utcdatetime(raw):
    my_datetime_brt = datetime.datetime.fromtimestamp(raw)
    local_dt = sao_paulo_datetime.localize(my_datetime_brt, is_dst=None)
    utc_datetime = local_dt.astimezone(pytz.utc)

    return utc_datetime


def utcdatetime_to_elasticsearch_format(utc_datetime):
    return utc_datetime.strftime("%Y-%m-%dT%H:%M:%S.000")


def parse_date_to_datetime(date):
    return datetime.datetime.strptime(date, "%Y-%m-%d")


def today_date():
    return datetime.datetime.now()


def format_today_date(d):
    return d.strftime("%Y-%m-%d")
