#%% #11650
import sys
input = sys.stdin.readline  #input보다 좀 더 빠름

N = int(input())
dimension = []
for i in range(N):
    x, y = map(int, input().split())  #입력받은 값을 공백을 기준으로 분리
    dimension.append((x, y))

dimension = sorted(dimension)

for i in range(N):
    print(dimension[i][0], dimension[i][1])