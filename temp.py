n = int(input())
sett = set(map(int, input().split()))

operations = int(input())

for _ in range(operations):
    operation = input().split()

    if operation[0] == 'pop':
        if sett:
            sett.pop()
        else:
            print("Error: Set is empty")

    elif operation[0] == 'remove':
        if len(operation) != 2:
            print("Error: Invalid input")
        else:
            element = int(operation[1])
            try:
                sett.remove(element)
            except KeyError:
                print("Error: Element not found in set")

    elif operation[0] == 'discard':
        if len(operation) != 2:
            print("Error: Invalid input")
        else:
            element = int(operation[1])
            sett.discard(element)

    else:
        print("Error: Invalid operation")

print(sett[0])
