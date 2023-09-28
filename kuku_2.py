# 行数を入力
rows = int(input("行数を入力して下さい: "))

# 列数を入力
cols = int(input("列数を入力して下さい: "))

# クク表の生成と表示
for i in range(1, rows + 1):
    for j in range(1, cols + 1):
        # 2桁の数値に整形して出力
        print(f"{i * j:2}", end= " ")
    # 一行終わるごとに改行
    print()
