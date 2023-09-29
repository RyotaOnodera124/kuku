def main():
    # 3都府県のいくつかの駅名とある日の最高気温(単位: ℃)のデータを辞書として持っています
    weather_information = [
        {'prefecture': '東京都', 'station': '渋谷', 'temperature': 6.5},
        {'prefecture': '東京都', 'station': '池袋', 'temperature': 7.0},
        {'prefecture': '東京都', 'station': '新橋', 'temperature': 7.5},

        {'prefecture': '大阪府', 'station': '梅田', 'temperature': 8.2},
        {'prefecture': '大阪府', 'station': '大阪', 'temperature': 9.3},
        {'prefecture': '大阪府', 'station': '堺', 'temperature': 9.5},

        {'prefecture': '福岡県', 'station': '博多', 'temperature': 13.0},
        {'prefecture': '福岡県', 'station': '太宰府', 'temperature': 15.0},
    ]

    # 福岡県内の気温を合計するための変数を初期化
    total_temperature = 0
    station_count = 0

    # 福岡県内の各駅の気温を合計
    for data in weather_information:
        if data['prefecture'] == '福岡県':
            total_temperature += data['temperature']
            station_count += 1

    # 平均気温を計算
    if station_count > 0:
        average_temperature = total_temperature / station_count
        print(f"福岡県の平均気温は {average_temperature:.1f} ℃ です。")
    else:
        print("福岡県のデータがありません。")

if __name__ == "__main__":
    main()
