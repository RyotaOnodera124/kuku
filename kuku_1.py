# 9x9の九九表を生成
for i in range(1, 10):
    for j in range(1, 10):
        # 2桁の数値に整形して出力
        print(f"{i * j:2}", end=" ")
    # 1行終わるごとに改行
    print()
