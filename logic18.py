def main(a):
    """Given a five-digit integer a, check the following statement "All digits of the number are in descending order".
    Args:
        a: int
    Returns:
        True if all digits of a are in descending order, False otherwise
    """
    c1=a%10
    c2=int((a%100-c1)/10)
    c3=a//100-(a//1000)*10
    c4=(a//1000)-(a//10000)*10
    c5=a//10000
    x= 1<=(100000-a)<=90000 and (c1>c2>c3>c4>c5) 
    return x
x=main(98765)
print(x)