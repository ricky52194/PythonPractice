import random
from datetime import date

def main():
    today = date.today()
    day = int(today.strftime("%d"))
    print(today.strftime("%m/%d/%y"))
    play_again = True
    while play_again:
        game = input("Which game? ")
        num_plays = int(input("How many games? "))
        if(game.lower() == 'powerball'):
            Powerball(num_plays,day)
        else:
            MegaMillions(num_plays,day)
        keep_playing = input('Play Again? Yes or No: ')
        if keep_playing.lower() == 'no':
            play_again = False

def Powerball(num_plays,day):
    count_games = 0
    while count_games < num_plays:
        nums = [num for num in range(1, 70)]
        selected_nums = []
        while len(selected_nums) < 5:
            for i in range(day):
                random.shuffle(nums)
            rand_num = random.choice(nums)
            selected_nums.append(rand_num)
            nums.remove(rand_num)
        print(f"Game {count_games + 1}: " + str(sorted(selected_nums)))
        powerball = random.choice([num for num in range(1,27)])
        print("Powerball: " + str(powerball))
        count_games += 1

def MegaMillions(num_plays,day):
    count_games = 0
    while count_games < num_plays:
        nums = [num for num in range(1, 71)]
        selected_nums = []
        while len(selected_nums) < 5:
            for i in range(day):
                random.shuffle(nums)
            rand_num = random.choice(nums)
            selected_nums.append(rand_num)
            nums.remove(rand_num)
        print(f"Game {count_games + 1}: " + str(sorted(selected_nums)))
        megaball = random.choice([num for num in range(1, 26)])
        print("Megaball: " + str(megaball))
        count_games += 1

main()
