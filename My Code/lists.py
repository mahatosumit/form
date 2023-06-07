'''numbers = [23, 555, 7876, 7654, 4566, 234567]
maxim = numbers[0]
for number in numbers:
    if numbers > maxim:
        maxim = number
print(maxim)'''

numbers = [34,56,755, 6765, 55,55,77,77,]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)