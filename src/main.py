import src.config.local as config
import src.service.yahoo_realtime_poller as yahoo_poller
import src.service.yahoo_historical_importer as historical_importer

def main():
    companies_chunks = [
        config.companies[x:x + config.chunk_size]
        for x in range(0, len(config.companies), config.chunk_size)]

    # do realtime importer
    # list(map(lambda chunk: yahoo_poller.realtime_chunk_importer(chunk), companies_chunks))

    # result = historical_importer.import_historical_data(companies_chunks)

    # my near real time processing.
    # for a given company, say PETR4.SA
    # read historical data from disk
    # append today's price
    # compute indicators
    # apply rule to buy or sell

    print('ae')


if __name__ == '__main__':
    main()
