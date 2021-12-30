def main(a):
    """
    Given a two-digit integer a,  check the following statement "All digits sum is even".
    Args:
        a: int
    Returns:
        True if all digits sum is even, False otherwise
    """

    c1=a%10
    c2=a//10
    c3=c1+c2
    
    
    x= 1<=(100-a)<=90 and c3%2==0

    
    





    return x

x=main(100)
print(x)
    
