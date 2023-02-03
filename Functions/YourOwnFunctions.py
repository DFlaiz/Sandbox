# So you want to write your own functions, huh
# By Doris

def header(text, surround):
    length = len(text) +4
    # surround = "*"
    # text = "Hello, World!"

    print(surround * length)
    print(surround, text, surround)
    print(surround * length)

def main():
    header("Hello, World!", "*")
    #print()
    header("Python Rocks", "!")
    #print()
    header("Coders 4 EVER","+")
    header("HI!","#")

main()