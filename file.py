"""opens the file anudip.txt in write mode
fileobj = open("anudip.txt","w")
if fileobj:
    print("File Opened successfully")
    fileobj.close() #Closing the file object"""


"""with open("D:\\Demo\\abc.txt","w") as fileobj:
    fileobj.write("Good Afternoon")
    print("content write sucessfully")"""

"""with open("D:\\Demo\\abc.txt", "r") as file:
    content = file.read()
    print(content)"""


with open("D:\\Demo\\abc.txt","a") as fileobj:
    fileobj.write("How are you")
    print("Append content")
