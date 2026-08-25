def test1():
    full_name = input("What is your name? ")
    names = full_name.split(" ")
    initals = ""
    for name in names:
        initals =  initals + name[0]

    print(initals)
# This already works but what if the user accidentally inputs one of their name's first letter in lowecase?

#I'm just gonna use this name because I'm tired of typing out my name everyime I test the function
name = "zmartt remollo caracol"

def test2(name):
    full_name = name
    names = full_name.split(" ")
    initials = []
    for name in names:
        initials.append(name[0].upper())
    print("".join(initials))
    print(type("".join(initials)))



#Run one of the test here, or both
test2(name)