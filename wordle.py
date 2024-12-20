import random

VOWELS = ['a', 'e', 'i', 'o', 'u']
lettersList = ['e', 't', 'a', 'i', 'n', 'o', 's', 'h', 'r', 'd', 'l', 'u', 'c', 'm', 'f', 'w', 'y', 'g', 'p', 'b', 'v', 'k', 'q', 'j', 'x', 'z']

def main(wordFile):
    initialList = create_initial_list(wordFile)

    attemptNum = 1
    wordStatus = [0] * 5
    word = ""
    for i in range(6):
        wordStatus, word = attempt_word(attemptNum, wordStatus, word, initialList)
        attemptNum += 1
    
    
def create_initial_list(wordFile):
    initialList = []

    for i in wordFile:
        if len(i.rstrip('\n')) == 5:
            initialList.append(i.rstrip('\n').lower())

    return initialList

def attempt_word(attemptNum, wordStatus, word, initialList):
    word = propose_word(attemptNum, wordStatus, word, initialList)
    wordStatus = check_word(word, wordStatus)

    return wordStatus, word


def propose_word(attemptNum, wordStatus, word, initialList):
    if attemptNum == 1:
        word = "soare"
    elif attemptNum == 2 and wordStatus == [0] * 5:
        word ="clint"
    else:
        word = word_engine(word, wordStatus, initialList)  
    
    return word


def check_word(word, wordStatus):
    print(f"Enter status of word: {word}")
    print("Grey = 0\tYellow = 1\tGreen = 2")

    for i in range(len(word)):
        numInput = int(input(f'{word[i]}: '))
        
        while numInput > 2 or numInput < 0:
            print("Please enter a valid number")
            numInput = int(input(f'{word[i]}: '))

        wordStatus[i] = numInput
        
    return wordStatus

def word_engine(word, wordStatus, initialList):
    isWordChanged = False
    vowelStatus = isVowel(word)
    wordFrame = [''] * 5
    for i in range(len(wordStatus)):
        if wordStatus[i] == 0:
            if word[i] in lettersList:
                lettersList.remove(word[i])           
        elif wordStatus[i] == 2:
            wordFrame[i] = word[i]
            if word[i] not in lettersList:
                lettersList.append(word[i])

    for i in range(len(wordStatus)):
        if wordStatus[i] == 1:
            if word[i] not in lettersList:
                lettersList.append(word[i])
            if i == 0 or i == 4:
                if vowelStatus[i]:
                    if wordFrame[1] =='':
                        wordFrame[1] = word[i]
                    elif wordFrame[2] =='':
                        wordFrame[2] = word[i]
                    elif wordFrame[3] =='':
                        wordFrame[3] = word[i]                       
                else:
                    if i == 0 and wordFrame[4] == '':
                        wordFrame[4] = word[i]
                    elif i == 4 and wordFrame[0] == '':
                        wordFrame[0] = word[i]
                    else:
                        for j in range(len(wordFrame)):
                            if wordFrame[j] == '' and j != 0:
                                print(word[i])
                                wordFrame[j] = word[i]
                                break

            else:
                if vowelStatus[i]:
                    if wordFrame[1] == '' and i != 1:
                        wordFrame[1] = word[i]
                    elif wordFrame[2] == '' and i != 2:
                        wordFrame[2] = word[i]
                    elif wordFrame[3] == '' and i != 3:
                        wordFrame[3] = word[i]
                    else:
                        for j in range(len(wordFrame)):
                            if wordFrame[j] == '':
                                wordFrame[j] = word[i]
                                break
                else:
                    if wordFrame[0] == '':
                        wordFrame[0] = word[i]
                    elif wordFrame[4] == '':
                        wordFrame[4] = word[i]
                    else:
                        for j in range(len(wordFrame)):
                            if wordFrame[j] == '' and j != 0:
                                wordFrame[j] = word[i]
                                break
    for i in range(len(wordStatus)):
        if wordStatus[i] == 1 or wordStatus[i] == 2:
            if word[i] not in lettersList:
                lettersList.append(word[i])
    
    print(wordFrame)
    print(lettersList)
    
    word, isWordChanged = check_against_list(initialList, wordFrame)

    acceptedWord = ''
    while isWordChanged == False:       
        wordFrame = shuffle_word(wordFrame)
        word, isWordChanged = check_against_list(initialList, wordFrame)

        acceptedWord = input("Accept Word? Enter anything to shuffle: ")
        while acceptedWord != '':
            wordFrame = shuffle_word(wordFrame)
            word, isWordChanged = check_against_list(initialList, wordFrame)
            acceptedWord = input(f"Accept Word [{word}]? Enter anything to shuffle: ")
    
    return word

def shuffle_word(wordFrame):
    random.shuffle(wordFrame)
    return wordFrame

def check_against_list(initialList, wordFrame):
    for i in initialList:
        matchedList = []
        if all(letter in lettersList for letter in i):
            print(i)
            for j in range(len(wordFrame)):
                if wordFrame[j] != '':
                    if wordFrame[j] == i[j]:
                        matchedList.append(True)
                    else:
                        matchedList.append(False)
        if all(matchedList) and len(matchedList) > 0 :    
            print(matchedList)           
            print("Found")
            isWordChanged = True
            word = i
            break
        else:
            isWordChanged = False
            word = ""
    
    return word, isWordChanged

def isVowel(word):
    vowelStatus = [False] * 5
    for i in range(len(word)):
        if word[i] in VOWELS:
            vowelStatus[i] = True
    
    return vowelStatus

if __name__ == "__main__":
    main()