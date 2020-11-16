import pytest
from address import Address

def test_constructor():
    address = Address('123 main street', 'Los Angeles', 'CA', '12345')
    assert isinstance(address, Address)

def test_street_getter():
    address = Address('123 main street', 'Los Angeles', 'CA', '12345')
    result = address.street
    expected = '123 main street'
    assert result == expected

def test_street_setter():
    address = Address('123 main street', 'Los Angeles', 'CA', '12345')
    address.street = '456 2nd street'
    result = address.street
    expected = '456 2nd street'
    assert result == expected

def test_city_getter():
    address = Address('123 main street', 'Los Angeles', 'CA', '12345')
    result = address.city
    expected = 'Los Angeles'
    assert result == expected

def test_city_setter():
    address = Address('123 main street', 'Los Angeles', 'CA', '12345')
    address.city = 'Irvine'
    result = address.city
    expected = 'Irvine'
    assert result == expected

def test_state_getter():
    address = Address('123 main street', 'Los Angeles', 'CA', '12345')
    result = address.state
    expected = 'CA'
    assert result == expected

def test_state_setter():
    address = Address('123 main street', 'Los Angeles', 'CA', '12345')
    address.state = 'AZ'
    result = address.state
    expected = 'AZ'
    assert result == expected

def test_zipcode_getter():
    address = Address('123 main street', 'Los Angeles', 'CA', '12345')
    result = address.zipcode
    expected = '12345'
    assert result == expected

def test_zipcode_setter():
    address = Address('123 main street', 'Los Angeles', 'CA', '12345')
    address.zipcode = '90000'
    result = address.zipcode
    expected = '90000'
    assert result == expected

def test_to_string():
    address = Address('123 main street', 'Los Angeles', 'CA', '12345')
    result = address.to_string()
    expected = '123 main street, Los Angeles, CA, 12345'
    assert result == expected

def test_to_string_wo_zip():
    address = Address('123 main street', 'Los Angeles', 'CA', '12345')
    result = address.to_string_wo_zip()
    expected = '123 main street, Los Angeles, CA'
    assert result == expected