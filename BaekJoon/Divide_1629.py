#%% #1629
import sys
input = sys.stdin.readline  #input보다 좀 더 빠름
A, B, C = map(int, input().split())

def Divide(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    elif b % 2 > 0:  # b가 홀수일 때
        return Divide(a, b-1) * a
    else:  # b가 짝수일 때
        result = Divide(a, b//2)
        return pow(result, 2) % C

print(Divide(A, B) % C)