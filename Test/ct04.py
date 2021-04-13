import sys
input = lambda: sys.stdin.readline().rstrip()  # "\n"제거
N = int(input())
arr = []
for _ in range(N):
    word = input()
    word_count = len(word)
    sum = 0
    for num in word:
        if num.isdigit():  # 숫자인지 확인
            sum += int(num)
    arr.append((word_count, sum, word))  

arr = sorted(arr, key = lambda x : (x[0], x[1], x[2]))  #길이->합계->사전순으로 정렬

##출력 방법1##
for i in range(N):
    print(arr[i][2])
    
##출력 방법2##
# for _, _, word in arr:
#     print(word)