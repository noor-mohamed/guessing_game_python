count = 0
guess = ''

answer = 'snake'

for i in range(6):
    count += 1;
    print('Enter your guess.')
    guess = input()
    if guess == answer:
        print('You\'re right the answer is ' + guess)
        break
    else:
        print('Wrong. The answer isn\'t ' + guess + '. Try again.')
        print('You\'ve used ' + str(count) + '/6 guesses.')
    
    if count == 6:
        print("You lost.")
        print('The answer was ' + answer + '.')
        break
