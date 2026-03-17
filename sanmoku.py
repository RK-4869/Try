#三目並べを作成していく。windowsローカルにおいてあるみたいだが、最新版に更新できていなかったため、1から作り直す。
#import sysではなくて今回はrandomが必要。
import random

#一度表示されるか確認する。→された。
#print("Hello world")

#Gameリストを作成し、表示させてみる。
Game=[0,1,2,3,4,5,6,7,8]
#print(Game)

#ゲーム開始時に名前を入力してもらう。
my = input("あなたの名前を入力してください:")
#相手の名前をrandom.choiceで作成してみる。
enemy_n = [
    "sato", "yamada", "harada", "aizawa"
    ]
#ランダムで表示させる。
enemy = random.choice(enemy_n)
print(f"対戦相手に{enemy}が選ばれました!!")
#盤面を3*3で構成する。
def display():
    for i in range(0, len(Game)):
        #3回に1回は改行する。
        if(i%3 == 2):
            print(Game[i])
        else:
            print(Game[i], end="") #最後は改行しない。

def inputBoard(playerT):
    #座標を入力する
    if(playerT == "o"):
        coo = int(input("0~8を入力して。"))
    else:
        coo = random.randint(0, 8)


    #入力した座標が数字ではなく、oかxであれば再入力
    if (Game[coo] == "o" or Game[coo] == "x"):
        inputBoard(playerT)
    #Gameに反映させる。
    else:
        Game[coo] = playerT
        

#ここまではターミナルで動かすことができた。
#次に勝敗引き分け判定を決める。
def win_lose():
    #勝ちパターンを表示させる。
    win_patterns =[
        (0,1,2), (3,4,5), (6,7,8), #行
        (2,5,8), (1,4,7), (0,3,6), #列
        (0,4,8), (2,4,6) #斜め
    ]
    
    for i in range(0, len(win_patterns)):
        [a, b, c] = win_patterns[i]
        
        if Game[a] == Game[b] == Game[c] and isinstance(Game[a], str):
            return Game[a]
        
        #引き分け判定
        if not any(isinstance(x, int)for x in Game):
            return "DRAW"

#三目並べを進行させる
while(True):
    display()
    #プレイヤーの番
    inputBoard("o")
    check = win_lose()
    if check:
        break
    
    #相手の番
    inputBoard("x")
    check = win_lose()
    if check:
        break

#結果を作成する。
display()
if check == "DRAW":
    print("引き分け")
elif check == "o":
    print(f"勝者は、{my}になりました。")
else:
    print("残念でした~。勝者は相手でした。")