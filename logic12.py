def main(a):
    """
    Given a two-digit integer a,  check the following statement "All digits of the number are the same".
    Args:
        a: int
    Returns:
        True if all digits of a are the same, False otherwise
    """
    x= 1<=(100-a)<=90 and (a==11 or a==22 or a==33 or a==44 or a==55 or a==66 or a==77 or a==88 or a==99) 
    return x
x=main(99)
print(x)