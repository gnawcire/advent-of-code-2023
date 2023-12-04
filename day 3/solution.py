def part1():
    sum = 0
    coordinatesChecked = set()
    def getNumber(rowIndex, columnIndex, Lines):
        while columnIndex-1 >= 0 and Lines[rowIndex][columnIndex-1].isdigit():
            columnIndex -= 1
        number = ""
        while columnIndex < len(Lines[rowIndex]) and Lines[rowIndex][columnIndex].isdigit():
            # print("num char:" + Lines[rowIndex][columnIndex])
            coordinates = (rowIndex, columnIndex)
            if coordinates in coordinatesChecked:
                return 0
            coordinatesChecked.add(coordinates)
            number = number + Lines[rowIndex][columnIndex]
            columnIndex += 1
        print("Number added: " + number)
        return int(number)
    def checkNeighbors(rowIndex, columnIndex, Lines):
        nonlocal sum
        print("character to check neighbors:" + Lines[rowIndex][columnIndex])
        if rowIndex+1 < len(Lines):
            if Lines[rowIndex+1][columnIndex].isdigit():
                sum += getNumber(rowIndex+1, columnIndex, Lines)
        if rowIndex-1 >= 0:
            if Lines[rowIndex-1][columnIndex].isdigit():
                sum += getNumber(rowIndex-1, columnIndex, Lines)
        if columnIndex+1 < len(Lines[rowIndex]):
            if Lines[rowIndex][columnIndex+1].isdigit():
                sum += getNumber(rowIndex, columnIndex+1, Lines)
        if columnIndex-1 >= 0:
            if Lines[rowIndex][columnIndex-1].isdigit():
                sum += getNumber(rowIndex, columnIndex-1, Lines)
        if rowIndex+1 < len(Lines) and columnIndex+1 < len(Lines[rowIndex+1]):
            if Lines[rowIndex+1][columnIndex+1].isdigit():
                sum += getNumber(rowIndex+1, columnIndex+1, Lines)
        if rowIndex+1 < len(Lines) and columnIndex-1 >= 0:
            if Lines[rowIndex+1][columnIndex-1].isdigit():
                sum += getNumber(rowIndex+1, columnIndex-1, Lines)
        if rowIndex-1 >= 0 and columnIndex-1 >= 0:
            if Lines[rowIndex-1][columnIndex-1].isdigit():
                sum += getNumber(rowIndex-1, columnIndex-1, Lines)
        if rowIndex-1 >= 0 and columnIndex+1 < len(Lines[rowIndex+1]):
            if Lines[rowIndex-1][columnIndex+1].isdigit():
                sum += getNumber(rowIndex-1, columnIndex+1, Lines)
    file = open("input.txt", "r")
    Lines = file.readlines()
    
    for row, line in enumerate(Lines):
        # print(line)
        for column, c in enumerate(line):
            if not c.isdigit() and not c == "." and not c == " " and not c == "\n":
                checkNeighbors(row, column, Lines)
    return sum

def part2():
    sum = 0
    coordinatesChecked = set()
    def getNumber(rowIndex, columnIndex, Lines):
        while columnIndex-1 >= 0 and Lines[rowIndex][columnIndex-1].isdigit():
            columnIndex -= 1
        number = ""
        while columnIndex < len(Lines[rowIndex]) and Lines[rowIndex][columnIndex].isdigit():
            # print("num char:" + Lines[rowIndex][columnIndex])
            coordinates = (rowIndex, columnIndex)
            if coordinates in coordinatesChecked:
                return 0, 0
            coordinatesChecked.add(coordinates)
            number = number + Lines[rowIndex][columnIndex]
            columnIndex += 1
        print("Number added: " + number)
        return 1, int(number)
    def checkNeighbors(rowIndex, columnIndex, Lines):
        nonlocal sum
        numbers = []
        print("character to check neighbors:" + Lines[rowIndex][columnIndex])
        if rowIndex+1 < len(Lines):
            if Lines[rowIndex+1][columnIndex].isdigit():
                add, number = getNumber(rowIndex+1, columnIndex, Lines)
                if add == 1:
                    numbers.append(number)
        if rowIndex-1 >= 0:
            if Lines[rowIndex-1][columnIndex].isdigit():
                add, number = getNumber(rowIndex-1, columnIndex, Lines)
                if add == 1:
                    numbers.append(number)
        if columnIndex+1 < len(Lines[rowIndex]):
            if Lines[rowIndex][columnIndex+1].isdigit():
                add, number = getNumber(rowIndex, columnIndex+1, Lines)
                if add == 1:
                    numbers.append(number)
        if columnIndex-1 >= 0:
            if Lines[rowIndex][columnIndex-1].isdigit():
                add, number = getNumber(rowIndex, columnIndex-1, Lines)
                if add == 1:
                    numbers.append(number)
        if rowIndex+1 < len(Lines) and columnIndex+1 < len(Lines[rowIndex+1]):
            if Lines[rowIndex+1][columnIndex+1].isdigit():
                add, number = getNumber(rowIndex+1, columnIndex+1, Lines)
                if add == 1:
                    numbers.append(number)
        if rowIndex+1 < len(Lines) and columnIndex-1 >= 0:
            if Lines[rowIndex+1][columnIndex-1].isdigit():
                add, number = getNumber(rowIndex+1, columnIndex-1, Lines)
                if add == 1:
                    numbers.append(number)
        if rowIndex-1 >= 0 and columnIndex-1 >= 0:
            if Lines[rowIndex-1][columnIndex-1].isdigit():
                add, number = getNumber(rowIndex-1, columnIndex-1, Lines)
                if add == 1:
                    numbers.append(number)
        if rowIndex-1 >= 0 and columnIndex+1 < len(Lines[rowIndex+1]):
            if Lines[rowIndex-1][columnIndex+1].isdigit():
                add, number = getNumber(rowIndex-1, columnIndex+1, Lines)
                if add == 1:
                    numbers.append(number)
        if len(numbers) == 2:
            sum += numbers[0] * numbers[1]
    file = open("input.txt", "r")
    Lines = file.readlines()
    
    for row, line in enumerate(Lines):
        # print(line)
        for column, c in enumerate(line):
            if c == "*":
                checkNeighbors(row, column, Lines)
    return sum




def main():
    print(part1())
    print(part2())

if __name__ == "__main__":
    main()