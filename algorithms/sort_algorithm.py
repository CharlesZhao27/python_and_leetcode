# Sort Algorithms in python


# Iterate everything and compare each individual
def bubbleSort(arr):
	length = len(arr)
	for i in range(length):
		for j in range(0,length-i-1):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
# Bubble sort TC: O(n**2), Space: O(1)s


# Select Minimum after current index, and swap position
def selectionSort(arr, n):
	for s in range(n):
		min_idx = s
		for i in range(s+1, n):
			if arr[i] < arr[min_idx]:
				min_idx = i
		arr[s],arr[min_idx] = arr[min_idx],arr[s]
	return arr
# SelectionSort TC: O(n**2), Space: O(1)



# Insertion_Sort
def insertionSort(arr):
	for i in range(1, len(arr)):
		a = arr[i]
		j = i-1
		while j >= 0 and a < arr[j]:
			arr[j+1] = arr[j]
			j -= 1
		arr[j+1] = a
	return arr





# Test
unsorted_array = [2,1,5,4,7,3]
insertionSort(unsorted_array)
print(unsorted_array)

