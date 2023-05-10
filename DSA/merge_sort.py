def merge_sort(arr):
	n = len(arr)
	mid = n // 2

	# base case
	if(n == 1):
		return arr

	else:
		left = arr[:mid]
		right = arr[mid:]

    # recursively sort left and right halves
		left = merge_sort(left)
		right = merge_sort(right)
		# merge the halves together

		return merge(left, right)

def merge(arr1, arr2):
	res =[]

	# pointer to keep track of iterations
	i, j = 0, 0

	while(i < len(arr1) and j < len(arr2)):
		if(arr1[i] < arr2[j]):
			res.append(arr1[i])
			i += 1
		else:
			res.append(arr2[j])
			j += 1

	#append any remaining elements to res
	res += arr1[i:] 
	res += arr2[j:]
	return res
