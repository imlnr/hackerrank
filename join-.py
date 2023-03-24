def split_and_join(line):
    # write your code here
    out = line.split()
    output = "-".join(out)
    return output

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)