def main():
    time = input("What time is it?: ")

    if 7.0 <= convert(time) and convert(time) <= 8.0:
        print("breakfast time")
    elif 12.0 <= convert(time) and convert(time) <= 13.0:
        print("lunch time")
    elif 18.0 <= convert(time) and convert(time) <= 19.0:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    minute = float(minutes)/60.0
    return float(hours) + minute

if __name__ == "__main__":
    main()