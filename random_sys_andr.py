import sys
import random

if len(sys.argv) < 3:
    sys.exit("Too few arguments")

elif len(sys.argv) > 3:
    sys.exit("Too many arguments")

elif len(sys.argv) == 3:
    try:
        lower_bound = int(sys.argv[1])
        upper_bound = int(sys.argv[2])
        guess = random.randint(lower_bound,upper_bound)
    except ValueError:
        sys.exit("Incorrect Paramters provided")
    while True:
        try:
            number = int(input("Guess the Number:"))
            if number == guess:
                print(f"Congratulations you have guessd the Number it is {guess}")
                break
            if number > guess:
                print("Too High")
            if number < guess:
                print("Too Low")
        except ValueError:
            print("Please Enter a Number")