def main(a):
    """
    Given a three-digit integer a,  check the following statement "All digits sum is odd".
    Args:
        a: int
    Returns:
        True if all digits sum is odd, False otherwise
    """

    c1=a%10
    c2=(a%100-c1)/10
    c3=a//100
    c_sum=c1+c2+c3

    x= 1<=(1000-a)<=900 and c_sum%2!=0

    return x
x=main(96)
print(x)

