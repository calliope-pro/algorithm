# ABC283-D
# 問題とテストケースが分かりにくい。
# 全体の文字を司る集合と各区間の文字を司る集合を上手く管理する
# ')'のとき消す区間の文字の集合は、後入れ先出しなので、stackが使える
import sys
import queue

rr = lambda: sys.stdin.readline().rstrip()

s = rr()
stack = queue.LifoQueue()
stack.put(set())
c_set = set()
for i, c in enumerate(s):
    if c == '(':
        stack.put(set())
        continue
    if c == ')':
        if stack.empty():
            print('No')
            exit()
        c_set_ = stack.get()
        c_set -= c_set_
        continue
    if c in c_set:
        print('No')
        exit()
    else:
        c_set.add(c)
        c_set_ = stack.get()
        c_set_.add(c)
        stack.put(c_set_)
else:
    if stack.qsize() == 1:
        print('Yes')
    else:
        print('No')
