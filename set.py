n = int(input())
X = set(map(int,input().split()[0:n]))
n = int(input())
y = set(map(int,input().split()[0:n]))
inter = X.difference(y)
print(len(inter))