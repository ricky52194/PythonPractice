import random

def main():
    numSet = set()
    while len(numSet) < 5:
        num = random.randint(1, 69)
        if num not in numSet:
            numSet.add(num)
    sortedNums = sorted(numSet)
    for num in sortedNums:
        print(num)

    powerball = random.randint(1, 26)
    print("Powerball: " + str(powerball))

def run():
    for i in range(5):
        print("Ran " + str(i+1) + " time(s)")
        main()

run()