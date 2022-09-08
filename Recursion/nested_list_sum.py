def nested_list_sum(input_list):
    sum = 0
    for element in input_list:
        # base case
        if(isinstance(element, list) == False):
            sum = sum + element
        # recursive case
        else:
            sum = sum + nested_list_sum(element)
    return sum
    
# test case
# print(nested_list_sum([[1,2], 2, [3,4],[5,6]]))
# print(nested_list_sum([]))
# print(nested_list_sum([1, 2, 3]))
