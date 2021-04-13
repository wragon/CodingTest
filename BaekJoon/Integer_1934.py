#%% #1934
from math import gcd
import sys
input = sys.stdin.readline  #input보다 좀 더 빠름

def LCM(a, b):
    return a * b // gcd(a, b)  # 정수 부분만 취함

T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    print(LCM(a, b))