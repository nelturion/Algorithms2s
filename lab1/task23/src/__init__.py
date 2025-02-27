def main():
    n, m, lead, a, b = custom_read("../txtf/input.txt")
    print(n, m, lead, a, b)
    if ["A", lead] in b:
        output = ["NO"]
    else:
        output = check(n, m, lead, clear_dict(a), b)
    write_file("../txtf/output.txt", output)

def split_cards(line):
    line = line.strip()
    card_dict = {"S": [], "C": [], "D": [], "H": []}

    for i in range(0, len(line), 2):
        card, suit = line[i], line[i + 1]
        if suit in card_dict:
            card_dict[suit].append(int(card))

    return card_dict

def split_cards2(line):
    line = line.strip()
    return [[line[i+1], int(line[i])] for i in range(0, len(line), 2)]

def custom_read(path):
    with open(path) as file:
        n, m, lead = file.readline()[:-1].split(" ")
        a = split_cards(replaces(file.readline()).replace(" ", ""))
        b = split_cards2(replaces(file.readline()).replace(" ", ""))
        a = {k: sorted(v) for k, v in a.items()}
    file.close()

    return int(n), int(m), lead, a, b

def check(n, m, lead, a, b):
    print(a, b)
    for i in range(m):
        card = b[i]
        card_suit = card[0]
        card_rank = card[1]
        suit_pack = a.get(card_suit)
        lead_pack = a.get(lead)
        if card_suit in a and card_rank <= max(suit_pack):
            for j in range(len(suit_pack)):
                if suit_pack[j] >= card_rank:
                    print(f"До: {a}")
                    suit_pack.pop(j)
                    a.pop(card_suit)
                    a.update({card_suit: suit_pack})
                    print(f"После: {a}")


        # if card[1] in a:
    return ["NO"]

def clear_dict(a):
    a1 = a.copy()
    for i in a1:
        if not a1.get(i):
            a.pop(i)
    return a

def replaces(line):
    replacements = {"6": "1", "7": "2", "8": "3", "9": "4", "T": "5", "J": "6", "Q": "7", "K": "8", "A": "9"}
    return "".join(replacements.get(char, char) for char in line)

if __name__ == "__main__":
    import time
    import tracemalloc
    from lab1.defs import *

    t_start = time.perf_counter()
    tracemalloc.start()
    main()
    print(time.perf_counter() - t_start)
    print(tracemalloc.get_tracemalloc_memory() / 2 ** 20, "MB")