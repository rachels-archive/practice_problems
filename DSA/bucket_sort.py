def bucket_sort(arr):

	bucket_size = 5 # depends on array range
									# bigger range => bigger buckets

	# ceiling division of range and bucket size to determine
	# number of buckets needed
	num_of_buckets = -(-(max(arr) - min(arr)) // bucket_size)
    
	# initialise array of empty buckets
	buckets = [[] for i in range(num_of_buckets)]
	
	start = min(arr)
	
	for num in arr:
		start = min(arr)
		
		if (num == start):
		    buckets[0].append(num) #append smallest number to first bucket
		 
		else:   
		    position = -(-(num - start) // bucket_size)
				
				# place each number into its corresponding bucket
		    buckets[position - 1].append(num)
	
  # sort the buckets
	buckets = [sorted(x) for x in buckets]
	
  # return the merged buckets(which is a sorted list)
	return [num for ls in buckets for num in ls]

array = [12, 33, 54, 98, 71, 23, 13, 39, 52] # test case
print(bucket_sort(array)) # Output: [12, 13, 23, 33, 39, 52, 54, 71, 98]
