import pytest

def test_methodA():
    print("This is method A")

@pytest.mark.skip
def test_methodB():
    print("This is method B")

@pytest.mark.xfail
def test_methodC():
    print("This is method C")

@pytest.mark.xfail
def test_methodD():
    print("This is method D")

def test_methodE():
    print("This is method E")