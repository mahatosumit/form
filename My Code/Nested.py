'''numbers = [5 , 2 , 5 , 2 , 5]
for x_count in numbers:
    print("X" * x_count)
    ###another method'''
numbers = [5 , 2 , 5 , 2 , 2]
for x_count in numbers:
    output = ""
    for count in range(x_count):
        output += "x"
        print(output)
