import src.config.local as config
import src.service.yahoo_realtime_poller as yahoo_poller
import src.service.yahoo_historical_importer as historical_importer
import src.service.real_time_polling as real_time_polling


def main():
    companies_chunks = [
        config.companies[x:x + config.chunk_size]
        for x in range(0, len(config.companies), config.chunk_size)]

    # do realtime importer
    # list(map(lambda chunk: yahoo_poller.realtime_chunk_importer(chunk), companies_chunks))

    # do import historical data
    # result = historical_importer.import_historical_data(companies_chunks)

    real_time_polling.do_polling('PETR4.SA')

    print('ae')


if __name__ == '__main__':
    main()
