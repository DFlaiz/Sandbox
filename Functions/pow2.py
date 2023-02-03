# write function pow2
# By Doris


# Recommended testing helper
def test_helper(actual, expected):
    if actual == expected:
        print(actual, "PASSED")
    else:
        print("ERROR", actual, "!=", expected)

def pow2(n):
    return 2 ** n

# Testing
def main():
    test_helper(pow2(4),   8)
    test_helper(pow2(2),   4)
    pow2(4)
    pow2(2)


main()

#
# def pow2(num):
#     return num **2

