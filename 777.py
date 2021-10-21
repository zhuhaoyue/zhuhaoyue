
import random

counts = 3
answer = random.randint(1,10)

while counts > 0:
    temp = input("不妨猜一下小七宝现在心里想的是哪一个数字：")
    guess = int(temp)

    if guess ==answer:
        print("你是小七宝心里的蛔虫嘛? !")
        print("哼，你猜中了也没奖励 !")
        break
    else:
        if guess < answer:
            print("小啦")
        else:
            print("大啦")
        if counts > 1:
            print("再给你一次机会！")
        else:
            print("机会用光咯")
            
    counts = counts-1

print("游戏结束，不玩啦~~")
