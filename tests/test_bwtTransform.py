from bwtTransform import bwt, ibwt

def test_bwt():
    assert  bwt("banana")== "annbaa"

def test_ibwt():
    assert  ibwt("annbaa")== "banana"