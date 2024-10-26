# Use of Euclidean algorithm.
# GCD of 48 and 18?
# 48/18 -> Quotient = 2, Remainder = 12
# 18/12 -> Quotient = 1, Remainder = 6
# 12/6 -> Quotient = 2, Remainder = 0
# Hence, 6 is the GCD.

def greatestCommonDivisor(n1, n2):
    assert (int(n1) == n1 and int(n2) == n2), "The numbers should be integer."

    if (n1 < 0):
        n1 *= -1
    if (n2 < 0):
        n2 *= -1

    remainder = n1 % n2
    if (remainder == 0):
        return n2
    else:
        return greatestCommonDivisor(n2, remainder)


print(greatestCommonDivisor(2, 3))
