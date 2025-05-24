data = str(input("Enter information to be stored in the file: "))

print("Data successfully written to output.txt")

file = open('output.txt','r+')
file.write(data+"\n")
file.close()

data_append = str(input("Enter additional text to be appended to output.txt: "))

file = open('output.txt','a')
file.write(data_append)
file.close()

print("Final contents of output.txt: ")

file = open('output.txt','r+')
print(file.read())
file.close()