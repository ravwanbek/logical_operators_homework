def main(a,b):
    """
    Given two integers a, b,  check the following statement "Each of the numbers 'a' and 'b' is even".
    Args:
        a: int
        b: int
    Returns:
        True if each of the numbers 'a' and 'b' is even, False otherwise
    """

    x=a%2==0 and b%2==0 
    return x
x=main(2,10)
print(x)

