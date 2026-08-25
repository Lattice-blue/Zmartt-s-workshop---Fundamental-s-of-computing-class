# 1. Ask for a  word an print its first character, last character, and length
word = input("Enter word: ")
length = len(word)
first_char = word[0]
last_char = word[length - 1]

print(f"first character = {first_char}")
print(f"last character = {last_char}")
print(f"length = {length}")