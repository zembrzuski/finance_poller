from talib import MACD
import src.service.helper.trade_service as trade_service

def execute(company_code, dates, prices):
    macd, macdsignal, macdhist = MACD(prices, fastperiod=12, slowperiod=26, signalperiod=9)

    # verifico se estou comprado
    position = trade_service.retrieve_position_for_a_company_and_a_strategy(company_code, 'macd')

    # se estou comprado, verifico signal
    #   se está positivo, mantenho
    #   se está negativo, vendo, estou é, ponho no banco de dados
    # se não estou comprado, verifico sinal
    #   se está positivo, compro
    #   se não está positivo, mantenho

    return None
