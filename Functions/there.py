# write function there
# By Doris

# number n and returns **2 if n = positive and 0 otherwise

def there(n):
    if n >= 0:
        return 2 ** n
    #else: is optional you can put it in or leave it out
    return 0

def main():
    print("input 0 = 32 - ", there(5) ==32)
    print("input 0 = 1 - ", there(0) ==1)
    print("input 3 = 8 - ", there(3) ==8)
    print("input -2 = 0 - ",there(-2) ==0)
    print("input -6 = 0 - ", there(-6) ==0)

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
