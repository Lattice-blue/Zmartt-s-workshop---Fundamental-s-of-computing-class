#
# !!! DO NOT INCLUDE THESE COMMENTS WHEN YOU COPY MY PROJECT
# 
#  What the hell is cramer's rule?
# 
# The beginning, it starts with figuring out what values satisfy two linear equations. 
# 
# This is starting to get fun
# I understand it now




# TODO: Implement core logic for cramer's rule

# TODO: Implement GUI that uses the core logic for cramer's rule


# !!! ONLY COPY THE STUFF UNDERNEATH THIS COMMENT

# Sample equations:
# 2x + 3y = 8
# 1x + 4y = 9

# a1x1 + b1y1 = c1 
# a2x2 + b2y2 = c2

a1 = 2
b1 = 3
a2 = 1
b2 = 4

c1 = 8
c2 = 9

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
 

def calc_main_determinant(a1, b1, a2, b2):
    return (a1 * b2) - (a2 * b1)

def get_x_deteriminant():

    return 

def get_y_deteriminant():

    return

def calc_values():

    return

