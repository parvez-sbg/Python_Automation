
def fib(n):
    a=0
    b=1

    if n<=0:
        print("invalid input")
    elif n==1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
                    c=a+b
                    a=b
                    b=c
                    print(c)
fib(n=int(input("enter a number:")))               