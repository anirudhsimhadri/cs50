import re

def main():
    print(convert(input("Say something please: ")))

def convert(sample):
    sample = sample.replace(":)", "🙂")
    sample = sample.replace(":(", "🙁")
    return sample

main()


# FIX PROJECT

# Input:
#     Hello :) goodbye :)
# Output:
#     Hello HIHI goodbye HIHI