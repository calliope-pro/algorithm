# ABC161-D
# queue
import queue
import sys
ri = lambda: int(sys.stdin.readline())
k = ri()
queue_ = queue.Queue()
for i in range(1, 10):
    queue_.put(i)
n = 1
while n < k:
    a = queue_.get()
    b = a%10
    a *= 10
    if b in range(1, 9):
        for i in range(-1, 2):
            queue_.put(a + b + i)
    elif b == 9:
        queue_.put(a + 8)
        queue_.put(a + 9)
    else:
        queue_.put(a)
        queue_.put(a + 1)
    n += 1
print(queue_.get())

# deque
import collections
import sys
ri = lambda: int(sys.stdin.readline())
k = ri()
deque = collections.deque(range(1, 10))
n = 1
while n < k:
    a = deque.popleft()
    b = a%10
    a *= 10
    if b in range(1, 9):
        for i in range(-1, 2):
            deque.append(a + b + i)
    elif b == 9:
        deque.append(a + 8)
        deque.append(a + 9)
    else:
        deque.append(a)
        deque.append(a + 1)
    n += 1
print(deque[0])
