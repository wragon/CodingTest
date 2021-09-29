#%% LOL에서 팀과 라인 랜덤 생성 프로그램
import random

def Team(name_list):
    blue_team = ""
    red_team = ""
    blue_cnt = 0
    red_cnt = 0
    idx = 0
    while(1):
        #블루팀과 레드팀이 모두 5명이 채워지면 반복문 나가기
        if blue_cnt == 5 and red_cnt == 5:
            break
        
        #blue팀과 red팀을 랜덤으로 나누기
        team_idx = random.randrange(0, 2)   
        #blue팀
        if(team_idx == 0):
            #이미 blue팀에 5명이 채워진 경우 반복문 처음으로
            if blue_cnt == 5:
                continue
            #5명이 아닐경우 추가
            blue_team += name_list[idx]
            blue_team += ","
            blue_cnt += 1
            idx += 1
        #rea팀
        if(team_idx == 1):
            #이미 red팀에 5명이 채워진 경우 반복문 처음으로
            if red_cnt == 5:
                continue
            #5명이 아닐경우 추가
            red_team += name_list[idx]
            red_team += ","
            red_cnt += 1
            idx += 1
        
    print("\nBlue_team : " + blue_team)
    print("Red_team : " + red_team)

               
def Line(name_list):
    line_list = ["TOP", "JGL", "MID", "AD", "SPT"]  #LOL 5개의 라인
    num_list = [4, 1, 2, 0, 3] #보기 좋게 출력하기 위해
    prev_name_idx = []  #중복을 없애기 위해
    prev_line_idx = []  #중복을 없애기 위해
    name = []
    line = []
    output = []

    while(1):
        if(len(prev_name_idx) == 5):
            break
        name_idx = random.randrange(0, 5)  #이름 인덱스
        line_idx = random.randrange(0, 5)  #라인 인덱스
        
        #중복된 번호가 나오면 while문에 처음으로 되돌아가기
        if(name_idx in prev_name_idx): 
            continue
        if(line_idx in prev_line_idx):
            continue
        
        name = name_list[name_idx]
        line = line_list[line_idx]
        output.append(line + " : " + name) 
        output = sorted(output)  #보기 좋게 출력하기 위해
        #이미 나온 번호를 저장하기
        prev_name_idx.append(name_idx)
        prev_line_idx.append(line_idx)

    for i in num_list:
        print(output[i])


name_list = []
msg = "\n■LOL 내전 프로그램■\n①팀 나누기\n②라인 나누기\n③나가기\n"
##이름 입력 방법1
#for i in range(5):
#    name_list.append(input("이름을 입력하시오 : "))

##이름 입력 방법2
while(1):
    choice = int(input(msg))
    if(choice == 1):
        print("10명의 친구의 이름을 적어주세요\n")
        friend = input("이름을 입력하시오 : ").split(",")
        for i in range(len(friend)):
            name_list.append(friend[i])
        Team(name_list)
        name_list.clear()  #리스트 초기화1
        
    elif(choice == 2):
        print("5명의 친구의 이름을 적어주세요\n")
        friend = input("이름을 입력하시오 : ").split(",")
        for i in range(len(friend)):
            name_list.append(friend[i])
        Line(name_list)
        del name_list[:]  #리스트 초기화2
        
    else:
        print("종료")
        break
#준용,강민,승민,익준,두연,현민,지훈,지환,덕화,창현,
#준용,성용,승헌,남훈,찬도
#민성,준용,희수,윤성,찬서,병휘,성용,은석,성호,찬도 