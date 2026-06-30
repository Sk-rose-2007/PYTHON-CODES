def sentence(s):
    vowels="aeiouAEIOU"
    b=" "
    dig=0
    vow=0
    cons=0
    space=0
    for i in s:
        if i in vowels:
            vow+=1
        elif i.isdigit:
            dig+=1
        elif i==b:
            space+=1
        else:
            cons+=1
    print(space)
a="python is"
sentence(a)
    