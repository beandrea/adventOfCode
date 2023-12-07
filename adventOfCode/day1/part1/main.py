digitMap = { 'oneight' : '18', 'oneightwo' : '182', 'twone' : '21', 'threeight' : '38', 'fiveight': '58',
            'sevenine' : '79', 'eightwo' : '82', 'eightwone' : '821', 'eighthree' : '83', 'nineight' : '98', 'nineightwo' : '982',
            'one' : '1', 'two': '2', 'three' : '3', 'four' : '4', 'five' : '5', 
            'six' : '6', 'seven' : '7', 'eight' : '8', 'nine' : '9'}

def extract(line: str) -> int:
    for digit in digitMap:
        line = line.replace(digit, digitMap[digit])
    with open('numRes.txt', 'a') as file:
        digits = [s for s in line if s.isnumeric()]
        x = int(str(digits[0]) + str(digits[-1]))
        print(digits, file=file)
        print(x, file=file)
    file.close()
    return x

def main() -> None:
    file = open('/Users/home/Desktop/python/adventOfCode/adventOfCode/day1/part1/nums.txt')
    digits = [extract(l) for l in file.read().split()]
    print(sum(digits))
    file.close()

if __name__ == "__main__":
    main()