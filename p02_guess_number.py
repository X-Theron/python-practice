import random

MIN_NUM = 1
MAX_NUM = 100
MAX_TRIES = 7
def game():
    print(f"游戏开始，范围 {MIN_NUM}-{MAX_NUM}，你一共有 {MAX_TRIES} 次机会，开始吧！")
    num = random.randint(MIN_NUM,MAX_NUM )
    times = MAX_TRIES
    while times > 0:
        try:
            guess_number = int(input("请输入数字"))
        except ValueError:
            print("输入无效，请输入纯数字")
            continue
        if guess_number < 1 or guess_number > 100:
            print("请输入 1–100 之间的数字")
            continue
        elif guess_number == num:
            times -= 1
            used = 7 - times
            if times >= 4:
                print(f"恭喜你{used}次猜中,你就是传说中的欧皇")
            elif 3 >= times >= 2:
                print(f"恭喜你{used}次猜中,很稳")
            else:
                print(f"恭喜你{used}次猜中,险胜")
            return True, used
        elif guess_number < num:
            times -= 1
            print(f"猜小了，还剩{times}次")
        elif guess_number > num:
            times -= 1
            print(f"猜大了，还剩{times}次")
    print(f"次数用完啦，答案是{num}，")
    return False, num

if __name__ == "__main__":
    win_times=0
    lose_times=0
    while True:
        won,info=game()
        if won:
            win_times += 1
        else:
            lose_times += 1
        while True:
            chance = input("再来一次还是退出?")
            if chance in ("再来一次", "退出"):
                break
            print("不认识的指令,请重新输入")
        if chance == "退出":
            break
    print(f"在游玩过程中，您一共赢了{win_times}次，输了{lose_times}次")


