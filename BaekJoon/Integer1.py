#%% #1037
import sys
input = sys.stdin.readline  #input보다 좀 더 빠름

N = int(input())
A = 0
divisor = list(map(int, input().split()))
A_max = max(divisor)
A_min = min(divisor)
A = A_max * A_min
print(A)