import src.repository.company_repository as company_repository


def retrieve_position_for_a_company_and_a_strategy(company_code, strategy):
    last_order = company_repository.retrieve_last_order_for_company_and_strategy(company_code, strategy)

    if not last_order:
        return 'NOT_POSITIONED'

    return 'NOT_POSITIONED' if last_order['order'] == 'VENDA' else 'HAVE_BOUGHT'
