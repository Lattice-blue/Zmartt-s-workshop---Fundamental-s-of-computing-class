#Printing the numbers from 1 through 20 using a for loop
# for n in range(1, 21):
#     print(n)


#Printing all even numbers from 2 through 50.abs

# for n in range(1, 51):
#     if n % 2 == 0:
#         print(n)

# for n in range (2, 51, 2):
#     print(n)

#Printing the sum of 1 to n
# n = int(input("n: "))
# count = 0

# for n in range(1, n+1):
#     count += n

# print(count)


#Asking for five quiz socres using a loop, assuming valid asnwers, then printing the averages.
# scores = []
# for i in range(1, 6):
#     scores.append(int(input(f"score{i}? ")))

# total = 0
# for score in scores:
#     total += score

# print(f"average: {total / len(scores)}")

# answer = "a"

# while answer != "q":
#     print("Avocado Shake \nMilkshake")
#     answer = input(": ")

# import random

# randomNumber = random.randint(1,100)
# guess = -1

# while guess != randomNumber:
#     guess = int(input("guess: "))
#     if guess == randomNumber:
#         print("YOU WON")
#         break
#     else:
#         if guess < randomNumber:
#             print("Higher")
#         else:
#             print("Lower")


