# First Exercise [Easy]
# print(5 + 2 * 3)
# print((5 + 2) * 3)
# print(17 // 5)
# print(17 % 5)

#2 Ask for an integer and print whether it is even - using the remainder operator
# def isEven(n):
#     return n % 2 == 0

# rand = [1,2,3,4,5,6,7,8,9]

# for n in rand:
#     if isEven(n):
#         print(f"{n} is even")
#     else:
#         print(f"{n} is odd")

#3 Ask for a score and print the Boolean result of 0 <= score <= 100

# def validRange(score):
#     return 0 <= score <= 100

# scores = [100, 200, 300, 40, 0, -100]

# for score in scores:
#     print(f"{score} is in valid range: {validRange(score)}")


#4 [Easy] Ask for total minutes and convert hours nad remaining minutes using // and %
# def formatTime(minutes):
    # hours = minutes // 60
    # minutes = minutes % 60
    # return f"hours: {hours}, minuts: {minutes}"
# 
# 
# print(formatTime(61))
# 

#5 [Medium] Given age and a boolean has_permission, create a Boolean expression for "age is at least 18 OR has permission."

# def validate(age, has_permission):
#     return age >= 18 or has_permission

# combination = [[20, False], [21, True], [15, True], [13, False]]

# for age, status in combination:
#     print(f"for age: {age} and status: {status}")
#     print(validate(age, status))

#6 [Hard] Write expressions to calculate compound interest A = P(1+r/n)**(nt).
# total = P * (1+r/n)**(n * t)
