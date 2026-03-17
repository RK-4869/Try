import sys

print("Hello, Python world!")
print(f"Python Vesion: {sys.version}")
print("実務へ向けた第一歩、成功です!") ##printができてるという確認
print("コミットその1できてる？") ##git bashを用いた初コミット
print("コミット確認") ##編集してコミットできてるかの確認
##print("VSCODE上でgit bashしてみた") ##できてた。

# 1. 盤面をリストで作る（0〜8の数字が入ったリスト）
board = [" " for _ in range(9)]

def display_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
import random  # CPUの動きに使う

board = [" " for _ in range(9)]

def display_board():
    print(f"\n{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}\n")

def check_winner(player):
    # 勝利パターン（横、縦、斜め）
    win_patterns = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # 横
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # 縦
        [0, 4, 8], [2, 4, 6]             # 斜め
    ]
    for p in win_patterns:
        if board[p[0]] == board[p[1]] == board[p[2]] == player:
            return True
    return False

# メインループ
current_player = "〇"
for turn in range(9):
    display_board()
    
    if current_player == "〇":
        # --- 入力チェック ---
        while True:
            try:
                move = int(input(f"{current_player}の番です (0-8): "))
                if 0 <= move <= 8 and board[move] == " ":
                    break
                else:
                    print("そこには置けません。空いている0-8の数字を入れてね。")
            except ValueError:
                print("数字（0-8）を入力してください！")
        board[move] = "〇"
    else:
        # --- CPU対戦 (random) ---
        print("CPU（×）が考えています...")
        empty_indices = [i for i, x in enumerate(board) if x == " "]
        move = random.choice(empty_indices)
        board[move] = "×"

    # --- 勝利判定 ---
    if check_winner(current_player):
        display_board()
        print(f"【祝】{current_player}の勝ちです！")
        break
    
    current_player = "×" if current_player == "〇" else "〇"
else:
    display_board()
    print("引き分けです！") ##paizaの模写(自作ではない)