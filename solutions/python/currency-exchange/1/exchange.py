"""
Functions for calculating steps in exchanging currency.

Python numbers documentation: 
https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

Overview of exchanging currency when traveling: 
https://www.compareremit.com/money-transfer-tips/guide-to-exchanging-currency-for-overseas-travel/
"""

def exchange_money(budget: float, exchange_rate: float) -> float:
    """
    Calculate the amount of foreign currency you will receive from a given budget.

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency (rate to convert 1 of your currency).
    :return: float - amount of foreign currency you can receive.
    """
    return budget / exchange_rate


def get_change(budget: float, exchanging_value: float) -> float:
    """
    Calculate the remaining amount of your currency after exchanging a portion of it.

    :param budget: float - amount of money you have.
    :param exchanging_value: float - amount of money you want to exchange.
    :return: float - remaining amount of your starting currency after exchanging.
    """
    return budget - exchanging_value


def get_value_of_bills(denomination: int, number_of_bills: int) -> int:
    """
    Calculate the total value of a given number of bills of a certain denomination.

    :param denomination: int - the value of a single bill.
    :param number_of_bills: int - total number of bills.
    :return: int - calculated total value of the bills.
    """
    return denomination * number_of_bills


def get_number_of_bills(amount: float, denomination: int) -> int:
    """
    Calculate the number of bills you can get from a given amount of money.

    :param amount: float - the total amount of money.
    :param denomination: int - the value of a single bill.
    :return: int - number of whole bills that can be obtained from the amount.
    """
    return int(amount // denomination)


def get_leftover_of_bills(amount: float, denomination: int) -> float:
    """
    Calculate the leftover amount after dividing the total amount into bills of a certain denomination.

    :param amount: float - the total amount of money.
    :param denomination: int - the value of a single bill.
    :return: float - amount that is left over after obtaining whole bills.
    """
    return amount % denomination


def exchangeable_value(budget: float, exchange_rate: float, spread: int, denomination: int) -> int:
    """
    Calculate the maximum exchangeable value based on the budget, exchange rate, and spread,
    considering that the result must be a multiple of the denomination.

    :param budget: float - the amount of money you want to exchange.
    :param exchange_rate: float - the unit value of the foreign currency (rate to convert 1 of your currency).
    :param spread: int - percentage fee charged on the exchange (spread).
    :param denomination: int - the value of a single bill.
    :return: int - the maximum value of foreign currency that can be obtained in whole bills.
    """
    adjusted_rate = exchange_rate * (1 + spread / 100)
    exchanged_amount = budget / adjusted_rate
    return get_number_of_bills(exchanged_amount, denomination) * denomination
