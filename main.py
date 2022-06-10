# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagrams(word1, word2):
    # [assignment] Add your code here
    strWord1 = word1.lower()
    strWord2 = word2.lower()

    if(len(strWord1) == len(strWord2)):

        sortW1 = sorted(strWord1)
        sortW2 = sorted(strWord2)

        if(sortW1 == sortW2):
            print("The words: ", word1, " and ", word2, " are anagrams!")
            return True
        else:
            print("The words: ", word1, " and ", word2, " are not anagrams!")
            return False
    
    else:
        print("The words: ", word1, " and ", word2, " are not anagrams!")
        return False

print("\nYOU ARE TO ENTER TWO WORDS TO CHECK IF THEY ARE ANAGRAMS!")
print("\nEnter the first word: ")
word1 = input()
print("\nEnter the secont word: ")
word2 = input()
print("\n")

find_anagrams(word1, word2)