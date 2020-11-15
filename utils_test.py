from utils import shift_num

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