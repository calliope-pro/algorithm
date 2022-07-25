from itertools import *
iterable1 = [3, 4, 6, 2, 1, 9, 0, 7, 5, 8]
iterable2 = list(range(2)) * 2
iterable3 = list(range(4, 10))
iterable4 = [2, 2, 1, 2, 3, 5, 5, 5, 8, 9, 1, 1]
iterable5 = list(range(3))
label = [0, False, True, 1, 0, 1]


# accumulate
print(list(accumulate(iterable1))) # 累積和
print(list(accumulate(iterable1, func=max))) # max関数を累積的に処理


# chain, chain.from_iterable
print(list(chain(iterable2, iterable3))) # 複数のiterable objectを引数として取る。
print(list(chain.from_iterable([iterable2, iterable3]))) # iterable objectを引数として取り、次元を1つ減らす（平坦化）したiterable objectを返す。

# combinations, combinations_with_replacement
print(list(combinations(iterable2, 2))) # 見ての通り組み合わせ
print(list(combinations_with_replacement(iterable5, 3))) # 自身を複数回含める組み合わせ


# compress
print(list(compress(iterable3, label))) # iterable objectでlabelのTrueに適合するものを返す。


# takewhile, dropwhile
print(list(dropwhile(lambda x: x<6, iterable1))) # 最初にFalseを返した位置以降
print(list(takewhile(lambda x: x<6, iterable1))) # 最初にFalseを返した位置より前


# groupby
print([[key, list(value)] for key, value in groupby(iterable4, key=lambda x: x%2)]) # 貪欲的グループ化,valueはitertools._grouper objectで返される。


# permutations
print(list(permutations(iterable2, 2))) # 順列


# product
print(list(product(iterable5, repeat=2))) # 直積、デカルト積、3進法である。
print(list(product(iterable3, iterable5, repeat=2))) # iterable3, iterable5, iterable3, iterable5のデカルト積


# zip_longest
print([(a, b) for a, b in zip_longest(iterable2, iterable3, fillvalue=500)]) # zipとの違い:長さが長いiterable objectに合わせる。未定要素をfillvalueで指定可能。


    



















