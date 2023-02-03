# Ifs, loops and calling functions
# By Doris Flaiz

x = -3
for i in range(-5,6):
    if i > 0:
        if i % 2 ==1:
            x += 3
            print("1", i,  x)
        else:
            x *= 2
            print("2", i, x)
    elif i % 4 == 0:
        x += i
        print("3", i, x)
    else:
        x -= 1
        print("4", i, x)
print(x)