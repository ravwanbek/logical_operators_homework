def main(a,b):
    """
    Given two integers a, b,  check the following statement "At least one  of the numbers 'a' and 'b' is negative".
    Args:
        a: int
        b: int
    Returns:
        True if at least one  of the numbers 'a' and 'b' is negative, False otherwise
    """
    x=a<0 or b<0 
    return x
x=main(-2,10)
print(x)