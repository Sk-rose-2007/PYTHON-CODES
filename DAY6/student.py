import csv
f=open("C:\\PYTHON CODES\\DAY6\\engineer.csv","r")
data=csv.reader(f)
f1=open("C:\\PYTHON CODES\\DAY6\\engineer.txt","w")
data1=csv.writer(f1)
for i in data:
    data1.writerow(i)
print("Data has been written to engineer.txt,\nCheck the file in the directory!!!")
f.close()
f1.close()
