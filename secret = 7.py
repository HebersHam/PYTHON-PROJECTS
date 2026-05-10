secret = 7
print ("Guess the secret number my friend")
print ("type hint if u need a hint")
guess = input("what is your guess?").lower()
if guess ==("hint"):
    print("the numnber is a single digit")
elif int(guess)==secret:
    print("YOU GOT IT RIGHT")
else:
    print("WRONG ONE JACKASS")