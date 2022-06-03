def reversed_binary_integer(num):
    intOfBinaryInversed = int(bin (num)[2:][::-1], 2)
    return intOfBinaryInversed


print(reversed_binary_integer(10))