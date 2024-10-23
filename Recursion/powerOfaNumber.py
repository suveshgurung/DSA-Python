def powerOfNumber(num, pow):
    assert (pow >= 0 and (int(pow) == pow)), "The power should be positive integer"
    if (pow == 0):
        return 1
    if (pow == 1):
        return num
    else:
        return (num * powerOfNumber(num, pow - 1))

print(powerOfNumber(3.2, 0))
