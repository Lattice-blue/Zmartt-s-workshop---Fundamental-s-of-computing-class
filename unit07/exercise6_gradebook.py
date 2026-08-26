# Build a small gradebook that stores student names and three scores in parallel lists or a list of tuples
# then prints each avaerage and the class average. 
# Explain the limiation of your chosen structure

# What is a parallel list? 
# Anyways I think I should store a tuple for which the first value is the student name and the 
# second value is a list

student_scores = [
    ("Anna", [90, 89, 97]),
    ("Brian", [78, 82, 80]),
    ("Clara", [95, 100, 92]),
    ("David", [65, 70, 58]),
    ("Emma", [88, 91, 85]),
    ("Felix", [45, 52, 60]),
    ("Grace", [99, 96, 94]),
    ("Henry", [72, 75, 68]),
    ("Isabella", [84, 89, 93]),
    ("Jack", [30, 42, 55]),
    ("Karen", [91, 87, 90]),
    ("Leo", [79, 83, 76]),
    ("Maya", [100, 98, 95]),
    ("Noah", [62, 58, 64]),
    ("Olivia", [85, 88, 82]),
]

# What's the limitation of this structure?


# and then print the average, I guess I'll just create a new list of the average of each student
# and then use that list to create the class average

def calculate_averages(score_list):

    student_averages = []

    for student_score in student_scores:
        score_sum = sum(student_score[1])
        student_averages.append((student_score[0], round( score_sum / len(student_score[1]), 2)))

    return student_averages


def calculate_class_average(average_list):
    averages = []
    # extract all of the averages
    for element in average_list:
        averages.append(element[1])
    return round(sum(averages) / len(average_list) , 2)


averages = calculate_averages(student_scores)
print(averages)

#calc class average
class_average = calculate_class_average(averages)
print(f"class average: {class_average}")

