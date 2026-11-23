# 猜数字游戏：1–100，最多猜7次，猜完给战绩评价。
print("游戏开始，范围 1–100，你一共有 7 次机会，开始吧！")
import random
num=random.randint(1,100)           # 随机生成答案
times=7
while times>=0:                           # 剩0次时还能再猜最后一次，超次走 else 揭示答案
    try:
        guessnum=int(input("请输入数字"))
    except ValueError:                    # 输入不是数字时，不崩，提示重来（不扣次数）
        print("输入无效，请输入纯数字")
        continue
    if guessnum==num:
        times -= 1                        # 用 7-times 反推"第几次猜中"，按次数给不同评价
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
chance=input("请问你想再来一局还是退出")


