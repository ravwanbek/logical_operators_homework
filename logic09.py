def main(a,b):
    """
    Given two integers a, b,  check the following statement "At least one of the numbers 'a' and 'b' is odd".
    Args:
        a: int
        b: int
    Returns:
        True if at least one of the numbers 'a' and 'b' is odd, False otherwise
    """
    x=a%2!=0 or b%2!=0 
    return x
x=main(3,2)
print(x)