#%% Greedy1(#1931)
import sys
input = sys.stdin.readline  #input보다 좀 더 빠름

N = int(input())
meeting = []
for i in range(N):
    start, end = map(int, input().split())  #입력받은 값을 공백을 기준으로 분리
    meeting.append((start, end))

meeting = sorted(meeting, key = lambda x : x[0])
meeting = sorted(meeting, key = lambda x : x[1])

cnt = 0
finish = 0
for i in range(N):
    if finish <= meeting[i][0]:  #시작시간 비교
        finish = meeting[i][1]   #종료시간 반영
        cnt += 1

print(cnt)