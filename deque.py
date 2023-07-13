from collections import deque

queue = deque([])

times = int(input())

for i in range(times):
    inp = input().split()

    if inp[0] == 'append':
        queue.append(inp[1])

    elif inp[0] == 'appendleft':
        queue.appendleft(inp[1])

    elif inp[0] == 'pop':
        queue.pop()

    elif inp[0] == 'popleft':
        queue.popleft()

    elif inp[0] == 'remove':
        queue.remove(inp[1])

    elif inp[0] == 'reverse':
        queue.reverse()

    elif inp[0] == 'rotate':
        queue.rotate(inp[1])

    elif inp[0] == 'extend':
        queue.extend(inp[1])

    elif inp[0] == 'extendleft':
        queue.extendleft(inp[1])

    elif inp[0] == 'clear':
        queue.clear()

final = ' '.join(queue)
print(final)
