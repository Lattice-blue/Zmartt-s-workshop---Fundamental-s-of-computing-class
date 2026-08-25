#Indexing of strings
# word = "abc "
# new = word.strip()
# print(len(word))
# print(len(new))

# Replace method
# word = "cat cat"
# new = word.replace("c", "h")
# print(new) 

# word = "Programming"
# vowels = 0
# for character in word:
#     if character in "aeiou":
#         vowels += 1

# print(vowels)

# Exercises

# 1. ASk fora  word an print its first character, last character, and length
word = input("Enter word: ")
length = len(word)
first_char = word[0]
last_char = word[length - 1]

print(f"first character = {first_char}")
print(f"last character = {last_char}")
print(f"length = {length}")