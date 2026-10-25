text = input("Enter a word: ")
# Convert to lowercase and remove spaces so only letters are counted
clean_text = text.lower().replace(" ", "")

frequency = {}

# Loop through each letter instead of words
for char in clean_text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print("\nLetter Frequency:")
for char, count in frequency.items():
    print(f"{char}-{count}")
