import src.repository.filesystem_helper as filesystem_helper


def do_communication(company_code, date, price, order, strategy, some_info):
    order_message = '{}\t{}\t{}\t{}\t{}\t{}'.format(company_code, date, price, order, strategy, some_info)

    filesystem_helper.persist_on_disk_an_order(order_message)

    print('ORDEM EFETUADA === {}'.format(order_message))
