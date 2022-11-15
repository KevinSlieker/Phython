word_without_vowels = ""

# Prompt the user to enter a word
# and assign it to the user_word variable.
user_word = input("Enter a word: ")
user_word = user_word.upper()

for letter in user_word:
    if letter == 'A':
        user_word= user_word.replace('A', '')
        continue
    elif letter == 'E':
        user_word= user_word.replace('E', '')
        continue
    elif letter == 'I':
        user_word= user_word.replace('I', '')
        continue
    elif letter == 'O':
        user_word= user_word.replace('O', '')
        continue
    elif letter == 'U':
        user_word= user_word.replace('U', '')
        continue
    else:
        word_without_vowels += letter
    
print(word_without_vowels)
    # Complete the body of the for loop.

# Print the word assigned to word_without_vowels.
