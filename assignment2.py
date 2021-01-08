# checks if the given substring is within given string
def containsSubsequence (inputString, subString):
    count = 0
    maxCount = len(subString)
    result = ""
    doesContain = False
    for character in inputString:
        if character == subString[count]:
            count = count + 1
            result = result + character
            if count == maxCount:
                break
    if (result == subString):
        doesContain = True
    return doesContain        

# removes substring characters from input string
def subtractSub (inputString, subString):
    count = 0
    maxCount = len(subString)
    result = ""
    for character in inputString:
        if count == maxCount:
            result = result + character
        else:
            if character == subString[count]:
                count = count + 1
            else:
                result = result + character
    return result

# dictionary of number values between strings and ints
numStringToInt = {"0" : 0,
                  "1" : 1,
                  "2" : 2,
                  "3" : 3,
                  "4" : 4,
                  "5" : 5,
                  "6" : 6,
                  "7" : 7,
                  "8" : 8,
                  "9" : 9}

# converts numbers in a string to numbers in ints
def convertNumber (stringNum):
    numList = list(stringNum)
    intResult = 0
    multiplier = 1
    for strNum in reversed(numList):
        properInt = numStringToInt[strNum]
        intNumber = properInt * multiplier
        intResult = intResult + intNumber
        multiplier = multiplier * 10
    return intResult

# every n characters of a given string
def everyNChars (input, n):
    iterationVal = n
    result = ""
    for index in range (iterationVal - 1, len(input), iterationVal):
        result = result + input[index]
    return result

# string of the Nth character of each word in input string
def everyNthCharOfWord (input, n):
    inputList = input.split()
    charIndex = n - 1
    result = ""
    for word in inputList:
        if charIndex > len(word):
            addChar = " "
        else:
            addChar = word[charIndex]

        if (addChar.isalpha() or addChar.isspace()):
            result = result + addChar
    return result

# flips each word in given string but keeps word order the same 
def flipWords (inputString):
    result = ""
    inputList = inputString.split()
    for word in inputList:
        flip = word[ :  : -1]
        result = result + flip + " "
    return result
    
# checks if the first N characters of 2 strings are the same
def samePrefix (inputString, compString, n):
    numChars = 0
    inputPre = ""
    compPre = ""
    isSame = False

    if (n > len(inputString) or n > len(compString)):
        if (len(inputString) > len(compString)):
            numChars = len(compString)
        else:
            numChars = len(inputString)
    else:
        numChars = n
        
    for index in range (0, numChars):
        inputPre = inputPre + inputString[index]
        compPre = compPre + compString[index]
    if (inputPre == compPre):
        isSame = True
    return isSame

# returns the given string of given index values in a given string
def indexWord (inputString, indexString):
    result = ""
    for indexVal in indexString:
        numIndex = convertNumber(indexVal)
        addChar = inputString[numIndex]
        result = result + addChar
    return result
 
# removes extra spaces from a string
def removeExtraSpaces (inputString):
    foundSpace = False
    result = ""
    for char in inputString:
        if char.isalnum():
            if foundSpace == True:
                result = result + " " + char
                foundSpace = False
            else:
                result = result + char
        else:
            foundSpace = True
    return result.lstrip()