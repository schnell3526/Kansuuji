import re

KANJI_NUMBER_DICT = {
    "零": 0, "一": 1, "二": 2, "三": 3, "四": 4, "五": 5, "六": 6, "七": 7, "八": 8, "九": 9,
    "〇": 0, "壱": 1, "弐": 2, "参": 3, "肆": 4, "伍": 5, "陸": 6, "漆": 7, "捌": 8, "玖": 9
}
KANJI_SMALL_DIGIT_DICT = {"十": 1, "拾": 1, "什": 1, "百": 2, "佰": 2, "千": 3, "阡": 3, "仟": 3}
KANJI_DIGIT_DICT = {
    "万": 4, "萬": 4, "億": 8, "兆": 12, "京": 16, "垓": 20, "𥝱": 24, "穣": 28, "溝": 32, "澗": 36, "正": 40,
    "載": 44, "極": 48, "恒河沙": 52, "阿僧祇": 56, "那由多": 60, "不可思議": 64, "無量大数": 68
}

PULAR_TYPO = {
    '憶': '億'
}

NUMBER_SET = set(KANJI_NUMBER_DICT)
SMALL_DIGIT_SET = set(KANJI_SMALL_DIGIT_DICT)
KANJI_DIGIT_SET = set(KANJI_DIGIT_DICT)

PATTERN_KANSUUJI = re.compile(r'|'.join(NUMBER_SET | SMALL_DIGIT_SET | KANJI_DIGIT_SET))
PATTERN_DIGIT = re.compile(r'\d')
PATTERN_SYMBOLS = re.compile(r',')
PATTERN_LEFT_VALUE = re.compile(r'(^\d*)(\.\d+)?([千百十]?)(.*)')