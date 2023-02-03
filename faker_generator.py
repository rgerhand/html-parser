""" This module is responsible for creating fake data"""
from faker import Faker

"""
    Faker generator module

        Methods:
            - generate_name()                   - responsible for creating fake names
            - generate_addresses()              - responsible for creating fake addresses
            
"""


def generate_name(numbers_of_data: int) -> list:
    """ Create a fake names"""
    faker = Faker('PL')
    list_with_names = []
    names = ','.join(f'{faker.name()}' for _ in range(0, numbers_of_data))
    split_names = names.split(',')
    for item in split_names:
        names_without_mr_and_mrs = item.lstrip('pani ')
        list_with_names.append(names_without_mr_and_mrs)

    return list_with_names


def generate_address(numbers_of_data: int) -> list:
    """ Create a fake address"""
    faker = Faker('PL')
    list_with_addresses = []
    names = ','.join(f'{faker.address()}' for _ in range(0, numbers_of_data))
    split_names = names.split(',')
    for item in split_names:
        list_with_addresses.append(item.replace("\n", ", "))

    return list_with_addresses
