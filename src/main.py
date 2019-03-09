import src.config.local as config
import src.service.yahoo_poller as yahoo_poller


def main():
    companies_chunks = [config.companies[x:x + 10] for x in range(0, len(config.companies), 10)]
    list(map(lambda chunk: yahoo_poller.realtime_chunk_importer(chunk), companies_chunks))


if __name__ == '__main__':
    main()
