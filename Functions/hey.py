# write a function Hey
# By Doris

# take a number and output the squared parameter

def hey(number):
    return number ** 2

#not only am i giving the input but also verifying the output matches the expected result
def main():
    print("hey  5 **2 = 25 - is", hey(5) == 25)
    print("hey  0 **2 = 0  - is", hey(0) == 0)
    print("hey -3 **2 = 9  - is", hey(-3) == 9)

main()

# so rather than printing the output and manually verifying I am making the code do the verification for me


# Recommended testing helper
# def test_helper(actual, expected):
#     if actual == expected:
#         print(actual, "PASSED")
#     else:
#         print("ERROR", actual, "!=", expected)
#
# def hey(x):
#     return x ** 2
#
# # Testing
# def main():
#     test_helper(hey(5),   25)
#     test_helper(hey(0),    0)
#     test_helper(hey(-3),   9)
#     test_helper(there(5), 32)
#     test_helper(there2(0), 1)
#     test_helper(there(3),  8)
#     test_helper(there(-2), 0)
#     test_helper(there2(-6),0)
#     are_we(2, "there")
#     are_we2(3, "50")
#     are_we(1, "")
#     are_we2(0, "hey!")
#
# main()
