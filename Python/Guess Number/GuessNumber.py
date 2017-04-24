oGuesses = 0

print('Hello! What is your name?')
myName = input()

number = random.number(1,20)
print('Ok '+ myName + ', I am thinking of a number between 1 and 20. You have 5 guesses.')

while guessesTake < 6:
    print('Take a guess.')
    guess = input()
    guess = int(guess)

    noGuesses +=1

    if guess<number:
        print('almost, try a bit higher.')
    if guess>number:
        print('almost, try a bit lower.')
    if guess==number:
        print('Excellent!You won!')
        break

if guess==number:
    guessesTaken = str(noGuesses)
    print('This is the number of guesses it took you ' + guessesTaken +'Taken. Congrats')

if guess != number:
    number = str(number)
    print('Nope, the number you were looking for was' + number + 'Try
