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

    # 各都府県の気温を合計するための辞書を初期化
    prefecture_temperatures = {}

    # 各都府県の気温を合計
    for data in weather_information:
        prefecture = data['prefecture']
        temperature = data['temperature']
        if prefecture in prefecture_temperatures:
            prefecture_temperatures[prefecture] += temperature
        else:
            prefecture_temperatures[prefecture] = temperature

    # 各都府県の気温を合計し、都府県の数で割って平均気温を計算
    total_temperature = sum(prefecture_temperatures.values())
    total_prefectures = len(prefecture_temperatures)
    average_temperature = total_temperature / total_prefectures

    print(f"全国の平均気温は {average_temperature:.2f} ℃ です。")


if __name__ == "__main__":
    main()
