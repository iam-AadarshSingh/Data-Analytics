Toppers = ["Aadarsh", "Khushi", "Anshit", "Bikku"]

print(Toppers[1:3])
print(Toppers[:2])
print(Toppers[4:])
print(Toppers[-2:])

print(Toppers.index("Aadarsh"))

newComers = ["Anshit Singh", "Yatindra Krishna"]
print(newComers)

newToppers = [Toppers, newComers]
print(newToppers)

number = [78, 56, 45, 897, 123]
number.sort()
print(number)
number.sort(reverse=True)
print(number)