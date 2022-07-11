def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(p):
    if len(p) < 2 or len(p) > 6:
        return False
    if p[0].isalpha() == False and p[1].isalpha() == False:
        return False
    count = 0
    while count < len(p):
        if p[count].isalpha() == False:
            if p[count] == "0":
                return False
            else:
                break
        count +=1
    for _ in p:
        if _ in [".", " ", "!", "?"]:
            return False
    return True

main()