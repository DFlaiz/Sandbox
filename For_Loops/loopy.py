# Loopy control flow
# Emily Hill for CSCI 117 3 # Is each function fruitful or void?

def get_area(width, height):
    if width > 0 and height > 0:
        return width * height
    else:
        print("\tERROR: width & height should be > 0")
        if width <= 0:
            print("\t\twidth is", width)
        else:
            print("\t\theight is", height)
        return 0
def draw_line(number):
    for j in range(number):
        print("*", end='')
    print()

def rectangle_outline(width, height):
    for i in range(height):
        # if we’re printing the first or last line
        if i == 0 or i == height-1:
            draw_line(width)

        # otherwise, if we’re in the middle
        else:
            print("*", end='')
            for j in range(1, width-1):
                print(" ", end='')
            print("*")
w=25
h=10
print("The area of a %d x %d square is %d" % (w, h, get_area(w, h)))

rectangle_outline(w, h)

get_area(w * -1, h)
get_area(w, h * -1)

for s in range(5):
    draw_line(s)