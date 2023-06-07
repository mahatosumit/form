secret_number = 10
guess_count = 0
count_limit = 3
while guess_count < count_limit:
    guess = int(input("Guess the numer:"))
    guess_count += 1
    if guess == secret_number:
        print("You won!")
        break
    else:
        print("Sorry you failed!")
