# 11. Book Club Points
#
# Serendipity Booksellers has a book club that awards points 
# to its customers based on the number of books purchased each 
# month. The points are awarded as follows:
#
# • If a customer purchases 0 books, he or she earns 0 points.
# • If a customer purchases 1 books, he or she earns 5 points.
# • If a customer purchases 2 books, he or she earns 10 points.
# • If a customer purchases 3 books, he or she earns 20 points.
# • If a customer purchases 4 or more books, he or she earns 40 points.
#
# Write a program that asks the user to enter the number of books 
# that he or she has purchased this month, then displays the number of points awarded.
#
number_of_books = int(input("Enter the number of books: "))
message = ""

if number_of_books < 0:
    message = "Error. Enter a positive number. \n" + \
              "Re-run program and try again."
else:
    message = "You are awared "

    if number_of_books >= 0 and number_of_books <= 1:
        message += "0 "
    elif number_of_books >= 2 and number_of_books <= 3:
        message += "5 "
    elif number_of_books >= 4 and number_of_books <= 5:
        message += "10 "
    elif number_of_books >= 6 and number_of_books <= 7:
        message += "20 "
    elif number_of_books >= 8:
        message += "40 "

    message += "points."

print(message)
