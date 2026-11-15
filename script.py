import random

class 遊戲角色:
    生命值 = 400
    def __init__(self, 姓名):
        self.姓名 = 姓名
    def 防禦(self, 指令):
        if 指令 == 1:
            print(f"{self.姓名}擺出了格擋姿勢")
            return 0.5
        elif 指令 == 2:
            print(f"{self.姓名}嘗試閃避攻擊")
            return random.choice([0.3, 1])
class 戰士(遊戲角色):
    def 攻擊(self, 指令):
        if 指令 == 1:
            print(f"{self.姓名}使出了塗次攻擊！！！")
            return 200
        elif 指令 == 2:
            print(f"{self.姓名}奮力使出了迴旋揮砍")
            return random.choice([300, 100])
class 魔物(遊戲角色):
    def 攻擊(self, 指令):
        if 指令 == 1:
            print(f"{self.姓名}使出了利爪攻擊！！！")
            return 180
        elif 指令 == 2:
            print(f"{self.姓名}張出血口噴出毒液")
            return random.choice([320, 100])
玩家姓名 = input("請輸入你的姓名")
玩家 = 戰士(玩家姓名)
敵方 = 魔物("宋品賢")
隨機 = random.choice([1, 2])
while True:
    攻擊指令 = int(input("請輸入攻擊指令(1)普通攻擊(2)特殊攻擊："))
    玩家攻擊力 = 玩家.攻擊(攻擊指令)
    損血 = int(敵方.防禦(隨機) * 玩家攻擊力)
    敵方.生命值 -= 損血
    if 敵方.生命值 <= 0:
        print(f"{敵方}倒下了，{玩家.姓名}勝利～～～！！！")
        break
    else:
        print(f"{敵方.姓名}受到了{損血}傷害！生命值剩下 {敵方.生命值}")
        print("")

    防禦指令 = int(input("請輸入防禦指令(1)格擋(2)閃避："))
    敵方攻擊力 = 敵方.攻擊(隨機)
    損血 = int(玩家.防禦(防禦指令) * 敵方攻擊力)
    玩家.生命值 -= 損血
    if 玩家.生命值 <= 0:
        print(f"{玩家}受重傷倒下了，遊戲結束～～～！！！")
        break
    else:
        print(f"{玩家.姓名}受到了{損血}傷害！生命值剩下 {玩家.生命值}")
        print("")
