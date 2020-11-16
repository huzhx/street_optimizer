from utils import shift_num, remove_num

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