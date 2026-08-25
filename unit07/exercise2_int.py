#Easy
#Ask for five integers, store them in a list, and print min, max, and sum
#So it's asking for the smallets integer, largest integer, and the sum of all the integers.
#Schizo mode

ints = []
for i in range(1,6):
    ints.append(int(input("Enter an integer, or the program will break: ")))
ints.sort()
min = ints[0]
max = ints[len(ints) - 1]
#I'm pretty damn sure there's a method for this
# sum = 0
# for int in ints:
#     sum += int

# print(sum)

# I knew it

ints_sum = sum(ints)
print(ints_sum)