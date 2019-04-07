import src.config.local as config
import src.service.yahoo_realtime_poller as yahoo_poller
import src.service.yahoo_historical_importer as historical_importer
import src.service.real_time_polling as real_time_polling


def main():
    companies_chunks = [
        config.companies[x:x + config.chunk_size]
        for x in range(0, len(config.companies), config.chunk_size)]

    """
    # do import historical data
    # devo rodar esse cara em todas as manhãs, antes de iniciar o pregão.
    """
    # result = historical_importer.import_historical_data(companies_chunks)

    """
    # do realtime importer
    # fazer isso periodicamente ao longo do dia. tipo de 10 em 10 minutos. apos executar isso,
    # estou apto a fazer minha bl
    """
    # list(map(lambda chunk: yahoo_poller.realtime_chunk_importer(chunk), companies_chunks))

    """
    # essa aqui é a lógica em si.
    """
    for chunk in companies_chunks:
        for company in chunk:
            real_time_polling.do_polling(company)

    print('ae')


if __name__ == '__main__':
    main()
