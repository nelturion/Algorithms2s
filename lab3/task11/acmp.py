from collections import deque, defaultdict

m = int(input())

moves = defaultdict(list)

for _ in range(m):
    from_substance, to_substance = input().split(' -> ')
    moves[from_substance].append(to_substance)

start = input()
target = input()


distances = {start: 0}

queue = deque([start])

while queue:
    current = queue.popleft()
    if current == target:
        print(distances[current])
        quit(0)

    for next_substance in moves[current]:
        if next_substance not in distances:
            distances[next_substance] = distances[current] + 1
            queue.append(next_substance)

print(-1)
