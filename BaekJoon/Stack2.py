#%% #1874
import sys
input = sys.stdin.readline  #input보다 좀 더 빠름
N = int(input())
cnt = 1
seq = []
result = []
boolean = True
for i in range(N):
    num = int(input())
    while cnt <= num:
        seq.append(cnt)
        result.append("+")
        cnt += 1
    if seq[-1] == num:
        seq.pop()
        result.append("-")
    else:
        boolean = False

if boolean == True:
    for j in range(len(result)):
        print(result[j])
else:
    print("NO")