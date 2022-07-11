# # name = input("What is your name?: ")
# name = "     ani simhadri      "
#
# name = name.strip()
# name = name.title()
#
# # f -> used for using curly braces {} within quotes of print statement
# print(f"Hello, {name}")
# print("Hello,", name)
#
# name.capitalize()

def main():
    name = input("What is your name?: ")
    hello(name)

def hello(to="world"):
    return f"hello, {to}"

if __name__ == "__main__":
    main()