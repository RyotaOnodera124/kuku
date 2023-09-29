import random


def roll_dice(N, M):
    results = [random.randint(1, N) for _ in range(M)]
    return results


def main():
    try:
        N = int(input("サイコロの面の数は?: "))
        M = int(input("何回振りますか?: "))

        if N <= 0 or M <= 0:
            print("正の整数を入力してください。")
            return

        dice_results = roll_dice(N, M)
        print(dice_results)
    except ValueError:
        print("無効な入力です。正の整数を入力してください。")


if __name__ == "__main__":
    main()
