# kansuuji
漢数字を含む文字列をint型へ変換する。

```python
from kansuuji import kanji2int

print(kanji2int('六百三十四'))
# 634
print(kanji2int('一億二千七百五十万'))
# 127500000
print(kanji2int('1.5億'))
# 150000000
print(kanji2int('197億9,200万円'))

# typoも考慮して変換できる。
print(kanji2int('1憶'))
# 100000000
```

## How to install

### for users
```shell
git clone git@github.com:schnell3526/Kansuuji.git
cd Kansuuji
pip install .
```

## for developers
```shell
git clone git@github.com:schnell3526/Kansuuji.git
cd Kansuuji
poetry install
```

run tests
```shell
pytest
```
