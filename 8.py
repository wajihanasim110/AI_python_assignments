#to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged
a=str(input("Enter a word or sentence"))
if len(a) > 2 and a[:2] == "Is":
    print(a)
else:
    print("Is " + a)
