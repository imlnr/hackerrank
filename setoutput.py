n = int(input())
sett = set(map(int,input().split()[0:n]))
print(sett)
operations = int(input())
for i in range(operations):
    data = list(map(str, input().split()))

    if data[0] == 'pop' or data[0] =='POP' or data[0] =='Pop':
        sett.pop()
        print(sett)
    
    elif data[0] == 'remove' or data[0] =='Remove':
        sett.remove(data[1])
        print(sett)
    
    elif data[0] == 'discard' or data[0] =='Discard':
        sett.discard(data[1])
        print(sett)
    else:
        print("Key error:")