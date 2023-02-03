# write function for pyramid
# by Doris
#
def pyramid(text, length):
    for i in range(0,length):
        for j in range(0, i+1):
            print(text, end="")
        print()

pyramid("* ", 2)
pyramid("* ", 5)
pyramid("* ", 10)


