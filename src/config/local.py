
# company_code, from_epoch, to_epoch, crumb
yahoo_historical_url = \
    'https://query1.finance.yahoo.com/v7/finance/download/{}?period1={}&period2={}&interval=1d&events=history&crumb={}'

yahoo_url_for_polling = "https://query1.finance.yahoo.com/v7/finance/quote?formatted=true&crumb=U4e8eDQi%2FyI&" \
                        "lang=en-US&region=US&symbols=" \
                        "{}" \
                        "&fields=messageBoardId%2ClongName%2CshortName%2CmarketCap%2CunderlyingSymbol%2CunderlyingExchangeSymbol%2CheadSymbolAsString%2CregularMarketPrice%2CregularMarketChange%2CregularMarketChangePercent%2CregularMarketVolume%2Cuuid%2CregularMarketOpen%2CfiftyTwoWeekLow%2CfiftyTwoWeekHigh&corsDomain=finance.yahoo.com"

companies = ["ABEV3.SA",
             "B3SA3.SA",
             "BBAS3.SA",
             "BBDC3.SA",
             "BBDC4.SA",
             "BBSE3.SA",
             "BRAP4.SA",
             "BRDT3.SA",
             "BRFS3.SA",
             "BRKM5.SA",
             "BRML3.SA",
             "BTOW3.SA",
             "CCRO3.SA",
             "CIEL3.SA",
             "CMIG4.SA",
             "CSAN3.SA",
             "CSNA3.SA",
             "CVCB3.SA",
             "CYRE3.SA",
             "ECOR3.SA",
             "EGIE3.SA",
             "ELET3.SA",
             "ELET6.SA",
             "EMBR3.SA",
             "ENBR3.SA",
             "EQTL3.SA",
             "ESTC3.SA",
             "FLRY3.SA",
             "GGBR4.SA",
             "GOAU4.SA",
             "GOLL4.SA",
             "HYPE3.SA",
             "IGTA3.SA",
             "ITSA4.SA",
             "ITUB4.SA",
             "JBSS3.SA",
             "KLBN11.SA",
             "KROT3.SA",
             "LAME4.SA",
             "LOGG3.SA",
             "LREN3.SA",
             "MGLU3.SA",
             "MRFG3.SA",
             "MRVE3.SA",
             "MULT3.SA",
             "NATU3.SA",
             "PCAR4.SA",
             "PETR3.SA",
             "PETR4.SA",
             "QUAL3.SA",
             "RADL3.SA",
             "RAIL3.SA",
             "RENT3.SA",
             "SANB11.SA",
             "SBSP3.SA",
             "SMLS3.SA",
             "SUZB3.SA",
             "TAEE11.SA",
             "TIMP3.SA",
             "UGPA3.SA",
             "USIM5.SA",
             "VALE3.SA",
             "VIVT4.SA",
             "VVAR3.SA",
             "WEGE3.SA"]

elasticsearch_address = 'http://localhost:9200'

chunk_size = 10

