if __name__ == '__main__':
    with open("../txtf/input.txt", "r") as file:
        # Ссылки на дочерние узлы указывают на номер строки, поэтому
        # придется обрабатывать данные на ходу
        data = file.readlines()

    # Считываем количество вершин
    n = int(data[0])

    # Если дерево пустое
    if n == 0:
        print(0)

    # Построение дерева в виде словаря
    tree = {}
    for i in range(n):
        key, left, right = map(int, data[i + 1].split())
        tree[i + 1] = (left, right)

    # Рекурсивная функция для вычисления высоты дерева
    def calculate_height(node):
        if node == 0:  # Если нет ребенка (узел является листом), высота = 0
            return 0
        left_child, right_child = tree[node]
        left_height = calculate_height(left_child)
        right_height = calculate_height(right_child)
        return 1 + max(left_height, right_height)

    # Начинаем расчет с корня (вершина с номером 1, потому что в 0 у нас узел означающий пустоту/отсутствие узла)
    height = calculate_height(1)

    # Выводим результат
    print(height)
    with open("../txtf/output.txt", "w") as file:
        file.write(str(height))
