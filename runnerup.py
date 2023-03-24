# n = int(input())
arr = list(map(int, input().split()))
print(arr)
# Convert list to set and back to remove duplicates
# unique_list = list(set(arr))

# Sort the list in descending order
sorted_list = sorted(arr, reverse=True)

# Find the second highest number
max_num = sorted_list[0]
for num in sorted_list:
    if num != max_num:
        second_max = num
        break

# Print the second highest number
print("The second highest number in the list is:", second_max)
