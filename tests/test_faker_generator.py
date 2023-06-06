""" This file is responsible for faker_generator tests"""
from python_src.utils.faker_generator import generate_name, generate_address


def test_generate_name():
    """Method to test generation of names"""
    names = generate_name(3)
    assert len(names) == 3
    assert isinstance(names, list)
    assert isinstance(names[0], str)


def test_generate_addresses():
    """Method to test generation of addresses"""
    addresses = generate_address(3)
    assert len(addresses) == 3
    assert isinstance(addresses, list)
    assert isinstance(addresses[0], str)
