""" This module is responsible for creating fake data"""
from faker import Faker


def generate_name(numbers_of_data: int) -> str:
    """ Create a fake names"""
    faker = Faker('PL')
    list_with_names = []
    names = ','.join(f'{faker.name()}' for _ in range(0, numbers_of_data))
    split_names = names.split(',')
    for item in split_names:
        names_without_mr_and_mrs = item.lstrip('pani ')
        list_with_names.append(names_without_mr_and_mrs)

    return list_with_names


def generate_address(numbers_of_data: int) -> str:
    """ Create a fake address"""
    faker = Faker('PL')
    list_with_addresses = []
    names = ','.join(f'{faker.address()}' for _ in range(0, numbers_of_data))
    split_names = names.split(',')
    for item in split_names:
        list_with_addresses.append(item.replace("\n", ", "))

    return list_with_addresses


generate_name(3)
generate_address(2)
