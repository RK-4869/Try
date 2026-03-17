#ダウンロードしたテキストファイルを読み込む。
input_file="data3.txt"
output_file="result3.txt"

#mergesort関数として、ソートしたいリストを受け取れるarr変数を設定する。
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    #quicksortと同様にmergesortも小中大に分類する。
    neutral = len(arr)//2
    small = merge_sort(arr[:neutral])
    big = merge_sort(arr[neutral:])
    
    #分割したリストを整理してmergeさせる。
    return merge(small, big)

def merge(small, big):
    result=[]
    i = j = 0
    
    #大小のリストを比較し、小さい方をresultに追加する。
    while i < len(small) and j < len(big):
        if small[i] <= big[j]:
            result.append(small[i])
            i += 1
        else:
            result.append(big[j])
            j += 1
    
    result.extend(small[i:])
    result.extend(big[j:])
    return result

try:
    #データを読み込む
    with open(input_file, "r", encoding="utf-8") as f:
        data = [line.strip().zfill(7) for line in f if line.strip()]
    
    #ソート実行
    sorted_data = merge_sort(data)
    
    #書き出しをする。
    with open(output_file, "w", encoding="utf-8") as f:
        for item in sorted_data:
            f.write(item+"\n")
    print("成功")
    

except FileNotFoundError:
    print(f"Errorです。ファイルが見つかりません。")

except ValueError:
    print(f"数値以外が書かれています。")

except Exception as e:
    print(f"別の原因のerrorがありました:{e}")