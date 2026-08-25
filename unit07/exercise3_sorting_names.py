#Easy Sort a list of names alphabetically and print each name on a new line
random_names = [
    "Liam Smith", "Olivia Johnson", "Noah Williams", "Emma Brown", 
    "Oliver Jones", "Ava Garcia", "Elijah Miller", "Charlotte Davis", 
    "William Rodriguez", "Sophia Martinez", "James Hernandez", "Amelia Lopez", 
    "Benjamin Gonzalez", "Isabella Wilson", "Lucas Anderson", "Mia Thomas"
]

#I think the built in algorithm just sorts this alphabetically automatically
random_names.sort()

counter = 1
for name in random_names:
    print(f"{counter}.{name}")
    counter += 1