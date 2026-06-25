import csv
f=open("studednt.csv","r")
data=csv.reader(f)
f1=open("studednt1.csv","w")
w=csv.writer(f1)
for i in data:
    w.writerow(i)
f1.close()
f.seek(0)

f2=open("studednt2.csv","w")
w2=csv.writer(f2)
for i in data:
    w2.writerow(i)
f2.close()
f.seek(0)

f3=open("studednt3.csv","w")
w3=csv.writer(f3)
for i in data:
    w3.writerow(i)
f3.close()
f.seek(0)