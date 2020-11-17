from os import path, remove
import csv
from address_optimizer import AddressOptimizer
from opt_strategy_1 import OptimizationStrategy1
from address import Address

def test_strategy_getter():
    os1 = OptimizationStrategy1()
    org_addresses = []
    address1 = Address('1', '40 MILLGROVE', 'Irvine','CA', '')
    address2 = Address('2', '10 HIDDEN BROOK', 'Irvine','CA', '')
    org_addresses.append(address1)
    org_addresses.append(address2)
    ao = AddressOptimizer(org_addresses, os1)
    result = ao.strategy
    expected = os1
    assert result == expected

def test_process_addresses1():
    os1 = OptimizationStrategy1()
    org_addresses = []
    address1 = Address('1', '40 MILLGROVE', 'Irvine','CA', '')
    address2 = Address('2', '10 HIDDEN BROOK', 'Irvine','CA', '')
    org_addresses.extend([address1, address2])
    ao = AddressOptimizer(org_addresses, os1)
    ao.process_addresses()
    result = ao.opt_addresses
    expected = []
    address1_ = Address('1', '40 MILLGROVE', 'IRVINE', 'CA', '92602') 
    address2_ = Address('2', '10 HIDDEN BRK', 'IRVINE', 'CA', '92602')
    expected.extend([address1_, address2_])
    assert result == expected

def test_process_addresses2():
    os1 = OptimizationStrategy1()
    org_addresses = []
    address1 = Address('1', '40 MILLGROVE', 'Irvine','CA', '')
    address2 = Address('2', '10 HIDDEN BROOK', 'Irvine','CA', '')
    org_addresses.extend([address1, address2])
    ao = AddressOptimizer(org_addresses, os1)
    ao.process_addresses()
    result = ao.opt_addresses
    expected = []
    address1_ = Address('1', '40 MILLGROV', 'IRVINE', 'CA', '92602') 
    address2_ = Address('2', '10 HIDDEN BRK', 'IRVINE', 'CA', '92602')
    expected.extend([address1_, address2_])
    assert result != expected

def test_opt_to_csv():
    os1 = OptimizationStrategy1()
    org_addresses = []
    address1 = Address('1', '40 MILLGROVE', 'Irvine','CA', '')
    address2 = Address('2', '10 HIDDEN BROOK', 'Irvine','CA', '')
    org_addresses.extend([address1, address2])
    ao = AddressOptimizer(org_addresses, os1)
    ao.process_addresses()
    file_path = 'test.csv'
    if (path.exists(file_path)):
        remove(file_path)
    ao.opt_to_csv(file_path)
    result = []
    with open(file_path) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            result.append(row)
    expected = []
    address1_ = Address('1', '40 MILLGROVE', 'IRVINE', 'CA', '92602') 
    address2_ = Address('2', '10 HIDDEN BRK', 'IRVINE', 'CA', '92602')
    expected.append([address1_.id, address1_.street, address1_.city, address1_.state, address1_.zipcode]) 
    expected.append([address2_.id, address2_.street, address2_.city, address2_.state, address2_.zipcode]) 
    assert result == expected
