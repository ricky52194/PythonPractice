import random


def main(num_plays):
    count_games = 0
    game = input("Which game? ")
    while count_games < num_plays:
        if game.lower() == "powerball":
            nums = [num for num in range(1, 70)]
        else:
            nums = [num for num in range(1, 71)]
        selected_nums = []
        while len(selected_nums) < 5:
            rand_num = random.choice(nums)
            selected_nums.append(rand_num)
            nums.remove(rand_num)
        print(sorted(selected_nums))
        powerball = random.randint(1, 26)
        megaball = random.randint(1, 25)

        if game.lower() == "powerball":
            print("Powerball: " + str(powerball))
        else:
            print("Megaball: " + str(megaball))
        count_games += 1
        print("Ran " + str(count_games) + " time(s)")


main(5)
