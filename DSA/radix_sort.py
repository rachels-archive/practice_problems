# function to get the place value of a number 
# [place] parameter specifies the position of the digit to be returned
def get_digit(number, place):
	return (number // 10 ** place) % 10

def radix_sort(arr):

	# number of digits of largest number
	max_digit = len(str(max(arr)))
	
	# initialise base(radix)
	base = 10 

  # sort the elements into the bins according to its place
  # value in the current iteration
	bins = [[] for item in range(base)]

	# iterate through each digit, starting with LSD
	for i in range(max_digit):
		# iterate through each element in the list
		for x in arr:
			# extract the i-th digit starting from the right
			curr_digit = get_digit(x, i)

			# add the digits to the bins accordingly
			bins[curr_digit].append(x)
	
		# flatten the list of bins into a 1D array
		arr = [x for sub_list in bins for x in sub_list]

		# reset bins for next iteration of digits
		bins =  [[] for i in range(base)]

	return arr

print(radix_sort([38, 2, 100, 5, 276, 42])) # test case
# Output: [2, 5, 38, 42, 100, 276]
	
