
# Check if palindrome
def palindrome(text: str):
    reversed = text[::-1]
    is_palindrome = True if reversed.lower() == text.lower() else False
    print(f'\nPalindrome: is the word the same if read backwards?\n{is_palindrome}\n{text}\n{reversed}\n')

# Check if anagram
def anagram():
    word_1 = input('First Text: ')
    word_2 = input('Second text: ')
    is_anagram: bool = sorted(word_1.lower()) == sorted(word_2.lower())   
    print(f'\nAnagram: can the letters in word 1 be rearranged to become word 2?\n{is_anagram}\n{word_1}\n{word_2}\n')
 

# Sort letters alphabetically
def sorting(text: str):
    print(f'\nSorting alphabetically the letters in {text}\n')
    for letter in sorted(set(text)):
        print(letter)

try:
    function_selector = input('[P] for palindrome checker, [A] for anagram checker, [S] for sorting algorithm, [E] to exit: ')
    if function_selector.upper() == "P":
        input_string = input('Text: ')
        palindrome(input_string)
    elif function_selector.upper() == "A":
        anagram()
    elif function_selector.upper() == "S":
        input_string = input('Text: ')      
        sorting(input_string)
    else:
        print("Exiting...")
except KeyboardInterrupt:
    print("Canceled")
except Exception as E:
    print("Error")