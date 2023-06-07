weight = int(input("Enter your weight \n:"))
unit = input('(L)bs or (K)g:\n')
if unit.upper() == "L":
    converted = weight*0.45
    print(f"You are{converted} kg")

else:
    converted = weight / 0.45
    print(f"You are{converted}pounds")
