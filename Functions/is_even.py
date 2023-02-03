# tells if a number is even or odd
#by Doris

def is_even(num):
    if num % 2 == 0:
        print(num,"Is even")
    else:
        print(num,"Is Odd")

def main():
    print(is_even(2))
    print(is_even(5))
    print(is_even(22))
    print(is_even(101))
main()
