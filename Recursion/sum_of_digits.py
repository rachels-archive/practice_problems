def sum_of_digits(num):
    if (num == 0):
        return 0
    else:
        digit = num % 10
        sum = digit + sum_of_digits(int(num / 10))
    return sum
    
# print(sum_of_digits(345))
