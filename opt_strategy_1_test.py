import pytest
from opt_strategy_1 import OptimizationStrategy1
from address import Address

def test_mask_address():
    os1 = OptimizationStrategy1()
    address = Address('1234 Astor Ave', 'Ann Arbor','MI', '48105')
    result = os1.mask_address(address).to_string()
    expected = '1230 Astor Ave, Ann Arbor, MI, 48105'
    assert result == expected

def test_get_opt_address():
    os1 = OptimizationStrategy1()
    address = Address('1234 Astor Ave', 'Ann Arbor','MI', '48105')
    result = os1.get_opt_address(address)
    expected = '1230 ASTOR DR, ANN ARBOR, MI, 48104'
    assert result.upper() == expected.upper()
