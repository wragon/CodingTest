#%% #2805
import sys
input = sys.stdin.readline  #input보다 좀 더 빠름

def Felling(tree, M, low, high):
    mid = (low + high) // 2
    if low > high:
        return mid
    height = 0
    for i in tree:
        if i >= mid:
            height += i - mid
    if height == M:
        return mid
    elif height > M:
        return Felling(tree, M, mid+1, high)
    elif height < M:
        return Felling(tree, M, low, mid-1)

N, M = map(int, input().split())
tree = list(map(int, input().split()))

tree = sorted(tree)
print(Felling(tree, M, 0, tree[N-1]))