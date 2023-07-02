def setoperations(sett,operations):
    for _ in range(operations):
        operation = input().split()

        if operation[0] == 'pop':
            if sett:
                sett.pop()
            else:
                return "Error: Set is empty"

        elif operation[0] == 'remove':
            if len(operation) != 2:
                return "Error: Invalid input"
            else:
                element = int(operation[1])
                try:
                    sett.remove(element)
                except KeyError:
                    return "Error: Element not found in set"

        elif operation[0] == 'discard':
            if len(operation) != 2:
                return "Error: Invalid input"
            else:
                element = int(operation[1])
                sett.discard(element)

        else:
            return "Error: Invalid operation"
        
    return sett

if __name__ == "__main__":
    n = int(input())
    sett = set(map(int, input().split()))
    operations = int(input())
    print(setoperations(sett,operations))