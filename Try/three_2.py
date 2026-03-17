'''three.pyで実装したが、リストに含まれているもの以外が入力されたときのエラーを実装していく。
そのためにはwhile文が必要と考えた。'''

import random

hands = ["ぐー", "ちょき", "ぱー"]
print("じゃんけんをしよう！")

#while文を導入していく。
while True:
    my_hand = input("ぐー、ちょき、ぱーのどれかを入力してください。")
    #入力された文字列がリストの中に入っているかを確認するためにbreakを使用する。
    if my_hand in hands:
        break #入っているならループを抜けることができる。
    else:
        print("正しく入力してください。(ひらがな入力ですよ！)")

#相手がランダムに選ぶ
cp_hand = random.choice(hands)

#手を見せ合う
print(f"陸さん:{my_hand}")
print(f"相手：{cp_hand}")

#勝敗判定の条件式を別の変数を用い、PEP8基準を元に整理してみる。
win_lose = (
    (my_hand == "ぐー" and cp_hand == "ちょき") or
    (my_hand == "ちょき" and cp_hand == "ぱー") or
    (my_hand == "ぱー" and cp_hand == "ぐー")
)
# 勝敗判定をif文を使ってする
if my_hand == cp_hand:
    print("結果：あいこになりました")
elif win_lose:
    print("結果：陸さんの勝ちになりました")
else:
    print("結果：相手の勝ちになりました")
