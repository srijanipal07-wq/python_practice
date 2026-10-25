#create Palindromic sequence using Python
def is_palindrome(seq):
    # Convert the sequence to string
    str_seq = str(seq)
    # Check if the string is equal to its reverse
    return str_seq == str_seq[::-1]
if __name__ == "__main__":
    # Get user input
    sequence = input("Enter a sequence to check if it's a palindrome: ")
    # Check if the sequence is a palindrome
    if is_palindrome(sequence):
        print(f"{sequence} is a palindrome.")
    else:
        print(f"{sequence} is not a palindrome.")