#Lists and Tuples
#I get that a list is the equivalent of an array in JavaScript but what is a Tuple?

#Does pop remove using index or value? it removes using the index, WHY is that not written in the module?

# test = ["algebra", "calculus"]
# print(test.pop(0))

#I'm probably going to forget these list operators.

#VERY IMPORTANT CONCEPT: When assigning a list to another variable, it does not create a copy
#it only copies the reference.
#When a list is created in the computer's memory the variable only points to it,
#when you assign it to another variable they now point on the same list in the memory, 
#to illustrate:

variable1 = [1,2,3,4]
variable2 = variable1

variable2.append(5)

print(variable1)

# this will output [1, 2, 3, 4, 5]
# So variable1 wasn't copied into a new list in variable2, they are REFERENCING THE SAME LIST



# Was is Tuples? Tupolev?
# kind of like a fixed list. 
# Designed for a fixed structure of items. Like GPS coordinates (x,y)

test = (1,2,3)
print(test)
for val in test:
    print(val)
print(f"The first value in the tuple: {test[0]}")


#So this is a built in data type
#Its elements can be unpacked into individual variables
