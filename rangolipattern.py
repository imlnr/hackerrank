# N, M = map(int, input().split())

# if M != N*3:
#     print("please enter the value of M which is equvalent of N*3.")
#     exit()

# # Top part of the door mat
# for i in range(N//2):
#     pattern = '.|.'*(2*i+1)
#     print(pattern.center(M, '-'))

# # Middle part of the door mat with 'WELCOME' written in the center
# print('WELCOME'.center(M, '-'))

# # Bottom part of the door mat
# for i in range(N//2-1, -1, -1):
#     pattern = '.|.'*(2*i+1)
#     print(pattern.center(M, '-'))

# size = int(input())
# for i in range(1,size+1):
#     for j in range(1,i+1):
#         print("*",end =" ")
#     print()
def print_rangoli(size):
    import string
    alpha = string.ascii_lowercase
    n = size
    width = 4 * n - 3
    mid = width // 2
    res = []
    for i in range(n):
        left = "-".join(alpha[n-1:n-i-1:-1] + alpha[n-i-1:n])
        res.append(left[::-1] + left[1:])
    res = res[:n-1] + res[::-1]
    for i in res:
        print(i.center(width, '-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
