

def part1():
    file = open("input.txt", "r")
    Lines = file.readlines()
    sum = 0
    for line in Lines:
        number = ""
        for c in line:
            if c.isdigit():
                number = number + c
                break
        for c in line[::-1]:
            if c.isdigit():
                number = number + c
                break
        sum = sum + int(number)
    return sum

def part2():
    def checkNumber(line, i):
        if line[i:i+3] == "one":
            return "1"
        elif line[i:i+3] == "two":
            return "2"
        elif line[i:i+5] == "three":
            return "3"
        elif line[i:i+4] == "four":
            return "4"
        elif line[i:i+4] == "five":
            return "5"
        elif line[i:i+3] == "six":
            return "6"
        elif line[i:i+5] == "seven":
            return "7"
        elif line[i:i+5] == "eight":
            return "8"
        elif line[i:i+4] == "nine":
            return "9"
        else:
            return "null"
    file = open("input.txt", "r")
    Lines = file.readlines()
    sum = 0
    for line in Lines:
        # print(line)
        number = ""
        for i, c in enumerate(line):
            if c.isdigit():
                number = number + c
                break
            elif checkNumber(line, i) != "null":
                number = number + checkNumber(line, i)
                break
                
        for i in range(len(line) - 1, -1, -1):
            if line[i].isdigit():
                number = number + line[i]
                break
            elif checkNumber(line, i) != "null":
                number = number + checkNumber(line, i)
                break
        sum = sum + int(number)
        # print(number)
    return sum
def main():
    print(part1())
    print(part2())

if __name__ == "__main__":
    main()