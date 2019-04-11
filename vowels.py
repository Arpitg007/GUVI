i=input()
if i.isalpha():
    i.lower()
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        print("Vowels")
    else:
        print("Consonant")
else:
    print("Invalid")
