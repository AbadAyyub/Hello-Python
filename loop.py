secret_number=9
guess_count=0
max_guesses=3
while guess_count <=  max_guesses :
    number = int(input("Enter your guess"))
    guess_count+=1
    if number == secret_number:
        print("You won")
        break
else:
     print("Sorry you failed")

