def main(a,b,c):
    """
    Given three integers a, b, c,  check the following statement "The number b is between a and c".
    Args:
        a: int
        b: int
        c: int
    Returns:
        True if b is between a and c, False otherwise
    """



    x= a<b<c or a>b>c
    return x

x=main(1,8,10)
print(x)