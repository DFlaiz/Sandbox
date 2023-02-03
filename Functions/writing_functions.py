# Introduction to writing functions
# file copy

def print_horiz_bar(pane_side_len, panes_across):
    for i in range(panes_across):
        print("+" + "-" * pane_side_len, end="")
    print("+")

def print_row_of_glass(pane_side_len, panes_across):
    for i in range(panes_across):
        print("|" + " " * pane_side_len, end="")
    print("|")

print_horiz_bar(3, 1)
print_row_of_glass(3, 3)
print_horiz_bar(7, 2)
print()
print_horiz_bar(4, 2)
print_row_of_glass(4,2)
print_row_of_glass(4,2)
print_horiz_bar(4, 2)
print()
print_horiz_bar(4, 2)
print_row_of_glass(9,1)
print_row_of_glass(9,1)
print_horiz_bar(4, 2)
print()
print_horiz_bar(4, 1)
print_row_of_glass(4, 1)
print_horiz_bar(4, 2)
print_row_of_glass(4, 2)
print_horiz_bar(4, 2)

# This program outputs the following:
# +---+
# |   |   |   |
# +-------+-------+

# Using only the functions defined above, write
# the python statements to print the following:

# Question 1:
# +----+----+
# |    |    |
# |    |    |
# +----+----+

# Question 2:
# +----+----+
# |         |
# |         |
# +----+----+

# Question 3:
# +----+
# |    |
# +----+----+
# |    |    |
# +----+----+