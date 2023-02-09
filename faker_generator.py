""" This module is responsible for creating fake data"""
from faker import Faker

"""
    Faker generator module

        Methods:
            - generate_name()                   - responsible for creating fake names
            - generate_addresses()              - responsible for creating fake addresses
            
"""


def generate_name(numbers_of_data: int) -> list[str]:
    """ Create a fake names"""
    faker = Faker('PL')
    list_with_names = [faker.first_name() + ' ' + faker.last_name() for _ in range(numbers_of_data)]

    return list_with_names


def generate_address(numbers_of_data: int) -> list[str]:
    """ Create a fake address"""
    faker = Faker('PL')
    list_with_addresses = []
    addresses = [faker.address() for _ in range(numbers_of_data)]
    for item in addresses:
        list_with_addresses.append(item.replace("\n", ", "))

    return list_with_addresses
