import re

def max_cubes(line: str, comparison_color: str) -> int:
    cubes = re.findall(r'(\d+) (\w+)', line)
    return max(int(count) for count, color in cubes if color == comparison_color)

def main():
    input_data = open('/Users/home/Desktop/python/adventOfCode/adventOfCode/day2/games.txt').read().splitlines()

    set_powers = []
    for game_id, line in enumerate(input_data, start=1):
        set_powers.append(max_cubes(line, 'red') *
                          max_cubes(line, 'green') * 
                          max_cubes(line, 'blue'))

    print(sum(set_powers))

if __name__ == '__main__':
    main()