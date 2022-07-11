greeting = input("Greeting: ")

if greeting.lower().strip().find("hello") == 0:
    print('$0')
elif greeting.lower().find("h") == 0:
    print('$20')
else:
    print("$100")       