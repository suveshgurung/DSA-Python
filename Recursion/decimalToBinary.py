def decimalToBinary(n):
    assert (int(n) == n), "The number should be an integer"
    quotient = int(n / 2)
    if (quotient == 0):
        return (n % 2)
    else:
        return ((n % 2) + (10 * decimalToBinary(quotient)))


print(decimalToBinary(-13))
