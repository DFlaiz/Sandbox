# calculating tips for a meal purchased


meal = 53.48
tax = 7
tip = 18
total = round(((meal * 7 / 100) + meal), 2)
total2 = round(((total * 18 / 100) + total), 2)

converted_total = str(total)
converted_total2 = str(total2)

print("Cost without tip: $" + converted_total)
print("Cost including tip: $" + converted_total2)