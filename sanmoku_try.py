#三目並べを作成していく。windowsローカルにおいてあるみたいだが、最新版に更新できていなかったため、1から作り直す。
#import sysではなくて今回はrandomが必要。
import random

#一度表示されるか確認する。→された。
#print("Hello world")

#Gameリストを作成し、表示させてみる。
Game= [
    0,1,2,3,4,5,6,7,8
]
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
    print("\n")
    for i in range(3):
        # 各行の要素を | で繋いでみる
        row = f" {Game[i*3]} | {Game[i*3+1]} | {Game[i*3+2]} "
        print(row)
        if i < 2:
            print("---+---+---") # 行の間の区切り線
    print("\n" + "=" * 13)

def inputBoard(playerT):
    #座標を入力する
    if(playerT == "o"):
        while True:
            try:
                coo = int(input("0~8を入力して。"))
                
                if 0 <= coo <= 8:
                    if Game[coo] not in ["o", "x"]:
                        break
                    else:
                        print("エラーです。すでに数字が入っています。")
                else:
                    #0~8以外が入力された場合
                    print("0~8の中から、[半角数字で]入力してください！")
            except ValueError:
                print("数字を入力してください。")
    else:
        while True:
            coo = random.randint(0, 8)
            if Game[coo] not in ["o", "x"]:
                break
    
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
    print(f"残念でした~。勝者は{enemy}でした。")
