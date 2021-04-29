#1021
import sys
from collections import deque
input = sys.stdin.readline  #input보다 좀 더 빠름

N, M = map(int, input().split())
vote = list(map(int, input().split()))
que = deque(list(map(int, range(1, N+1))))
count = 0

for num in vote:
    while(1):
        if num == que[0]:
            que.popleft()
            break
        else:
            if que.index(num) <= (len(que)//2):
                que.rotate(-1)
                count += 1
            else:
                que.rotate(1)
                count += 1  

print(count)