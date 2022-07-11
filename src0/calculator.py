# x = float(input("what is x: "))
# y = float(input("what is y: "))
#
# z = round(x/y)
#
# print(f"{z:.2f}")
#
# # int(x)
# # str(x)
# # round(x)




def main():
    x = int(input("What's x?: "))
    print("x squared is", square(x))

def square(n):
    return n*n

if __name__ == "__main__":
    main()