import pytest

from kansuuji import kanji2int



@pytest.mark.parametrize('kanjis, expect', [
    ('零', 0), ('一', 1), ('二', 2), ('三', 3), ('四', 4), ('五', 5), ('六', 6), ('七', 7), ('八', 8), ('九', 9),
    ('〇', 0), ('壱', 1), ('弐', 2), ('参', 3), ('肆', 4), ('伍', 5), ('陸', 6), ('漆', 7), ('捌', 8), ('玖', 9),
    ('十', 10), ('拾', 10), ('什', 10), ('百', 100), ('佰', 100), ('千', 1000), ('仟', 1000), ('阡', 1000),
    ('万', 10_000), ('萬', 10_000)
])
def test_kanji2int_1(kanjis, expect):
    """1文字の漢数字のパース"""
    assert kanji2int(kanjis=kanjis) == expect

@pytest.mark.parametrize('kanjis, expect',[
    ('十一', 11), ('二十一', 21), ('百十一', 111), ('百二十一', 121), ('二百十一', 211), ('六百三十四', 634),
    ('二千二十二', 2022), ('一億二千七百五十万', 127_500_000), ('1.5億', 150_000_000)
])
def test_kanji2int_2(kanjis, expect):
    """複数文字の漢数字のパース"""
    output = kanji2int(kanjis=kanjis)
    assert output == expect

@pytest.mark.parametrize('kanjis, expect',[
    ('1千', 1000), ('肆千', 4_000), ('壱万', 10_000), ('10万', 100_000), ('1億2800万', 128_000_000), ('1億2,800万', 128_000_000)
])
def test_kanji2int_3(kanjis, expect):
    assert kanji2int(kanjis=kanjis) == expect