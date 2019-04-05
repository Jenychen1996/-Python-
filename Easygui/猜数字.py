import easygui as g
import random

secret = random.randint(1,10)
print('------------------我爱鱼C工作室------------------')
msg = '不妨猜一下小甲鱼现在心里想的是哪个数字(1~10):'
title = '数字小游戏'
msg2 = '哎呀，猜错了，请重新输入吧(1~10)：'
g.msgbox('嗨，欢迎进入第一个小游戏。')
def GuessNum():
    try:
        temp = g.integerbox(msg, title, lowerbound=1, upperbound=10)
        guess = int(temp)
        while guess:
            if guess == secret:
                g.msgbox("我草，你是小甲鱼心里的蛔虫吗？！")
                g.msgbox("哼，猜中了也没有奖励！")
                break
            else:
                if guess > secret:
                    g.msgbox("哥，大了大了~~~")
                else:
                    g.msgbox("嘿，小了，小了~~~")
                guess = g.integerbox(msg, title, lowerbound=1, upperbound=10)
    except ValueError as reason:
        g.msgbox("输入值有误...请重新输入" + str(reason))

    except EOFError as reason:
        g.msgbox("输入值有误...请重新输入" + str(reason))

    except KeyboardInterrupt as reason:
        g.msgbox("输入值有误...请重新输入" + str(reason))

    finally:
        g.msgbox("游戏结束，不玩啦^_^")

GuessNum()
