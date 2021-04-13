total = 0
while(1):
    num = int(input("숫자를 입력하시오: "))
    total += num
    choice = input("계속?(yes/no): ")
    if choice == "yes":
        num = 0
    elif choice == "no":
        break;
    else:
        print("잘못 입력하셨습니다.")
        break;
        
print("합계는 : %d" %total)