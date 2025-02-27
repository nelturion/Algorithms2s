def read_file(path):
    with open(path, "r") as file:
        n = int(file.readline())
        a = []
        for i in range(0, n):
            a.append(list(map(int, file.readline().split(" "))))
    file.close()
    return n, a

def write_file(path, output):
    with open(path, "w") as file:
        for i in output:
            file.write(str(i))
            file.write("\n")
    file.close()