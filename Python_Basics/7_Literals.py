# ---------------------------------------
# Python Literals Example
# ---------------------------------------

# Numeric Literals

# Binary Literal
a = 0b1010      # Binary number (base 2)

# Decimal Literal
b = 100         # Decimal number (base 10)

# Octal Literal
c = 0o310       # Octal number (base 8)

# Hexadecimal Literal
d = 0x12c       # Hexadecimal number (base 16)

print(a, b, c, d)

# ---------------------------------------
# Float Literals
# ---------------------------------------

float_1 = 10.5
float_2 = 1.5e2     # 1.5 × 10^2
float_3 = 1.5e-3    # 1.5 × 10^-3

print(float_1, float_2, float_3)

# ---------------------------------------
# Complex Literal
# ---------------------------------------

x = 3.14j
print(x)            # complex number
print(x.imag)       # imaginary part
print(x.real)       # real part

# ---------------------------------------
# String Literals
# ---------------------------------------

string = 'This is Python'
strings = "This is Python"
char = "C"

multiline_str = """This is a multiline
string with more than one line code."""

unicode_str = u"\U0001f600\U0001F606\U0001F923"
raw_str = r"raw \n string"

print(string)
print(strings)
print(char)
print(multiline_str)
print(unicode_str)
print(raw_str)

# ---------------------------------------
# Boolean Literal
# ---------------------------------------

a = True + 4
b = False + 10

print("a:", a)
print("b:", b)

# ---------------------------------------
# None Literal
# ---------------------------------------

k = None
print("Value of k:", k)

# ---------------------------------------
# Simple Program
# ---------------------------------------

a = 5
b = 6

print("Program executed")