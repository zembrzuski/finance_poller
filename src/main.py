import src.config.local as config
import src.service.yahoo_realtime_poller as yahoo_poller
import src.service.yahoo_historical_importer as historical_importer

def main():
    companies_chunks = [
        config.companies[x:x + config.chunk_size]
        for x in range(0, len(config.companies), config.chunk_size)]

    # do realtime importer
    # list(map(lambda chunk: yahoo_poller.realtime_chunk_importer(chunk), companies_chunks))

    print('visit this site, please: \n https://finance.yahoo.com/quote/PETR4.SA?p=PETR4.SA&.tsrc=fin-srch')
    print('click historical data')
    print('click apply')
    print('click download data')
    print('at network inspection console, look for PETR4.SA?period1=XXXXXXXXXXXXXXXX')
    from_epoch = 1262311200
    to_epoch = 1893463200
    crumb = input('then, type the crumb property on the request address. It is something like U4e8eDQi/yI\n')
    cookie = input('the, type the cookie parameter (look on the headers of the request)\n')

    list(map(
        lambda companies: historical_importer.import_chunks_historical(companies, from_epoch, to_epoch, crumb, cookie),
        companies_chunks))

    print('finished')


if __name__ == '__main__':
    main()
