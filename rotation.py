def countRotations(arr, n):
	min = arr[0]
	min_index = 0
	for i in range(0, n):
	
		if (min > arr[i]):
		
			min = arr[i]
			min_index = i
		
	return min_index;


arr = [3, 6, 12,15, 18, 2 ]
n = len(arr)
print(countRotations(arr, n))

