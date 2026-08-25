#Hard exercise
#Build a text analyzer that reports total characters, words, vowels, digits, and spaces.
#Normalize nothing until after the original counts are computed.
#What does orignal counts are computed? 

#TODO:
#reports:
#total characters
#Doesn't this just use len?
#words, I guess I could use split
#vowels, I could just do a for loop
#digits, I could use isDigit at the same time as the vowel loop,
#spaces, well I could just the for loop too and check for ascii value or a string literal

#Normalize nothing until after the orignal counts are computed, I guess I should not normalize the input
#until after those metrics are measured, that won't matter for total characters I think,words, for vowels however, I could just
#check for uppercase characters and lowercase characters.



#My code before looking any solutions up on the internet:
def count_characters(text):
    char_count = 0
    for char in text:
        if char != " ":
            char_count += 1
    return char_count

def count_words(text):
    #how do I do this? Splitting in into a list using split()?
    #What if the user puts a space before and after the text?
    words = text.split(" ")    
    return len(words)

def count_vowels(text):
    #since the text is to be not normalized I'll have to check for upper case and lower case characters
    count = 0
    for char in text:
        if char in "aeiou" or char in "AEIOU":
            count += 1
    return count

def count_digits(text):
    count = 0
    for char in text:
        if char.isdigit():
            count += 1
    return count

def count_spaces(text):
    count = 0
    for char in text:
        if char == " ":
            count += 1
    return count

def analyze(text):
    #first the character count, I think this doesn't include the spaces, so I'd have to exlucde it. So a for loop?
    #I'd better put this in a separate function
    
    #get the character count
    #This is primitive though, does a tab count as a character?
    char_count = count_characters(text)

    #getting the words count
    #primitive function
    word_count = count_words(text)

    #getting the vowels
    vowel_count = count_vowels(text)

    #counting the digits
    digit_count = count_digits(text) 

    #counting the spaces
    space_count = count_spaces(text)

    #output here
    print(f"character count: {char_count}")
    print(f"word count: {word_count}")
    print(f"vowel count: {vowel_count}")
    print(f"digit count: {digit_count}")
    print(f"space count: {space_count}")
    return

#Running the analyzer

the_text = input(": ")
analyze(the_text)