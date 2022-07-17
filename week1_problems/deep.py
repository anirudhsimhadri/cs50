def main():
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything?: ")
    print(check(answer.lower().strip()))

def check(a):
    if a == "42" or a == "forty-two" or a == "forty two":
        return "Yes"
    else:
        return "No"

main()