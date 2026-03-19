#オセロを作成するファイルです。
#まず使用しそうな関数と変数を定義する。
#定数:オセロをするにあたって変わらないもの
#変数：オセロが進むにつれて変化していくものとする。

#ボードのサイズを作成する。基本的な8*8の合計64マスで作成してみる。これは定数
BOARD_SIZE = 8
#各マスを白黒や空スペースに関して数字で定数として入力しておく。
#空スペースなら0、黒石なら1、白石なら2とする。
EMPTY = 0
BLACK = 1
WHITE = 2

#次に三目並べの勝ちパターンのようにオセロに必要な移動量について書いてみる。
#方向を書いておかないとひっくり返す動作の時にチェックできなさそう。上下左右でリストにしてみる。
#(-1, 0)なら上方向、(1, 1)なら右下のように書いていく。
DIRECTIONS = [
    #左上、上、右上
    (-1, -1), (-1, 0), (-1, 1),
    #左、右
    (0, -1), (0, 1),
    #左下、下、右下
    (1, -1), (1, 0), (1, 1),
]

#文字マッピングについて表示していく。その際、辞書が使えそうなので辞書を使って書いてみる。
STONE_DISPLAY = {
    #空スペースは点のみにしておく。(中黒)
    EMPTY: "・",
    #黒石は黒と見分けがつくように塗りつぶされた丸を使用する。
    BLACK: "⚫︎",
    #白石は通常の丸を使用する
    WHITE: "⚪︎",
}

#次にプレイヤー名について辞書としてまとめておく。
PLAYER_NAME = {
    BLACK: "黒(⚫︎)",
    WHITE: "白(⚪︎)"
}

#次にオセをを始める上で、ボードを常に初期化する必要がありそう。
#テーブルボードはboard[行][列]で表現する。board[0][0]であれば左上のマスになる？

def initialize_board():
    board = [
        #8行8列の2次元リストを作成する。
        [EMPTY for _ in range(BOARD_SIZE)]
        for _ in range(BOARD_SIZE)
    ]
    #---オセロの初期配置---
    #中央の4マスに白黒石を配置する。ボードの中央は、3,4の位置にあたる。
    center = BOARD_SIZE // 2
    
    board[center -1][center -1] = WHITE #左上に白を置く。
    board[center -1][center]    = BLACK #右上に黒を置く。
    #同様に左下と右下にも石を置く。
    board[center][center -1]    =BLACK  #左下
    board[center][center]       =WHITE  #右下
    
    return board

#次にボードを表示していく。ここでUX部分も意識してコードを書いてみる。
#視覚的にも見やすくしたいため、点線や実線を使用していく。ターミナルでも使用できる罫字も使用してみる。
#置くことのできる場所をmovesを引数として記述する。
def display_board(board, valid_moves=None):
    if valid_moves is None:
        valid_moves = []
    #列ラベル
    print("\n 1 2 3 4 5 6 7 8")
    #枠線部分を実装した。
    print("   " + "-" * 17)
    
    for r in range(BOARD_SIZE):
        #行番号を表示する
        print(f"{r+1}|", end="  ")
        
        for c in range(BOARD_SIZE):
            stone = STONE_DISPLAY[board[r][c]]
            print(stone, end="  ")
        
        #右側の枠線として
        print("|")
    
    #下の枠線として
    print("  " + "-" * 17)

#一度ボード画面を表示してみる。
my_board = initialize_board()
display_board(my_board)

#石を置けるか判定するロジックを作る。
def is_moves(board, row, col, player):
    #指定したrowやcolにplayerの石を置くことができるか判定をしたい。
    #置くことができる場合は、挟んでひっくり返せる方向のリストをさせるようにする。
    #置くことができない場合は、空のスペースのリストを返す。
    
    #既に石がある場合
    if board[row][col] != EMPTY:
        return []
    
    #相手の色を特定する。
    opponent = WHITE if player == BLACK else BLACK
    
    #挟める石がある方向を書くリストを作る。
    valid_derections =[]
    
    #方向をすべて確認する。行の移動量をdr(dalta row)、dc(delta column)とすると、
    for dr, dc in DIRECTIONS:
        #行列それぞれの移動量を確認する。row+dcが上をチェックcするなら、row - 1?になりそう。
        r, c = row + dr, col + dc
        
        #置いた石の真隣が相手側が置いた石かどうかチェックする
        if 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE and board[r][c] == opponent:
            #その方向に進む
            while 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE:
                #空のスペースであれば失敗する。
                if board[r][c] == EMPTY:
                    break
                #自分の石が見つかるなら、その方向は挟んでひっくり返すことができる
                if board[r][c] == player:
                    valid_derections.append((dr, dc))
                    break
                #相手側の石の場合、その方向の先を見る。
                r += dr
                c += dc
    
    return valid_derections

#place_stoneを使用して、実際に石を置くロジックを考えてみる。
def place_stone(board, row, col, player):
    #boardは現在のボード、row, colは石を置く場所、playerは黒か白を置くひと。
    #最初に指定されたマスに石を置いてみるコードを書く。
    board[row][col] = player
    
    #is_movesを用いてひっくり返せう方向のリストを取得する。
    directions = is_moves(board, row, col, player)
    
    #返ってきた方向リストをfor文を使用して書いていく。
    for dr, dc in directions:
        #その方向の真隣から始める。
        r, c = row + dr, col + dc
        
        #相手の石があるならそのままひっくり返す。
        #自分の石があれば止まるように書いてみる。
        while board[r][c] != player:
            #相手の石をひっくり返して自分の石に置き換える。
            board[r][c] = player
            #置き換えられたら次のマスに進む。
            r += dr
            c += dc

#一度中断して入門学習に戻る。



