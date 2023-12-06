digitMap = { 'oneight' : '18', 'twone' : '21', 'threeight' : '38', 'fiveight': '58',
            'sevenine' : '79', 'eightwo' : '82', 'eighthree' : '83', 'nineight' : '98',
            'one' : '1', 'two': '2', 'three' : '3', 'four' : '4', 'five' : '5', 
            'six' : '6', 'seven' : '7', 'eight' : '8', 'nine' : '9'}

def extract(line: str) -> int:
    for digit in digitMap:
        line = line.replace(digit, digitMap[digit])
    digits = [s for s in line if s.isnumeric()]
    return int(digits[0] + digits[-1])

def main() -> None:
    file = open('nums.txt', 'r')
    digits = [extract(l) for l in file.split()]
    print(sum(digits))

if __name__ == "__main__":
    main()