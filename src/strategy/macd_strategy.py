from talib import MACD

def execute(company_code, dates, prices):
    macd, macdsignal, macdhist = MACD(prices, fastperiod=12, slowperiod=26, signalperiod=9)

    # verifico se estou comprado
    # se estou comprado, verifico signal
    #   se está positivo, mantenho
    #   se está negativo, vendo, estou é, ponho no banco de dados
    # se não estou comprado, verifico sinal
    #   se está positivo, compro
    #   se não está positivo, mantenho

    return None
