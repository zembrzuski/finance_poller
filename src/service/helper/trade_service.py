import src.repository.company_repository as company_repository
import src.service.order_communication_service as order_communication_service

def retrieve_position_for_a_company_and_a_strategy(company_code, strategy):
    last_order = company_repository.retrieve_last_order_for_company_and_strategy(company_code, strategy)

    if not last_order:
        return 'NOT_POSITIONED'

    return 'NOT_POSITIONED' if last_order['order'] == 'VENDA' else 'HAVE_BOUGHT'


def execute_order(company_code, date, price, order, strategy, some_info):
    result = company_repository.persist_an_order(company_code, strategy, price, date, order)
    order_communication_service.do_communication(company_code, date, price, order, strategy, some_info)

    return True
