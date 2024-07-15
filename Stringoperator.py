#string concatination
str1 = "Hello, "
str2 = "World!"
result = str1 + str2
print(result) # the result will be "Hello, World!"
#repetation *operator
result1=str1*2
print(result1)
#membership opeartor
sentence = "This is a sample sentence."
check1 = "mohit" in sentence#false
print(check1)
check1 = "mohit"  not in sentence#true
print(check1) 
# string formating
name = "Alice"
age = 30
formatted_str = "My name is %s, and I am %d years old." % (name, age)
print(formatted_str)

formatted_str = "My name is {}, and I am {} years old.".format(name, age)
print(formatted_str) # formatted_str will be "My name is Alice, and I am 30 years old."

#strin comparision
str1 = "apple"
str2 = "banana"
result1 = str1 != str2
print(result1)# False

#traverse string
text = "Hello, World!"
index = 0
while index < len(text):
    char = text[index]
    print(char)
    index += 1

