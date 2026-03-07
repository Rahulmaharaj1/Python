# ---------------------------------------
# Implicit vs Explicit Type Conversion
# ---------------------------------------

# Implicit Type Conversion (Automatic)
# Python automatically converts data type

print(5 + 5.6)  # int automatically converted to float
print(type(5), type(5.6))

# ---------------------------------------
# Explicit Type Conversion (Manual)
# ---------------------------------------

# Example that will cause error
# print(4 + '4')  # ❌ int + string allowed नहीं है

# Convert string to int
num = int("4")
print(4 + num)

# Convert int to string
a = str(5)
print("Converted to string:", a)
print(type(a))

# Convert int to float
b = float(4)
print("Converted to float:", b)
print(type(b))

# Complex number example
# int(4+5j)  # ❌ complex number को int में convert नहीं कर सकते