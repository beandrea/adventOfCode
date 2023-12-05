def findAll(aStr, sub) -> None:
    start = 0
    while True:
        start = aStr.find(sub, start)
        if start == -1: 
            return
        yield start
        start += len(sub)

def main() -> None:
    numWords = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    with open('/Users/home/Desktop/python/adventOfCode/day1/day1part1/nums.txt') as f:
        line = f.read().split()
        final = []
        for e in line:
            indexes = {}
            for numWord in numWords:
                matches = list(findAll(e, numWord))
                for m in matches:
                    indexes[m] = nums[numWords.index(numWord)]
            for num in nums:
                matches = list(findAll(e, str(num)))
                for m in matches:
                    indexes[m] = num
            first = str(indexes[min(indexes)])
            first += str(indexes[max(indexes)])
            final.append(int(first))
    f.close()
    print(sum(final))

if __name__ == "__main__":
    main()