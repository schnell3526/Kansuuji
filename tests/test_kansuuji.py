from kansuuji.kansuuji import *

def test_kanji2int():
    kanji = '一'
    expect = '1'
    assert kanji2int(kanji=kanji) == expect