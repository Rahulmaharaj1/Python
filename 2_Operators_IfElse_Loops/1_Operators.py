# ---------------------------------------
# Python Operators Examples
# ---------------------------------------

# Arithmetic Operators (गणितीय ऑपरेटर)
print("Arithmetic Operators")

print(5 + 6)   # Addition -> 11
print(5 - 6)   # Subtraction -> -1
print(5 * 6)   # Multiplication -> 30
print(5 / 2)   # Division -> 2.5
print(5 // 2)  # Floor Division -> 2
print(5 % 2)   # Modulus (remainder) -> 1
print(5 ** 2)  # Exponent (power) -> 25


# ---------------------------------------
# Relational Operators (Comparison)
# ---------------------------------------

print("\nRelational Operators")

print(4 > 5)   # False (4 greater नहीं है 5 से)
print(4 < 5)   # True
print(4 >= 4)  # True
print(4 <= 4)  # True
print(4 == 4)  # True (equal)
print(4 != 4)  # False (not equal)


# ---------------------------------------
# Logical Operators
# ---------------------------------------

print("\nLogical Operators")

print(1 and 0)   # AND -> दोनों true होने चाहिए
print(1 or 0)    # OR -> कोई एक true होना चाहिए
print(not 1)     # NOT -> value उलटी कर देता है


# ---------------------------------------
# Bitwise Operators (Binary level)
# ---------------------------------------

print("\nBitwise Operators")

print(2 & 3)   # Bitwise AND
print(2 | 3)   # Bitwise OR
print(2 ^ 3)   # Bitwise XOR
print(~3)      # Bitwise NOT
print(4 >> 2)  # Right Shift
print(5 << 2)  # Left Shift


# ---------------------------------------
# Assignment Operators
# ---------------------------------------

print("\nAssignment Operators")

a = 2
a %= 2   # a = a % 2
print(a) # result -> 0


# ---------------------------------------
# Membership Operators
# ---------------------------------------

print("\nMembership Operators")

print('D' not in 'Delhi')   # False (D Delhi में है)
print(1 in [2, 3, 4, 5, 6]) # False (1 list में नहीं है)


# ---------------------------------------
# Program: Sum of a 3 Digit Number
# ---------------------------------------

number = int(input("\nEnter a 3 digit number: "))

# Last digit निकालना
a = number % 10

# Last digit हटाना
number = number // 10

# Second digit निकालना
b = number % 10

# Last digit हटाना
number = number // 10

# Third digit निकालना
c = number % 10

# Sum of digits
print("Sum of digits:", a + b + c)