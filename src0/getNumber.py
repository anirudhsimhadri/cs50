def main():
    x = get_int("What is x?: ")
    print("x is", x)
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


main()