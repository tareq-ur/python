
# total_run = 400
# total_wicket = 20

# if total_run < int (input("Enter your Run:")) :

#     print("Selected For Batsman")

# elif total_wicket <   int (input("Enter your wicket:")) : 
#     print("Selected for Allrounder")

# else:
#     print("Need more Practice") 




Number = int (input("Enter the number:"))


if Number % 3== 0 and Number % 5 == 0:
    print("FizzaBuzz")

elif Number % 3 == 0:
    print("Fizz")

elif Number % 5 == 0:
    print("Buzz")    


else:
    print("This not a FizzaBuzz number")    