# PAST003-D
# 愚直に書いたクソコード
# 0~9に対して2次元配列が合致するか2重ループ使う方が楽(どっちにしろ無駄にだるい)
# 特徴見抜いて軽量化できるけど。。。。。。
import sys

rr = lambda: sys.stdin.readline().rstrip()
ri = lambda: int(sys.stdin.readline())

n = ri()
board = [rr() for _ in range(5)]
ans = ''
for i in range(1, 4*n+1, 4):
    board_pattern = [board[idx][i:i+3] for idx in range(5)]
    if board_pattern == [
        '###',
        '#.#',
        '#.#',
        '#.#',
        '###',
    ]:
        ans += '0'
    if board_pattern == [
        '.#.',
        '##.',
        '.#.',
        '.#.',
        '###',
    ]:
        ans += '1'
    if board_pattern == [
        '###',
        '..#',
        '###',
        '#..',
        '###',
    ]:
        ans += '2'
    if board_pattern == [
        '###',
        '..#',
        '###',
        '..#',
        '###',
    ]:
        ans += '3'
    if board_pattern == [
        '#.#',
        '#.#',
        '###',
        '..#',
        '..#',
    ]:
        ans += '4'
    if board_pattern == [
        '###',
        '#..',
        '###',
        '..#',
        '###',
    ]:
        ans += '5'
    if board_pattern == [
        '###',
        '#..',
        '###',
        '#.#',
        '###',
    ]:
        ans += '6'
    if board_pattern == [
        '###',
        '..#',
        '..#',
        '..#',
        '..#',
    ]:
        ans += '7'
    if board_pattern == [
        '###',
        '#.#',
        '###',
        '#.#',
        '###',
    ]:
        ans += '8'
    if board_pattern == [
        '###',
        '#.#',
        '###',
        '..#',
        '###',
    ]:
        ans += '9'
print(ans)
