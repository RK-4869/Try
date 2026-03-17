#ダウンロードしたテキストファイルを読み込む。
input_file="data1.txt"
output_file="result1.txt"

try:
    with open(input_file, "r", encoding="utf-8") as f:
        #ファイルの中身を読み込む。
        numbers = f.read().split()
    #選択ソートを使用して並び替えをする。
    n = len(numbers)
    for i in range(n):
        min_ = i
        
        for j in range(i+1, n):
            if numbers[j] < numbers[min_]:
                min_ = j
        
        #一番小さいであろう数字と今の数字を入れ替える。
        numbers[i], numbers[min_] = numbers[min_], numbers[i]
        
        #結果を書き出す。
    result = "\n ".join(map(str, numbers))
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(result)
    print(f"resultに保存しました。", flush=True)

except Exception as e:
    print(f"エラーあり。:{e}")