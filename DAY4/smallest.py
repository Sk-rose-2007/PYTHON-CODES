l= [10, 50, 20, 80, 30]

smallest = l[0]

for i in l:
    if i < smallest:
        smallest = i

print("Smallest =", smallest)