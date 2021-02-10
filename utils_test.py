import pytest
from utils import shift_num, remove_num, remove_after_street_info, consume_api, strip_apt_term, has_street_term, has_apt_term

def test_shift_num1():
    num = '1234'
    result = shift_num(num)
    expected = '1230'
    assert result == expected

def test_shift_num2():
    num = '1230'
    result = shift_num(num)
    expected = '1235'
    assert result == expected

def test_shift_num3():
    num = '1'
    result = shift_num(num)
    expected = '10'
    assert result == expected

def test_remove_num1():
    addr = '1st ave'
    result = remove_num(addr)
    expected = '1st ave'
    assert result == expected

def test_remove_num2():
    addr = '1st ave apt 123'
    result = remove_num(addr)
    expected = '1st ave apt'
    assert result == expected

def test_remove_num3():
    addr = '1st ave apt123'
    result = remove_num(addr)
    expected = '1st ave apt'
    assert result == expected

def test_remove_num4():
    addr = '1staveapt123'
    result = remove_num(addr)
    expected = '1staveapt'
    assert result == expected

def test_remove_num5():
    addr = '1 st ave apt123'
    result = remove_num(addr)
    expected = '1 st ave apt'
    assert result == expected

def test_remove_num6():
    addr = '1 st 3ave apt123'
    result = remove_num(addr)
    expected = '1 st 3ave apt'
    assert result == expected

def test_remove_num7():
    addr = '1 st 3ave 123 apt'
    result = remove_num(addr)
    expected = '1 st 3ave apt'
    assert result == expected 

def test_consume_api1():
    api_endpoint = 'https://geomap.ffiec.gov/FFIECGeocMap/GeocodeMap1.aspx/GetGeocodeData'
    payload = {}
    with pytest.raises(Exception):
        consume_api(api_endpoint, payload)

def test_consume_api2():
    api_endpoint = 'https://geomap.ffiec.gov/FFIECGeocMap/GeocodeMap1.aspx/GetGeocodeData'
    payload = {"sSingleLine": "1230 Astor Ave Ann Arbor Mi", "iCensusYear": "2020"}
    resp = consume_api(api_endpoint, payload)
    result = resp['d']['sMatchAddr']
    expected = '1230 ASTOR DR, ANN ARBOR, MI, 48104'
    assert result == expected

def test_strip_apt_term1():
    addr = '1st ave apt'
    result = strip_apt_term(addr)
    expected = '1st ave'
    assert result == expected

def test_strip_apt_term2():
    addr = '123 1st ave apt 123'
    result = strip_apt_term(addr)
    expected = '123 1st ave'
    assert result == expected

def test_strip_apt_term3():
    addr = '123 1st ave apt123'
    result = strip_apt_term(addr)
    expected = '123 1st ave'
    assert result == expected

def test_strip_apt_term4():
    addr = '123 1 st ave spc 123'
    result = strip_apt_term(addr)
    expected = '123 1 st ave'
    assert result == expected

def test_strip_apt_term5():
    addr = '123 1st ave no 123'
    result = strip_apt_term(addr)
    expected = '123 1st ave'
    assert result == expected

def test_strip_apt_term6():
    addr = '123 1st ave box 123'
    result = strip_apt_term(addr)
    expected = '123 1st ave'
    assert result == expected

def test_strip_apt_term7():
    addr = '123 1st cr unit 123'
    result = strip_apt_term(addr)
    expected = '123 1st cr'
    assert result == expected

def test_strip_apt_term8():
    addr = '123 1st dr unit a'
    result = strip_apt_term(addr)
    expected = '123 1st dr'
    assert result == expected

def test_strip_apt_term9():
    addr = '123 1 st apt 123'
    result = strip_apt_term(addr)
    expected = '123 1 st'
    assert result == expected

def test_strip_apt_term10():
    addr = '123 1st apt a'
    result = strip_apt_term(addr)
    expected = '123 1st'
    assert result == expected

def test_strip_apt_term11():
    addr = '123 aptline street apt 2'
    result = strip_apt_term(addr)
    expected = '123 aptline street'
    assert result == expected 

def test_strip_apt_term11():
    addr = '123 fline street apt 2'
    result = strip_apt_term(addr)
    expected = '123 fline street'
    assert result == expected 

def test_remove_after_street_info1():
    addr = '123 1st ave 123'
    result = remove_after_street_info(addr)
    expected = '123 1st ave'
    assert result == expected

def test_remove_after_street_info2():
    addr = '123 1st 123'
    result = remove_after_street_info(addr)
    expected = '123 1st 123'
    assert result == expected

def test_has_street_term1():
    addr = '123 1st 123'
    result = has_street_term(addr)
    expected = False
    assert result == expected

def test_has_street_term2():
    addr = '123 1st ave apt123'
    result = has_street_term(addr)
    expected = True
    assert result == expected

def test_has_apt_term1():
    addr = '123 1st 123'
    result = has_apt_term(addr)
    expected = False
    assert result == expected

def test_has_apt_term2():
    addr = '123 fline street apt 2'
    result = has_apt_term(addr)
    expected = True
    assert result == expected