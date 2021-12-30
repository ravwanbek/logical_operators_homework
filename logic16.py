def main(a):
    """
    Given integer a,  check the following statement "The integer is a five-digit number".
    Args:
        a: int
    Returns:
        True if a is five-digit number, False otherwise
    """
    x=1<=(100000-a)<=90000
    return x
x=main(152)
print(x)