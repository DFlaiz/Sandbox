# calduate average of user input of 10 numbers
# by Doris Flaiz

sum_num = 0
cnt = 10
for i in range(cnt):
    sum_num += float(input("Please enter a real number and hit enter: "))
print("Sum of numbers entered: ", sum_num)
print("Average = ", sum_num / cnt)



