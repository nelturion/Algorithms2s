# Кастомное чтение файла для этой задачи
def custom_read(path):
    with open(path) as file:
        n, m, lead = file.readline()[:-1].split(" ")
        a = split_cards(replaces(file.readline()).replace(" ", ""))
        b = split_cards(replaces(file.readline()).replace(" ", ""))
        a = {k: sorted(v, reverse=True) for k, v in a.items()}
        b = {k: sorted(v, reverse=True) for k, v in b.items()}
    file.close()

    return int(n), int(m), lead, a, b


# Разбиение строки на словарь
def split_cards(line):
    line = line.strip()
    card_dict = {"S": [], "C": [], "D": [], "H": []}

    for i in range(0, len(line), 2):
        card, suit = line[i], line[i + 1]
        if suit in card_dict:
            card_dict[suit].append(int(card))

    return card_dict


# Очистка словаря от пустых мастей
def clear_dict(a):
    a1 = a.copy()
    for i in a1:
        if not a1.get(i):
            a.pop(i)

    return a

# Заменя
def replaces(line):
    replacements = {"6": "1", "7": "2", "8": "3", "9": "4", "T": "5", "J": "6", "Q": "7", "K": "8", "A": "9"}
    return "".join(replacements.get(char, char) for char in line)


# Проверка (основной алгоритм)
def check(n, m, lead, a, b):
    print(f"Козырь: {lead}\nНаша колода: {a}\nКолода противника: {b}\n")

    # Если в колоде есть козырная масть - ставим её в начало, чтобы быстрее получить ответ нет
    if lead in b:
        # print(b)
        b1 = {lead: b[lead]} if lead in b else {}
        b1.update({k: v for k, v in b.items() if k != lead})
        b = b1
        # print(b)

    # Проходим по всем мастям
    for i in b:
        cards = b.get(i)
        # Проходим по всем картам той или иной масти
        print(f"КАРТЫ ЭТОЙ МАСТИ: {cards}")
        for card in cards:
            print(f"{card}{i}")

            # Можем побить той же мастью
            if i in a and card <= a.get(i)[0]:
                print(a, b)
                our_card = a.get(i)[0]
                a[i].remove(our_card)
                # b[i].remove(card)
                print(f"Карта {our_card}{i} бьет {card}{i}")

            else:
                # Если у нас нет козырей или карта противника сама является козырем
                if i == lead or lead not in a:
                    print("НЕ МОЖЕМ ПОБИТЬ")
                    return ["NO"]
                # Иначе используем свой минимальный козырь
                else:
                    print("Иначе используем свой минимальный козырь")
                    print(f"Игрок 1 {a}, Игрок 2 {b}")

                    our_card = a.get(lead)[-1]
                    a[lead].remove(our_card)
                    # b[i].remove(card)

                    print(f"Карта {our_card}{lead} бьет {card}{i}")
                    print(f"Игрок 1 {a}, Игрок 2 {b}")
                    print("СЛЕДУЮЩАЯ КАРТА")

    print("КАРТ БОЛЬШЕ НЕТ")
    return ["YES"]


def main():
    n, m, lead, a, b = custom_read("../txtf/input.txt")
    # print(n, m, lead, a, b)

    if int(9) in b.get(lead):
        print("У противника есть коз. туз\n")
        output = ["NO"]
    else:
        print("У противника нет коз. туза\n")
        output = check(n, m, lead, clear_dict(a), clear_dict(b))

    print(f"{output}\n")
    write_file("../txtf/output.txt", output)


if __name__ == "__main__":
    import time
    import tracemalloc
    from lab1.defs import *

    t_start = time.perf_counter()
    tracemalloc.start()
    main()
    print(time.perf_counter() - t_start)
    print(tracemalloc.get_tracemalloc_memory() / 2 ** 20, "MB")