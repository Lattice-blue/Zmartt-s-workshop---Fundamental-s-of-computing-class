user_input = input("Enter your sentence: ")
user_input = user_input.lower()
a_count = 0
for character in user_input:
    if character == "a":
        a_count += 1

print(a_count) 