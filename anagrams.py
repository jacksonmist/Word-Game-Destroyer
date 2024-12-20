def main(wordFile):
    initial_list = create_initial_list(wordFile)
    letter1, letter2, letter3, letter4, letter5, letter6 = get_letters()
    secondList = create_second_list(initial_list, letter1, letter2, letter3, letter4, letter5, letter6)
    finalList = create_final_list(secondList, letter1, letter2, letter3, letter4, letter5, letter6)
    print_words(finalList)

def create_initial_list(wordFile):
    initialList = []
    for i in wordFile:
        if len(i.rstrip('\n')) >= 3 and len(i.rstrip('\n')) <= 6:
            initialList.append(i.lower().rstrip('\n'))

    return initialList

def get_letters():
    letter1 = input("Enter letter 1: ")
    letter2 = input("Enter letter 2: ")
    letter3 = input("Enter letter 3: ")
    letter4 = input("Enter letter 4: ")
    letter5 = input("Enter letter 5: ")
    letter6 = input("Enter letter 6: ")

    return letter1, letter2, letter3, letter4, letter5, letter6

def create_second_list(initialList, letter1, letter2, letter3, letter4, letter5, letter6):
    secondList = []
    isValid = True

    for word in initialList:
        for letter in word:
            if letter == letter1 or letter == letter2 or letter == letter3 or letter == letter4 or letter == letter5 or letter == letter6:
                pass
            else:
                isValid = False
                break
        if isValid:
                secondList.append(word)
        isValid = True
   
    return secondList

def create_final_list(secondList, letter1, letter2, letter3, letter4, letter5, letter6):
    finalList = []

    for word in secondList:
        validWord = True
        letter1Uses = 0
        letter2Uses = 0
        letter3Uses = 0
        letter4Uses = 0
        letter5Uses = 0
        letter6Uses = 0
        for letter in word:
            if letter == letter1 and letter1Uses < 1:
                letter1Uses += 1
            elif letter == letter2 and letter2Uses < 1:
                letter2Uses += 1
            elif letter == letter3 and letter3Uses < 1:
                letter3Uses += 1  
            elif letter == letter4 and letter4Uses < 1:
                letter4Uses += 1
            elif letter == letter5 and letter5Uses < 1:
                letter5Uses += 1
            elif letter == letter6 and letter6Uses < 1:
                letter6Uses += 1 
            else:
                validWord = False
        if validWord:
            finalList.append(word)
        else:
            continue
    
    return finalList

def print_words(finalList):
    sortedList = sorted(finalList, key=len)
    
    rowCount = 0
    print('=====================')
    for i in sortedList:
        print(f'{i}', end='\t')
        rowCount += 1
        if rowCount == 3:
            print('\n')
            rowCount = 0
    print('\n')
    print('=====================')

if __name__ == '__main__':
    main()