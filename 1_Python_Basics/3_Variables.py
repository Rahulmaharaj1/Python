# ---------------------------------------
# Static vs Dynamic Typing & Binding
# ---------------------------------------

# Python is a dynamically typed language
# Variable का type runtime पर decide होता है

name = "nitish"
print("Name:", name)

# ---------------------------------------
# Simple Variable Example
# ---------------------------------------

a = 5
b = 6

print("Sum:", a + b)

# ---------------------------------------
# Dynamic Typing
# ---------------------------------------
# Python में variable का type change हो सकता है

a = 5
print("Value of a:", a)

a = "nitish"   # अब a integer से string बन गया
print("New value of a:", a)

# ---------------------------------------
# Static Typing (Example from C/C++)
# ---------------------------------------
# C/C++ जैसी languages में type पहले declare करना पड़ता है

# int a = 5   # यह Python में valid नहीं है
# यह केवल C/C++ में होता है

# ---------------------------------------
# Dynamic Binding
# ---------------------------------------
# Python runtime पर variable को value से bind करता है

a = 5
print("Dynamic Binding Example:", a)

a = "nitish"
print("Dynamic Binding Changed:", a)

# ---------------------------------------
# Stylish Declaration Techniques
# ---------------------------------------

# Multiple variable declaration
a = 1
b = 2
c = 3
print("Multiple Variables:", a, b, c)

# Tuple unpacking (Pythonic way)
a, b, c = 1, 2, 3
print("Tuple Unpacking:", a, b, c)

# Same value assign to multiple variables
a = b = c = 5
print("Same Value Assignment:", a, b, c)