#%%  baseball
import random

numList = []
#맞출 숫자 랜덤으로 생성
#중복하지 않는 3개의 숫자를 string으로 배열에 삽입
#int형으로 한다면 123을 1,2,3이 아닌 123으로 보기 때문에
#string형으로 변환해준다.
for i in range(3):
    numList.append(str(random.randrange(1, 10)))
    #중복 검사
    for j in range(i):
        while numList[j] == numList[i]:
            del numList[i]
            numList.append(str(random.randrange(1, 10)))
    
print("▒▒PLAY BALL▒▒\n")
#본 게임
for cnt in range(10):
    s_cnt = 0
    b_cnt = 0
    
    print(str(cnt+1) + "번째 입니다.")
    inputList = input("숫자 3개를 입력해주세요 : ")
    for i in range(3):
        for j in range(3):
            if i == j:
                if inputList[i] == numList[j]:
                    s_cnt += 1
                else:
                    continue
            else:
                if inputList[i] == numList[j]:
                    b_cnt += 1
                else:
                    continue
    #맞춘 숫자가 없다면 out              
    if s_cnt == 0 and b_cnt == 0:
        print("Out!")
    #strike가 3개면 승리  
    elif s_cnt == 3:
        print("Strike Out!!!")
        print(str(cnt) + "번째 만에 성공!")
        break
    #그것도 아니라면 현재 상황 출력  
    else:
        print("『" + str(s_cnt) + "』 strike 『" + str(b_cnt) + "』 ball\n" )
    #game over    
    if cnt == 9:
        print("You Lose")