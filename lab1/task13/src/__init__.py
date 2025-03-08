def main():
    n, nums = custom_read("../txtf/input.txt")

    total = sum(nums)
    target = total // 3

    # проверка базовых случаев
    if n < 3 or total % 3 != 0:
        return 0

    # Если есть элемент больше целевой суммы — разбиение невозможно
    if any(x > target for x in nums):
        return 0

    # для всех не базовых случаев:
    # dp[i][j] = True, если можно собрать i подмножеств с суммарной суммой j
    dp = [set() for _ in range(4)]
    dp[0].add(0)

    for num in nums:
        # Обходим состояния в обратном порядке, чтобы избежать повторного использования элементов
        for i in range(3, 0, -1):
            for prev_sum in dp[i - 1]:
                current_sum = prev_sum + num
                if current_sum <= target:
                    dp[i].add(current_sum)

    # Проверяем, удалось ли собрать 3 подмножества с суммой target
    if target in dp[3]:
        return 1
    else:
        return 0


def custom_read(path):
    with open(path, "r") as file:
        n = int(file.readline().strip())
        arr = list(map(int, file.readline().strip().split(" ")))
    return n, arr

def custom_write(path, output):
    with open(path, "w") as file:
        file.write(str(output))

if __name__ == '__main__':
    import time
    import tracemalloc

    start_time = time.perf_counter()
    tracemalloc.start()

    custom_write("../txtf/output.txt", main())
    main()

    print("time  taken: ", time.perf_counter() - start_time, "seconds")
    print("memory used: ", tracemalloc.get_tracemalloc_memory() / 2 ** 20, "MB")
