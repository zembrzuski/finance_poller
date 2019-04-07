from talib import RSI
import src.service.helper.trade_service as trade_service


def execute(company_code, dates, prices):
    rsi = RSI(prices, timeperiod=14)

    position = trade_service.retrieve_position_for_a_company_and_a_strategy(company_code, 'rsi')

    print(rsi[-1])

    order = action_for_bought_strategy(rsi[-1]) \
        if position == 'HAVE_BOUGHT' \
        else action_for_not_positioned_strategy(rsi[-1])

    if order:
        some_info = 'macd ' + str(rsi[-1])
        trade_service.execute_order(company_code, dates[-1], prices[-1], order, 'rsi', some_info)


def action_for_bought_strategy(rsi):
    return 'VENDA' if rsi > 75 else None


def action_for_not_positioned_strategy(rsi):
    return 'COMPRA' if rsi < 25 else None
