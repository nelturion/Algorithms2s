def main():
    n, a = read_file("../txtf/input2.txt")
    a = length(a, n)
    output = count_lessons(a)
    write_file("../txtf/output.txt", output)

def length(a, n):
    for i in range(0, n):
        a[i].append(a[i][1]-a[i][0])
    return a

def count_lessons(a):
    count = 0
    a.sort(key = lambda x: (x[2], x[0]))
    print(f"List: {a}")
    end_point = 0
    while True:
        ok = False
        for i in range(0, len(a)):
            min_lenght = min(sub_arr[2] for sub_arr in a)
            print(min_lenght)
            if a[i][0] >= end_point:
                ok = True
                count += 1
                end_point = a[i][1]
                print(f"choosed: {a[i]}")
                a.pop(i)
                break
        if not ok:
            break
    print(f"Answer: {count}")
    return [count]



if __name__ == "__main__":
    import time
    import tracemalloc
    from lab1.defs import *

    t_start = time.perf_counter()
    tracemalloc.start()
    main()
    print(time.perf_counter() - t_start)
    print(tracemalloc.get_tracemalloc_memory() / 2 ** 20, "MB")