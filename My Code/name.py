name = input("Enter your name")
if len(name)<= 3:
    print("Name is too short")
elif len(name)> 50 :
    print("Name must be maximum of 50 character looks good")
else:
    print("Name is sweet")