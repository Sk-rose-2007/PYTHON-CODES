def countvowels(s):
    count = 0
    vowels = "aeiouAEIOU"

    for ch in s:
        if ch in vowels:
            count += 1

    return count

text = input("Enter a string: ")
print("Number of vowels:", countvowels(text))