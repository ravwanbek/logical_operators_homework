def main(a):
    """
    Given integer a,  check the following statement "The integer is three-digit number".
    Args:
        a: int
    Returns:
        True if a is three-digit number, False otherwise
    """
    x= 1<=(1000-a)<=900
    return x
x=main(15)
print(x)