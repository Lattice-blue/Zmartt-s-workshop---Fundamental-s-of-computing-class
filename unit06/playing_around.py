# Indexing of strings
word = "abc "
new = word.strip()
print(len(word))
print(len(new))

# Replace method
word = "cat cat"
new = word.replace("c", "h")
print(new) 

word = "Programming"
vowels = 0
for character in word:
    if character in "aeiou":
        vowels += 1

print(vowels)


#WARNING: COMMENT OUT DIFFERENT PARTS BEFORE RUNNING



