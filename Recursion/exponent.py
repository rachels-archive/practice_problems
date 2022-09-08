def exponent(a,b):
    if (b == 0):
        return 1
    elif (b == 1):
        return a
    else:
        return a * power(a, b-1)
    
# exponent(2,3) -> 2 to the power of 3
# print(exponent(2,3))
# print(exponent(5,0))
