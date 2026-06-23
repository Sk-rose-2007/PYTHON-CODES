l=[101,80,50,60,30,5]
largest=l[0]
for i in l:
    if i>largest:
        largest=i
print(largest)

second_largest=0
for i in l:
    if i>second_largest and i!=largest:
        second_largest=i
print(second_largest)