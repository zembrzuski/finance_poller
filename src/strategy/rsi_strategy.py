from talib import MACD, RSI


def execute(company_code, dates, prices):
    rsi = RSI(prices, timeperiod=14)

    # verifico se estou comprado
    # se estou comprado, verifico signal
    #   se está positivo, mantenho
    #   se está negativo, vendo, estou é, ponho no banco de dados
    # se não estou comprado, verifico sinal
    #   se está positivo, compro
    #   se não está positivo, mantenho

    return None
