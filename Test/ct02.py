import sys
input = sys.stdin.readline  #input보다 좀 더 빠름

N, M = map(int, input().split())
arr = []
for i in range(M):
    package, one = map(int, input().split())  #입력받은 값을 공백을 기준으로 분리
    arr.append((package, one))

arr = sorted(arr, key = lambda x : x[0])  #세트가격 오름차순 정렬
min_set = arr[0][0] 
arr = sorted(arr, key = lambda x : x[1])  #단품가격 오름차순 정렬
min_one = arr[0][1]

if min_set > min_one * 6:
    min_set = min_one * 6

if (N % 6) * min_one > min_set:
    money = (N//6) * min_set + min_set
else:
    money = (N//6) * min_set + (N%6) * min_one

print(money)
