#Medium difficulty
#Create a simple password check that requires at least 8 characters and at least one digit

input_not_valid = True
usr_input = ""
while input_not_valid:
    usr_input = input("Create new password (must have at least 8 characters and contains a digit): ")
    if len(usr_input) >= 8:
        for char in usr_input:
            if char.isdigit():
                input_not_valid = False 
        print("Password must contain a digit")
    else:
        print("Password must be more than 7 characters")            
    


print("Password created successfully")

#I'm supposed to make tests for this and going through each step but I'm tired rn.