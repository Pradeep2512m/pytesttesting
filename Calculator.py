def add2no(x, y):
    return x+y
def sub2no(x, y):
    return x-y
def mul2no(x, y):
    return x*y
def div2no(x, y):
    return x/y

if __name__=="__main__":
    a=int(input("Enter 1st number:"))
    b=int(input("Enter 2nd number:"))

    add=add2no(a, b)
    sub=sub2no(a, b)
    mul=mul2no(a, b)
    div=div2no(a, b)

    print(add)
    print(sub)
    print(mul)
    print(div)

