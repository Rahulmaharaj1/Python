# if-else examples
# 1. Find the min of 3 given numbers
# 2. Menu Driven Program

# Taking input from the user and converting it to integers
a = int(input('first num'))    # User inputs the first number
b = int(input('second num'))   # User inputs the second number
c = int(input('third num'))    # User inputs the third number

# Check if 'a' is smaller than both 'b' and 'c'
if a < b and a < c:
    print('smallest is', a)   # If true, 'a' is the smallest

# If the first condition is false, check if 'b' is smaller than 'c'
elif b < c:
    print('smallest is', b)   # If true, 'b' is the smallest

# If neither 'a' nor 'b' is the smallest, then 'c' must be the smallest
else:
    print('smallest is', c)   # 'c' is the smallest




    # Displaying a menu to the user and taking input
menu = input("""
Hi! How can I help you.
1. Enter 1 for pin change
2. Enter 2 for balance check
3. Enter 3 for withdrawal
4. Enter 4 for exit
""")

# Check the user's choice
if menu == '1':
    print('Pin change')       # If user enters 1
elif menu == '2':
    print('Balance')          # If user enters 2
else:
    print('Exit')             # Any other input (3, 4, or invalid) will go here