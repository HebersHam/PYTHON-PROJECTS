import random
secret = random.randint(1,100)
print('Hello guess the number and you shall live')
guesses = 0
while True:
    guess = int(input('enter ye guess:'))
    guesses = guesses + 1
    if guess < secret:
        print('too low')
    elif guess> secret:
        print('too high')
    else:
        print('U win!! ' + str(guesses) + ' guesses used')
        break