birthday={"ram": "1997-04-23", "hari": "1995-08-20"}
print("welcome to the birthday dictionary.we know the birthdays of")
for names in birthday:
    print(names)
print("who's birthday do want to look up?")
names= input()
if names in birthday:
    print("{}'s birthday is in {}".format(names,birthday[names]))
else:
    print("{}'s birthday is not found".format(names))
