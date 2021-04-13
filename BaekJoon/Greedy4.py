#%% #11399
import sys
input = sys.stdin.readline  #input보다 좀 더 빠름

N = int(input())
P = list(map(int, input().split()))

P = sorted(P)
sum = 0
time = 0
for i in range(N):
    sum += P[i]
    time += sum

print(time)