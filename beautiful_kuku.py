# 行数を入力
rows = int(input("行数を入力してください: "))

# 列数を入力
cols = int(input("列数を入力してください: "))

# 行列の掛け算の結果を表示
for i in range(1, rows + 1):
    for j in range(1, cols + 1):
        # 掛け算の結果を計算
        result = i * j
        # 結果を指定された形式で表示
        print(f"{i} x {j} = {result:2}", end=" | ")
    # 行の終わりに改行
    print()
