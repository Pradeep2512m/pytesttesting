import Calculator
import pytest

@pytest.mark.parametrize("a,b,c",[(1,2,3),(4,5,6),(7,8,9)])
def test_add2no(a,b,c):

    result=Calculator.add2no(a, b)
    assert result == c


@pytest.mark.parametrize("a,b,c",[(1,2,3),(4,12,6),(7,14,9)])
def test_sub2no(a,b,c):

    result=Calculator.sub2no(a, b)
    assert result == c


@pytest.mark.parametrize("a,b,c",[(1,2,3),(4,5,6),(7,8,9),(14,12,55)])
def test_mul2no(a,b,c):

    result=Calculator.mul2no(a, b)
    assert result == c

@pytest.mark.parametrize("a,b,c",[(1,2,3),(4,5,6),(7,8,9)])
def test_div2no(a,b,c):

    result=Calculator.div2no(a, b)
    assert result == c