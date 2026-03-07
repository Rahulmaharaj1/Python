# Python is a case sensitive language
# इसका मतलब है कि Python में uppercase और lowercase अलग माने जाते हैं
# Example: name और Name दो अलग variables होंगे

# Print text
print('Hello World')   # स्क्रीन पर Hello World print करेगा

# Print celebrity name
print('salman khan')   # string को quotes में लिखना जरूरी होता है

# print(salman khan)   # ❌ यह error देगा क्योंकि quotes नहीं हैं

# Print integer number
print(7)   # integer number print करेगा

# Print decimal number
print(7.7)   # float number print करेगा

# Print boolean value
print(True)   # True boolean value print करेगा

# Multiple values print करना
print('Hello',1,4.5,True)  
# Output: Hello 1 4.5 True

# Separator change करना
print('Hello',1,4.5,True,sep='/')
# Output: Hello/1/4.5/True

# New line example
print('hello')
print('world')
# Output:
# hello
# world

# end parameter example
print('hello', end='-')
print('world')
# Output: hello-world