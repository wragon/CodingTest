n = 8
k = 2
cmd = ["D 2", "U 3", "D 4", "U 2", "Z", "Z", "U 1"]
answer = ["O"] * n
move_type = ['U', 'D', 'C', 'Z']
del_line = []
for plan in cmd:
    if plan[0] == move_type[0]:
        k -= int(plan[2])
        if k < 0:
            k = 0
        # print("{}{}{}{}".format(plan,answer,k,n))
    elif plan[0] == move_type[1]:
        k += int(plan[2])
        if k > n:
            k = n
        # print("{}{}{}{}".format(plan,answer,k,n))
    elif plan[0] == move_type[2]:
        del answer[k]
        del_line.append(k)
        answer.insert(k, "X")
        if k == n:
            k -= 1
        else:
            k += 1
        n -= 1
        # print("{}{}{}{}".format(plan,answer,k,n))
    elif plan[0] == move_type[3]:
        if len(del_line) != 0:
            n += 1
            del answer[del_line[-1]]
            answer.insert(del_line[-1], "O")
            del del_line[-1]
        print("{}{}{}{}".format(plan,answer,k,n))
answer = ''.join(answer)
print(answer)