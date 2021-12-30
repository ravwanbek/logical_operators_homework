def main(a,b):
    """
    Given two integers a, b,  check the following statement "Each of the numbers 'a' and 'b' is negative".
    Args:
        a: int
        b: int
    Returns:
        True if each of the numbers 'a' and 'b' is negative, False otherwise
    """



    x= a<0 and b<0
    return x
x=main(-1,-5)
print(x)

