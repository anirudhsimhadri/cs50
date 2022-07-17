def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    new = d.replace("$", "")
    return float(new)


def percent_to_float(p):
    new = p.replace("%", "")
    new_1 = float(new)/100
    return new_1

main()