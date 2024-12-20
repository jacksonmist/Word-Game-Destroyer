import spelling_bee
import anagrams
import wordle

SPELLING_BEE = 1
ANAGRAMS = 2
WORDLE = 3

def main():
    wordFile = open('complete_word_list.txt', 'r')
    selection = selection_menu()

    if selection == SPELLING_BEE:
        spelling_bee.main(wordFile)
    elif selection == ANAGRAMS:
        anagrams.main(wordFile)
    elif selection == WORDLE:
        wordle.main(wordFile)

def selection_menu():
    print("===============")
    print("1: Spelling Bee")
    print("2: Anagrams")
    print("3: Wordle")
    print("===============")    

    selection = int(input("Enter your selection: "))

    return selection

if __name__ == "__main__":
    main()