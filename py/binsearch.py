# binsearch.py
# Erwin Lara
# BINARY SEARCH 
# CSCI 77800 Fall 2022
# collaborators: 
# consulted: GeeksforGeeks, www.realpython.com, https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-1.php
# and Java Program from Summer

# Returns index of x in arr if present, else -1
def bin_Search(arr, lowPos, highPos, target):
  
	# Validate base case
	if highPos >= lowPos:

		mid = (highPos + lowPos) // 2
    
		if arr[mid] == target:
			return mid

		elif arr[mid] > target:
			return bin_Search(arr, lowPos, mid - 1, target)

		else:
			return bin_Search(arr, mid + 1, highPos, target)

	else:
		return -1

# Check the array
arr = [ 22, 3, 4, 10, 40,45,23 ]
target = 3

# Function call
result = bin_Search(arr, 0, len(arr)-1, target)

if result != -1:
	print("Element is present at index", str(result))
else:
	print("Element is not present in array")
