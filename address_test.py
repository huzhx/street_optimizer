import pytest
from address import Address

def test_constructor():
    address = Address('123 main street', 'Los Angeles', 'CA', '12345')
    assert isinstance(address, Address)

def test_street_getter():
    address = Address('123 main street', 'Los Angeles', 'CA', '12345')
    result = address.street
    expected = '123 main street'.title()
    assert result == expected

def test_street_setter():
    address = Address('123 main street', 'Los Angeles', 'CA', '12345')
    address.street = '456 2nd street'
    result = address.street
    expected = '456 2nd street'.title()
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
    expected = '123 Main Street, Los Angeles, CA, 12345'
    assert result == expected

def test_to_string_wo_zip():
    address = Address('123 main street', 'Los Angeles', 'CA', '12345')
    result = address.to_string_wo_zip()
    expected = '123 Main Street, Los Angeles, CA'
    assert result == expected

def test_extract_street_num1():
    address = Address('', 'Los Angeles', 'CA', '12345')
    with pytest.raises(Exception):
        address.extract_street_num()

def test_extract_street_num2():
    address = Address(None, 'Los Angeles', 'CA', '12345')
    with pytest.raises(Exception):
        address.extract_street_num()

def test_extract_street_num3():
    address = Address('123 main street', 'Los Angeles', 'CA', '12345')
    result = address.extract_street_num()
    expected = ['123', 'main street'.title()]
    assert result == expected

def test_extract_street_num4():
    address = Address(' 123  main street ', 'Los Angeles', 'CA', '12345')
    result = address.extract_street_num()
    expected = ['123', 'main street'.title()]
    assert result == expected

def test_replace_street_num1():
    address = Address('123 main street', 'Los Angeles', 'CA', '12345')
    address.replace_street_num('456')
    result = address.street
    expected = '456 main street'.title()
    assert result == expected

def test_replace_street_num2():
    address = Address(' 123  main street ', 'Los Angeles', 'CA', '12345')
    address.replace_street_num('456')
    result = address.street
    expected = '456 main street'.title()
    assert result == expected

def test_replace_street_num3():
    address = Address(' ', 'Los Angeles', 'CA', '12345')
    with pytest.raises(Exception):
        address.replace_street_num('456')

def test_eq1():
    address1 = Address('123 main street', 'Los Angeles', 'CA', '12345')
    address2 = Address('123 main street', 'Los Angeles', 'CA', '12345')
    assert address1 == address2

def test_eq2():
    address1 = Address('123 main street', 'Los Angeles', 'CA', '12345')
    address2 = Address('23 main street', 'Los Angeles', 'CA', '12345')
    assert address1 != address2