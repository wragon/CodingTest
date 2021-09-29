#%% LOL2
import random
namelist = input("10명의 이름을 적으시오 : ").split(",")
line = ["TOP", "JGL", "MID", "AD", "SPT"]
num_list = [4, 1, 2, 0, 3] #출력 순서

red_name = []
blue_name = []
red_line = []
blue_line = []
Routput = []
Boutput = []

# 팀 랜덤
red_name = random.sample(namelist, 5)
for name in namelist: # redteam에 안들어간 사람 blue팀에 넣기
    if name not in red_name:
        blue_name.append(name)
        
# 라인 랜덤
red_line = random.sample(line, 5)
blue_line = random.sample(line, 5)

for i in range(5):
    Routput.append(red_line[i] + " : " + red_name[i])
    Boutput.append(blue_line[i]+ " : " + blue_name[i])

# 알파벳순 정렬
Routput = sorted(Routput)
Boutput = sorted(Boutput)

print("[blueteam]")  
for i in num_list:
    print(Routput[i])
print("---\n[redteam]")
for i in num_list:
    print(Boutput[i])

#준용,덕화,창현,승민,두연,현민,지호,한,익준,지환