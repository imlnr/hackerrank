def print_formatted(number):
    if number <= 99 and number >= 1:
        for i in range(1,number+1):
            print(i,end="  ")
            print(oct(i)[2:],end="  ")
            print(hex(i)[2:].upper(),end="  ")
            print(bin(i)[2:],end=" ")
            print(" ")
        return 
    else:
        return "please enter a number between 1-99."

# maincode
if __name__ =='__main__':
    n = int(input())
    out = print_formatted(n)
    print(out)
    