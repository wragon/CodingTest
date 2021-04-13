import sys
input = sys.stdin.readline
N = int(input())
guest = []
for i in range(N):
    start, end = map(int, input().split())  #입력받은 값을 공백을 기준으로 분리
    guest.append((start, end))

guest = sorted(guest, key = lambda x : x[0])
enter = 0

for i in range(N):
    if guest[i][0] > enter:
        enter = guest[i][0]
    enter += guest[i][1]
    
print(enter)