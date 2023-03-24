N, M = map(int, input().split())

if M != N*3:
    print("please enter the value of M which is equvalent of N*3.")
    exit()

# Top part of the door mat
for i in range(N//2):
    pattern = '.|.'*(2*i+1)
    print(pattern.center(M, '-'))

# Middle part of the door mat with 'WELCOME' written in the center
print('WELCOME'.center(M, '-'))

# Bottom part of the door mat
for i in range(N//2-1, -1, -1):
    pattern = '.|.'*(2*i+1)
    print(pattern.center(M, '-'))
