# Write a function are_we
# By Doris

def are_we(n,string):
    for i in range(0, n):
        print("Are we", string,"yet?", end='')
    print()

def main():
    are_we(2,"there")
    are_we(3,"50")
    are_we(1,"")
    are_we(0,"hey!")

main()



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
