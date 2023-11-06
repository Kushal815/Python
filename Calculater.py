while True:
    def add(a,b):
        c=a+b
        return(c)
    def sub(a,b):
        c=a-b
        return(c)
    def mul(a,b):
        c=a*b
        return(c)
    def div(a,b):
        c=a/b
        return(c)

    n1=int(input("Enter 1st value: "))
    n2=int(input("Enter 2nd value: "))
    sin = input("Give a Operater + / - / * / / ")
    if "+" == sin:
        j=add(n1,n2)
    elif "-" == sin:
        j=sub(n1,n2)
    elif "*" == sin:
        j=mul(n1,n2)
    elif "/" == sin:
        j=div(n1,n2)

    print(j)
