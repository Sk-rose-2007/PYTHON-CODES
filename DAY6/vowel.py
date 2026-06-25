file = open("C:\\PYTHON CODES\\file.txt", "r")
data = file.read()
vowels = "aeiouAEIOU"
count = 0
for i in data:
    if i in vowels:
        count += 1
print("Number of vowels in the file:", count)
file.close()