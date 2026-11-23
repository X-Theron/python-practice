while True:
    print("游戏开始，范围 1–100，你一共有 7 次机会，开始吧！")
    import random
    num=random.randint(1,100)
    times=7
    while times>0:
        try:
            guessnum=int(input("请输入数字"))
        except ValueError:
            print("输入无效，请输入纯数字")
            continue
        if guessnum==num:
            times -= 1
            if times>=4:
                print(f"恭喜你{7-times}次猜中,你就是传说中的欧皇")
            elif 3>=times>=2:
                print(f"恭喜你{7-times}次猜中,很稳")
            elif 1>=times>=0:
                print(f"恭喜你{7-times}次猜中,险胜")
            break
        elif guessnum<num:
            times -= 1
            print(f"猜小了，还剩{times}次")
            continue
        elif guessnum>num:
            times -= 1
            print(f"猜大了，还剩{times}次")
            continue
    else:
        print(f"次数用完啦，答案是{num}，")
    chance=input("请问你想再来一次还是退出")
    if chance=="再来一次":
        pass
    elif chance=="退出":
        break
    else:
        print("请重新输入")



