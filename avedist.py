# def average(array):
#     # your code goes here
#     arr = []
#     for i in range(array):
#         arr.append(int(input()))
#     summation = sum(arr)
#     length = len(arr)   
#     print(summation,length)
# if __name__ == '__main__':
#     array = 5
#     average(array)
# n = int(input())  # Read the size of the list
# arr = list(map(int, input().split()[:n]))  # Read 6 integers but only store the first 5 in a list

# print(arr)  # Print the list to verify that it was read correctly

def average(array):
    # your code goes here
    arr2 = array[:n]
    no_duplicate = list(set(arr2))
    final_list = sum(no_duplicate) / len(no_duplicate)
    return "{:.3f}".format(final_list)
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    average(arr)