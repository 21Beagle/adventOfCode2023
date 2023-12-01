f = open('day1/input.txt', "r")

lines = f.readlines()

def findFirstNumber(line):
    for i in line:
        try:
            character = int(i)
            return character
        except ValueError:
            continue

def findLastNumber(line):
    for i in line[::-1]:
        try:
            character = int(i)
            return character
        except ValueError:
            continue

def firstStar(lines):
    calibration = 0

    for line in lines:
        firstNumber = str(findFirstNumber(line))
        lastNumber = str(findLastNumber(line))
        output = int(firstNumber + lastNumber)
        calibration += output
     
     
    print(calibration)
    return calibration




def replaceTextNumberWithInt(line):
    number = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    replacementText = ["o1e", "t2o", "t3e", "f4r", "f5e", "s6x", "s7n", "e8t", "n9e"]
    
    # the whole replacement text seem silly but it accounts for the case 
    # where we have a letter shared by two numbers
    # eg twone contains both two and one but one would be replaced leaving tw1
    # so we replace one with o1e and two with t2o and it maintains the integrity of the string
    
    for i in range(len(number)):
        line = line.replace(number[i], replacementText[i])
    return line
    
def secondStar(lines):
    numberReplacedLines = []
    
    for line in lines:
        numberReplacedLine = replaceTextNumberWithInt(line)
        numberReplacedLines.append(numberReplacedLine)
    
    firstStar(numberReplacedLines)


firstStar(lines) # -> 54388

secondStar(lines) # -> 53515

# two stars complete