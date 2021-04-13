#%% #1920
import sys
input = sys.stdin.readline  #input보다 좀 더 빠름

def Binary(A, n, low, high):
    mid = (low + high) // 2
    if low > high:
        return 0
    elif A[mid] == n:
        return 1
    elif A[mid] < n:
        return Binary(A, n, mid+1, high)
    elif A[mid] > n:
        return Binary(A, n, low, mid-1)

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

A = sorted(A)
for i in B:
    print(Binary(A, i, 0, N-1))