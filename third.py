name1 = input("Enter first person name: ")

name2 = input("Enter second person name: ")

combined = name1+name2

combined_lower = combined.lower()

t = combined_lower.count("t")
r = combined_lower.count("r")
u = combined_lower.count("u")
e = combined_lower.count("e")

l = combined_lower.count("l")
o = combined_lower.count("o")
v = combined_lower.count("v")
e = combined_lower.count("e")

true = t+r+u+e
love = l+o+v+e

score = str(true)+str(love)

print(score)

