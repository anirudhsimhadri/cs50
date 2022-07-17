

while True:
    fuel = input("Fraction: ")
    try:
        x, y = fuel.split("/")
        x = int(x)
        y = int(y)
        output = round((x/y)*100)
        break
    except (ValueError, ZeroDivisionError):
        pass

if output <= 1:
    print("E")
elif output >= 99:
    print("F")
else:
    print(f"{output}%")



