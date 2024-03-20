# ABC344-A
# 正規表現でゴリ押し
import re

print(re.sub(r"(.*)\|.*\|(.*)", r"\1\2", input()))
