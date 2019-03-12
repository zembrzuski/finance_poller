import src.repository.company_repository as company_repository


def retrieve_position_for_a_company(company_code):
    last_order_1 = company_repository.retrieve_last_order(company_code)

    if len(last_order_1) == 0:
        return 'NOT_POSITIONED'

    last_order = last_order_1[0]

    return 'NOT_POSITIONED' if last_order['ORDER'] == 'SELL' else 'HAVE_BOUGHT'
