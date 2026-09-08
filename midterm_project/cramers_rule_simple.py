
# Simple version for the cramer's rule code implementation project


# TODO: Implement core logic for cramer's rule

# !!! ONLY COPY THE STUFF UNDERNEATH THIS COMMENT

# Sample equations:
# 2x + 3y = 8
# 1x + 4y = 9

# a1x1 + b1y1 = c1 
# a2x2 + b2y2 = c2



# expected values:
# x = 1
# y = 2

# Main deteriminant
# D = |a1 b1|
#     |a2 b2|
#
# x-determinant
# Dx = |c1  b1|
#      |c2  b2|
#
# y-determinant
# Dy = |a1 c1|
#      |a2 c2|

# x = Dx / D 
# y = Dy / D

# x should be 1
# and 
# y should be 2
 
# Determinant

def calc_main_determinant(a1, b1, a2, b2):
    return (a1 * b2) - (a2 * b1)

def calc_x_deteriminant(c1, b1, c2, b2):
    return (c1 * b2) - (c2 * b1)

def calc_y_deteriminant(a1, c1, a2, c2):
    return (a1 * c2) - (a2 * c1)

def calc_x(x_determinant, main_determinant):
    return x_determinant / main_determinant

def calc_y(y_determinant, main_determiniant):
    return y_determinant / main_determiniant


a1 = 2
b1 = 3
a2 = 1
b2 = 4

c1 = 8
c2 = 9

main_determinant = calc_main_determinant(a1, b1, a2, b2)
x_determinant = calc_x_deteriminant(c1, b1, c2, b2)
y_determinant = calc_y_deteriminant(a1, c1, a2, c2)

x = calc_x(x_determinant, main_determinant)
y = calc_y(y_determinant, main_determinant)

print(f"main determinant = {main_determinant}, x determinant = {x_determinant}, y determinant = {y_determinant}")

print(f"x = {x}, and y = {y}")