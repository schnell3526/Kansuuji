import pytest

from kansuuji.kansuuji import *

@pytest.mark.parametrize('kanji, expect', [
    ('零', 0), ('一', 1), ('二', 2), ('三', 3), ('四', 4), ('五', 5), ('六', 6), ('七', 7), ('八', 8), ('九', 9),
    ('〇', 0), ('壱', 1), ('弐', 2), ('参', 3), ('肆', 4), ('伍', 5), ('陸', 6), ('漆', 7), ('捌', 8), ('玖', 9),
])
def test_kanji2int(kanji, expect):
    assert kanji2int(kanji=kanji) == expect