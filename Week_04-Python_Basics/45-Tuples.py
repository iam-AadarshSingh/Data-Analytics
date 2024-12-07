x = (40,41,42,561,456,789)
print(x)

print(type(x))
print(x[0])

(age, weight) = "17, 30".split(',')
print(age)
print(weight)

def square_info(x):
    a = x ** 2
    p = 4 ** x
    print("Area and Perimeter:")
    return a,p
square_info(3)