# Класс с реализованными методами
class SortedStorage:
    def __init__(self):
        self.storage = []

    def add(self, number):
        self.storage.append(number)
        self.storage.sort(reverse=True)

    def remove(self, number):
        self.storage.remove(number)

    def get_max(self, k):
        return self.storage[k-1]

    # Задаем само хранилище
    @staticmethod
    def read_list(path_in, path_out):
        sorted_storage = SortedStorage()

        with open(path_in) as file_in, open(path_out, "w") as file_out:
            n = int(file_in.readline())

            for i in range(0, n):
                action, number = file_in.readline().split()
                number = int(number)

                if action == "+1" or  action == "1":
                    sorted_storage.add(number)
                elif action == "0":
                    result = sorted_storage.get_max(number)
                    file_out.write(str(result) + "\n")
                else:
                    sorted_storage.remove(number)


# Запуск
def main():
    SortedStorage.read_list("../txtf/input.txt", "../txtf/output.txt")


if __name__ == "__main__":
    import time
    import tracemalloc

    t_start = time.perf_counter()
    tracemalloc.start()
    main()
    print(time.perf_counter() - t_start)
    print(tracemalloc.get_tracemalloc_memory() / 2 ** 20, "MB")