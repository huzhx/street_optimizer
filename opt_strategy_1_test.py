import pytest
from opt_strategy_1 import OptimizationStrategy1
from address import Address

def test_mask_address1():
    os1 = OptimizationStrategy1()
    address = Address('1', '1234 Astor Ave', 'Ann Arbor','MI', '48105')
    result = os1.mask_address(address).to_string()
    expected = '1, 1230 Astor Ave, Ann Arbor, MI, 48105'
    assert result == expected

def test_mask_address2():
    os1 = OptimizationStrategy1()
    address = Address('1', '  1510 124th Street ', 'Los Angeles','CA', '90047')
    result = os1.mask_address(address).to_string()
    expected = '1, 1515 124Th Street, Los Angeles, CA, 90047'
    assert result == expected

def test_mask_address3():
    os1 = OptimizationStrategy1()
    address = Address('1', '1510 124th Street Apt 123', 'Los Angeles','CA', '90047')
    result = os1.mask_address(address).to_string()
    expected = '1, 1515 124Th Street, Los Angeles, CA, 90047'
    assert result == expected

def test_mask_address4():
    os1 = OptimizationStrategy1()
    address = Address('1', '1510 124th Street Apt123', 'Los Angeles','CA', '90047')
    result = os1.mask_address(address).to_string()
    expected = '1, 1515 124Th Street, Los Angeles, CA, 90047'
    assert result == expected

def test_mask_address5():
    os1 = OptimizationStrategy1()
    address = Address('1', '1510 124th 123', 'Los Angeles','CA', '90047')
    result = os1.mask_address(address).to_string()
    expected = '1, 1515 124Th, Los Angeles, CA, 90047'
    assert result == expected

def test_get_opt_address1():
    os1 = OptimizationStrategy1()
    address = Address('1', '1234 Astor Ave', 'Ann Arbor','MI', '48105')
    result = os1.get_opt_address(address)
    expected = Address('1', '1234 ASTOR DR', 'ANN ARBOR', 'MI', '48104')
    assert result == expected

def test_get_opt_address2():
    os1 = OptimizationStrategy1()
    address = Address('1', '1234 A', 'Ann Arbor','MI', '48105')
    result = os1.get_opt_address(address)
    expected = None
    assert result is None

def test_get_opt_address3():
    os1 = OptimizationStrategy1()
    address = Address('1', '1510 124th Street', 'Los Angeles','CA', '90047')
    result = os1.get_opt_address(address)
    expected = Address('1', '1510 W 124TH ST', 'LOS ANGELES', 'CA', '90047')
    assert result == expected

def test_get_opt_address4():
    os1 = OptimizationStrategy1()
    address = Address('1', '1510 124th Street Apt 123', 'Los Angeles','CA', '90047')
    result = os1.get_opt_address(address)
    expected = Address('1', '1510 W 124TH ST', 'LOS ANGELES', 'CA', '90047')
    assert result == expected