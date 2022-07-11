x = float(input("What is x?: "))
y = float(input("What is y?: "))

def bigNum(a,b):
    if a<b:
        print(str(int(b)) + " is bigger")
    elif a>b:
        print(str(int(a)) + " is bigger")
    else:
        print( "both are same")

def equalToNot(a, b):
    # if a<b or b<a:
    if a!=b:
        print("x is not equal to y")
    else:
        print("x is equal to y")

equalToNot(x, y)