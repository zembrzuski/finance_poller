from talib import RSI, MACD
import src.service.helper.trade_service as trade_service


def execute(company_code, dates, prices):
    rsi = RSI(prices, timeperiod=14)
    macd, macdsignal, macdhist = MACD(prices, fastperiod=12, slowperiod=26, signalperiod=9)

    position = trade_service.retrieve_position_for_a_company_and_a_strategy(company_code, 'rsi_macd')

    order = action_for_bought_strategy(rsi[-1], macdsignal[-1]) \
        if position == 'HAVE_BOUGHT' \
        else action_for_not_positioned_strategy(rsi[-1], macdsignal[-1])

    if order:
        some_info = 'macd ' + str(rsi[-1])
        trade_service.execute_order(company_code, dates[-1], prices[-1], order, 'rsi_and_macd', some_info)


def action_for_bought_strategy(rsi, macdsignal):
    rsi_sell = (rsi > 70) + 0
    macd_sell = (macdsignal < 0) + 0

    return 'VENDA' if (rsi_sell + macd_sell) == 2 else None


def action_for_not_positioned_strategy(rsi, macdsignal):
    rsi_buy = (rsi < 30) + 0
    macd_buy = (macdsignal > 0) + 0

    return 'COMPRA' if (rsi_buy + macd_buy) == 2 else None
