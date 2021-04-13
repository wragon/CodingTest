import sys
input = sys.stdin.readline  #input보다 좀 더 빠름

A, B, K = map(int, input().split())
dack = 0
temp = A+B-K
if temp < 5:
    dack = 0
else:
    dack = temp // 5
    
print(dack)

