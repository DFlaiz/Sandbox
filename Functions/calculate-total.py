# write function for calculating total
# By Doris

# a meal: the cost of the meal
# b tax_rate: the percent tax(e.g., NJ tax would be 0.07)
# c tip_rate: the percent tip (e.g., a 20% tip rate is 0.20)p

def calculate_total(meal, tax_rate, tip_rate):
    calculate_total = meal + (meal * tax_rate) + (meal * tip_rate)
    print("Total price for meal, including both tax and tip =" , calculate_total)

calculate_total(53.48, .07, .18)

# meal = 53.48
# tax_rate = .07
# tip_rate = .18
#
# calculate_total = meal + (meal * tax_rate) + (meal * tip_rate)
# print(calculate_total)