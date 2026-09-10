#How tf am I suppposed to make this

#First principles
#The function crosses the horizontal at least once
#Using the graph as a heuristics to find the initial interval values
#Check if a of [a, b]  is negative and
#Check if b of [a, b] is positive using the function

#f(x) = x^3 - x - 2

#[1, 2]

# for a f(1) = 1^3 - 1 - 2 = 1 - 1 - 2 = 0 - 2 = -2 CHECK
# for b f(2) = 2^3 - 2 - 2 = 8 - 2 - 2 = 6 - 2 = 4 CHECK

# Intermediate Value Theorem
# f(1) * f(2) = (-2)(4) = -8 < 0 CHECK


#Do I implement the function too?
#I believe I can eventually become highly competent in this

def bisection(f, a, b, tolerance):
    #Fail fast version
    
    #If one of the values produces zero then that is the root of the function
    if f(a) == 0:
        return a
    if f(b) == 0:
        return b

    #If the Intermediate Value is positive that means the inerval is either above or below zero
    if f(a) * f(b) > 0:
        raise ValueError("f(a) and f(b) must have opposite signs.")


    #After those checks perform the bisection algorithm
    #First centering
    center = (a + b) / 2

    iteration = 0
    print(f"{'Iter':<6} | {'a':<10} | {'b':<10} | {'Midpoint (c)':<14} | {'f(c)':<12}")
    print("-" * 62)

    while abs(f(center)) > tolerance:
        iteration += 1
        # Print iteration row with fixed decimal precision
        print(f"{iteration:<6} | {a:<10.6f} | {b:<10.6f} | {center:<14.6f} | {f(center):<12.6e}")

        if f(a) * f(center) > 0:
            a = center
        else:
            b = center

        center = (a + b) / 2
    return center
    #once the value is within the tolerance range return the value.




# DEFINE the expression here

def func(x):
    # return x**3 - x - 2
    return 5 - x**3

# ASKS for the initial intervals
# NOTE: Use a graph to find the initial values visually

print("Enter interval vales for f(x) = x^3 - x -2")
a = int(input("a: "))
b = int(input("b: "))

#HARD CODED in the tolerance value
TOLERANCE = 1e-6

#RUNS the bisection algorithm
root = bisection(func, a, b, TOLERANCE)

#PRINTS the root
print(f"The root is: {root}")