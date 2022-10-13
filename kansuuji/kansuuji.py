import math
import re
from typing import Union

import mojimoji

from .utils import (
    KANJI_DIGIT_DICT,
    KANJI_NUMBER_DICT,
    KANJI_SMALL_DIGIT_DICT,
    NUMBER_SET,
    SMALL_DIGIT_SET,
    KANJI_DIGIT_SET,
    PATTERN_SYMBOLS,
    PATTERN_LEFT_VALUE,
    PATTERN_KANSUUJI_OR_DIGIT,
    fix_typo,
    PATTERN_ALL_CHARS
)

def kanji2int(kanjis: Union[str, int], remove_typo=False) -> int:

    if isinstance(kanjis, int): return kanjis
    if not isinstance(kanjis, str): raise ValueError('Unsupported Data Type')
    if remove_typo:
        kanjis = ''.join(map(fix_typo, kanjis))
    # normalization
    kanjis = mojimoji.zen_to_han(kanjis, kana=False)

    if PATTERN_ALL_CHARS.search(kanjis):
        raise ValueError()
    kanjis = PATTERN_SYMBOLS.sub('', kanjis)

    if len(kanjis) == 1:
        if kanjis in NUMBER_SET:
            return KANJI_NUMBER_DICT[kanjis]
        if kanjis in SMALL_DIGIT_SET:
            return 10**KANJI_SMALL_DIGIT_DICT[kanjis]
        if kanjis in KANJI_DIGIT_SET:
            return 10**KANJI_DIGIT_DICT[kanjis]

    result = 0
    if any(str.isdigit(moji) for moji in kanjis):
        # 入力に数字が含まれている場合
        value = 0
        while kanjis:
            left_value = PATTERN_LEFT_VALUE.search(kanjis)
            current, float_number, small_digit, kanjis = left_value.groups()
            current = int(current or 1)
            if float_number:
                current += float(float_number)
            if small_digit:
                current *= 10**KANJI_SMALL_DIGIT_DICT[small_digit]
            value += current

            head = re.match(rf'{"|".join(KANJI_DIGIT_SET)}', kanjis)
            if not kanjis or head:
                digit = head.group(0) if kanjis else ''
                result += value * 10 ** KANJI_DIGIT_DICT.get(digit, 0)
                value = 0
                kanjis = kanjis[len(digit):]
            print(kanjis)
        return int(result)
    else:
        current_num_min, current_num = 0, 0
        for kansuuji in PATTERN_KANSUUJI_OR_DIGIT.findall(kanjis):
            if kansuuji in NUMBER_SET:
                current_num_min = KANJI_NUMBER_DICT[kansuuji]
            elif kansuuji in SMALL_DIGIT_SET:
                current_num += (current_num_min if current_num_min else 1) * 10**KANJI_SMALL_DIGIT_DICT[kansuuji]
                current_num_min = 0
            elif kansuuji in KANJI_DIGIT_SET:
                result += (current_num + current_num_min) * 10**KANJI_DIGIT_DICT[kansuuji]
                current_num = current_num_min = 0

    return result + current_num + current_num_min

    raise Exception('NOT implemented !')