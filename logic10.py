def main(a):
    """
    Given integer a,  check the following statement "The integer is two-digit number".
    Args:
        a: int
    Returns:
        True if a is two-digit number, False otherwise
    """
    x= 1<=(100-a)<=90
    return x
x=main(66)
print(x)