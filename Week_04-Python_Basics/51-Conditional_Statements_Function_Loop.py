def count(numbers):
    total = 0
    for x in numbers:
        if x < 20:
            total +=1
    return total


list_1 = [1, 3, 7, 5, 15, 100, 98, 56, 68]
print(count(list_1))