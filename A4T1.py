file_name = str(input("Enter file name: "))
try:
    file = open(file_name,'r+')
    line = file.readlines()
    line1 = line[0]
    line2 = line[1]
    print("Reading file content")
    print("Line 1: ",line1)
    print("Line 2: ",line2)
    file.close()
except FileNotFoundError:
    print("Error: File \'{}\' not found".format(file_name))