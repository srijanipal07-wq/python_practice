# Check if a word is a vowel or consonant
word = input("Enter a word: ")

# Define vowels
vowels = "aeiouAEIOU"

# Check each letter in the word
for letter in word:
    if letter.isalpha():
        if letter in vowels:
            print(f"{letter} is a vowel.")
        else:
            print(f"{letter} is a consonant.")
    else:
        print(f"'{letter}' is not a valid letter.")