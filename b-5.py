def get_input():
    try:
        input_data = input("データを入力してください(スペース区切り): ")
        input_numbers = [int(x) for x in input_data.split()]
        return input_numbers
    except ValueError:
        print("無効な入力です。整数をスペース区切りで入力してください。")
        return get_input()


def calculate_sum(data):
    total = 0
    for num in data:
        total += num
    return total


def calculate_max(data):
    max_value = data[0]
    for num in data:
        if num > max_value:
            max_value = num
    return max_value


def calculate_min(data):
    min_value = data[0]
    for num in data:
        if num < min_value:
            min_value = num
    return min_value


def calculate_average(data):
    total = calculate_sum(data)
    count = len(data)
    return total / count


def main():
    data = get_input()

    if len(data) > 0:
        print(f"合計値: {calculate_sum(data)}")
        print(f"最大値: {calculate_max(data)}")
        print(f"最小値: {calculate_min(data)}")
        print(f"平均値: {calculate_average(data)}")
    else:
        print("データが入力されていません。")


if __name__ == "__main__":
    main()
