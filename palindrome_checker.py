import re

def palindrome_checker(sentence):
    cleaned=re.sub(r'[^a-zA-Z0-9]','',sentence)
    cleaned=cleaned.lower()

    return cleaned == cleaned[::-1]


user_input=input("Enter the sentence:")

if palindrome_checker(user_input):
    print("The sentence is a palindrome")
else:
    print("The sentence is not a palindrome")