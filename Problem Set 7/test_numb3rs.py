import pytest
from numb3rs import validate

def test_few():
    assert validate("1.2.3") == False

def test_many():
    assert validate("1.2.3.4.5") == False

def test_high():
    assert validate("290.222.345.1") == False

def test_low():
    assert validate("122.23.22.11") == True