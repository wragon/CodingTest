#2164
import sys
from collections import deque
input = sys.stdin.readline  #input보다 좀 더 빠름

N = int(input())
que = deque()

for i in range(N):
    que.append(i+1)

while len(que) > 1:
    que.popleft()
    que.append(que.popleft())

print(que[0])