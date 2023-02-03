# Writing input/output (I/O) Programs

# finding the users favorite movie and how much they like it

movie = input("What is your favorite movie? ")
q2 = "On a scale of 1 to 5, how would you rate that movie? "
rating = eval(input(q2))
mine = 5
print("I see that there is a differnce of", mine - rating, \
      "stars, because I chose", mine)
