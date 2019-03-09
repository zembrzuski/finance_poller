import src.config.local as config
import src.service.yahoo_poller as yahoo_poller


def main():
    companies_chunks = [
        config.companies[x:x + config.chunk_size]
        for x in range(0, len(config.companies), config.chunk_size)]

    list(map(lambda chunk: yahoo_poller.realtime_chunk_importer(chunk), companies_chunks))


if __name__ == '__main__':
    main()
