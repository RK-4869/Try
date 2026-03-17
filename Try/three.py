import random

#選択肢をリストにまとめてみる
hands = ["ぐー", "ちょき", "ぱー"]

#じゃんけんをするときの自分の目線
print("じゃんけんをしよう！")
my_hand = input("ぐー、ちょき、ぱーのどれかを入力してください。")

#相手がランダムに選ぶ
cp_hand = random.choice(hands)

#手を見せ合う
print(f"陸さん:{my_hand}")
print(f"相手：{cp_hand}")

#勝敗判定をif文を使ってする
if my_hand == cp_hand:
    print("結果：あいこになりました")
elif my_hand == "ぐー" and cp_hand =="ちょき" or my_hand == "ちょき" and cp_hand=="ぱー" or my_hand=="ぱー" and cp_hand== "ぐー":
    print("結果：陸さんの勝ちになりました")
else:
    print("結果：相手の勝ちになりました")
