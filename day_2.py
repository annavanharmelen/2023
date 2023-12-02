from re import split

## Part 1
# get list of single games
game_record = open("input_day2.txt", "r").read().strip()
raw_games = [split(":|;", x) for x in split(": |\n", game_record)[1::2]]

# read each game into list of games containing dicts of sets
games = []
for game in raw_games:
    sets = []
    for set in game:
        cubes_in_set = split(", | ", set.strip())
        sets.append(
            {k: int(v) for (k, v) in zip(cubes_in_set[1::2], cubes_in_set[::2])}
        )
    games.append(sets)

# loop through games to find all possible ones
possible_games = []
max_colours = {"green": 13, "red": 12, "blue": 14}

for i, game in enumerate(games):
    possible = True
    for set in game:
        for colour in max_colours:
            if colour in set and set[colour] > max_colours[colour]:
                possible = False
    
    possible_games.append(i+1) if possible else None

print('Answer to part 1: ' + str(sum(possible_games)))

## Part 2
# Loop through games to calculate power of each game
powers = []

for game in games:
    minimums = {"red": 1, "green": 1, "blue": 1}

    for set in game:
        for colour in minimums:
            if colour in set and set[colour] > minimums[colour]:
                minimums[colour] = set[colour]

    powers.append(minimums["red"] * minimums["green"] * minimums["blue"])
    
print('Answer to part 2: ' + str(sum(powers)))
