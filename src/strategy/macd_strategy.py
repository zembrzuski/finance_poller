from talib import MACD
import src.service.helper.trade_service as trade_service


def execute(company_code, dates, prices):
    macd, macdsignal, macdhist = MACD(prices, fastperiod=12, slowperiod=26, signalperiod=9)
    position = trade_service.retrieve_position_for_a_company_and_a_strategy(company_code, 'macd')

    order = action_for_bought_strategy(macdsignal[-1]) \
        if position == 'HAVE_BOUGHT' \
        else action_for_not_positioned_strategy(macdsignal[-1])

    if order:
        some_info = 'macd ' + str(macdsignal[-1])
        trade_service.execute_order(company_code, dates[-1], prices[-1], order, 'macd', some_info)


def action_for_bought_strategy(signal):
    return None if signal > 0 else 'VENDA'


def action_for_not_positioned_strategy(signal):
    return 'COMPRA' if signal > 0 else None
