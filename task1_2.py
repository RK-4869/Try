#クイックソートで昇順に並び替えていく。

#ダウンロードしたテキストファイルを読み込む。
input_file="data2.txt"
output_file="result2.txt"

#quick_sort関数として、ソートしたいリストを受け取る変数arrを作成する。
def quick_sort(arr):
    #分割できない部分までであれば、そのままデータを残す
    if len(arr) <=1:
        return arr
    #文字列として比較するため、中央値をpivotにする。
    pivot = arr[len(arr) // 2]
    #リストの中身を小中大に分類する。
    small = [x for x in arr if x < pivot]
    neutral = [x for x in arr if x == pivot]
    big = [x for x in arr if x > pivot]
    return quick_sort(small) + neutral +quick_sort(big)

#ファイルからデータを読み込む
try:
    with open(input_file, "r") as f:
        data2 = [line.strip() for line in f if line.strip()]
    #quicksortを実行すRU
    sorted_data = quick_sort(data2)
    
    #結果をファイルに出力する。
    with open(output_file, "w") as f:
        for item in sorted_data:
            f.write(item + "\n")
    
    print(f"クイックソートが完了しました")

#エラー文を書く。
except FileNotFoundError:
    print(f"errorです。")
#多方面のエラー文も書く。権限ないとか・・・？
except Exception as e:
    print(f"別の原因のerrorです!:{e}")