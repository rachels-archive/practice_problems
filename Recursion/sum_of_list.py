# function to return the sum of every number in a list
def sum_of_list(list):
    # base cases
    if (len(list) == 0):
        return 0
    elif (len(list) == 1):
        return list[0]
    # recursive case
    else: 
        return list[0] + sum_of_list(list[1:])
    
# test cases
# print(sum_of_list([]))
# print(sum_of_list([1, 2, 3]))
