def main(wordFile):
    initial_list = create_initial_list(wordFile)
    yellowLetter, letter1, letter2, letter3, letter4, letter5, letter6 = get_letters()
    wordList = create_second_list(initial_list, yellowLetter)
    
    finalList = create_final_list(wordList, yellowLetter, letter1, letter2, letter3, letter4, letter5, letter6)
    print_words(finalList)

def create_initial_list(wordFile):
    initialList = []
    for i in wordFile:
        if len(i.rstrip('\n')) >= 4:
            initialList.append(i.lower().rstrip('\n'))

    return initialList

def get_letters():
    yellowLetter = input("Enter yellow letter: ")
    letter1 = input("Enter grey letter 1: ")
    letter2 = input("Enter grey letter 2: ")
    letter3 = input("Enter grey letter 3: ")
    letter4 = input("Enter grey letter 4: ")
    letter5 = input("Enter grey letter 5: ")
    letter6 = input("Enter grey letter 6: ")

    return yellowLetter, letter1, letter2, letter3, letter4, letter5, letter6

def create_second_list(initialList, yellowLetter):
    wordList = []
    for i in initialList:
        if yellowLetter in i:
            wordList.append(i)
    
    return wordList
      
def create_final_list(wordList, yellowLetter, letter1, letter2, letter3, letter4, letter5, letter6):
    finalList = []
    isValid = True

    for word in wordList:
        for letter in word:
            if letter == yellowLetter or letter == letter1 or letter == letter2 or letter == letter3 or letter == letter4 or letter == letter5 or letter == letter6:
                pass
            else:
                isValid = False
                break
        if isValid:
                finalList.append(word)
        isValid = True
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

if __name__ =="__main__":
    main()