import re

def max_cubes(line: str, comparison_color: str) -> int:
    cubes = re.findall(r'(\d+) (\w+)', line)
    return max(int(count) for count, color in cubes if color == comparison_color)

def main():
    input_data = open('/Users/home/Desktop/python/adventOfCode/adventOfCode/day2/games.txt').read().splitlines()

    possible_game_ids = []
    for game_id, line in enumerate(input_data, start=1):
        if max_cubes(line, 'red') <= 12 and max_cubes(line, 'green') <= 13 and max_cubes(line, 'blue') <= 14:
            possible_game_ids.append(game_id)

    print(sum(possible_game_ids))

if __name__ == '__main__':
    main()