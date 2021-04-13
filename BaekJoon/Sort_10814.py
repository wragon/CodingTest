#%% #10814
import sys
input = sys.stdin.readline  #input보다 좀 더 빠름

N = int(input())
member = []
for i in range(N):
    age, name = input().split()  #입력받은 값을 공백을 기준으로 분리
    member.append((int(age), name))

member = sorted(member, key = lambda x : x[0])

for i in range(N):
    print(member[i][0], member[i][1])