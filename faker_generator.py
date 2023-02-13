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
    faker_inst = Faker('PL')
    list_with_names = [f'{faker_inst.first_name()} {faker_inst.last_name()}' for _ in range(numbers_of_data)]

    return list_with_names


def generate_address(numbers_of_data: int) -> list[str]:
    """ Create a fake addresses"""
    faker_inst = Faker('PL')
    list_with_addresses = [faker_inst.address().replace("\n", ", ") for _ in range(numbers_of_data)]

    return list_with_addresses
