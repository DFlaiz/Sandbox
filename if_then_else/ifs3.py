# Learning if's and loops
# By Doris Flaiz

string = "hello"
length = 0
for char in string:
  length += 1
print(string, "length is ", length)
print()

mmm = 4
for i in range(10):
    if i % 3 == 0:
        mmm += 1
        print(i, "and ", mmm)
print(mmm)
print()

list = [2, 6, -3, 5]
total = 0
for x in list:
    if x > 0:
        total = total + x
        print(x, "and ",total)
print(total)
print()

x = 0
for j in range(-5,6):
    print("1 what is x?", x)
    if j >= 0:
        if j % 2 == 0:
            x += j
        else:
            x -= j
    else:
        if j % 5 == 0:
            print("3 what is x?", x)
            x *= -1 * j
            print("4 what is x?", x)
        x += j
        print("2 what is X? ", x)
        print("here is J = ",j, "and % 5", j % 5)
    print(j, "and ",x)
print(x)

