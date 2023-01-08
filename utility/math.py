def gcd(a: int, b: int) -> int:
    """
    gcd(a, b) returns the greatest common divisor
    between a and b
    """

    if b == 0:
        return a

    return gcd(b, a % b)


def lcm(a: int, b: int) -> int:
    """
    lcm(a, b) returns the least common multiple
    derived with the greatest common divisor
    """

    return a * b // gcd(a, b)
