# # day 6 go deeper exercise, still for loops
# # by Doris Flaiz
#
# #1
# for i in range(-16,16,4):
#     print(i, end='-')
# print(i+4)
# print()
#
# #2
for j in range(-10,102,10):
    print(j, end='|')
print()
#
# #3 sum10.py:
#
# sum_num = 0
# for i in range(10):
#     sum_num += eval(input("Please enter a real number and hit enter: "))
# print("Sum of numbers entered: ", sum_num)
sum = 0
for i in range(5):
	sum += eval(input('Please enter a grade: '))
avg= sum/5
print('Current average: ', avg)
print('25% improvement', avg + (avg*25/100))




