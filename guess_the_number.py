n = 18
count = 9
print('You have 9 trials to guess the number')
for i in range(1,10):
    num1 = int(input('Guess the number between the range of 10 to 20 : '))
    if (num1 <= 14):
        print('Increase your number by a more difference')
        count = count - 1
        print('Number of guesses left : ',count)
    elif (15<=num1<=17):
        print('Increase your number by a little difference')
        count = count - 1
        print('Number of guesses left : ',count)
    elif (num1 == n):
        print('Congratulations! You have guess the correct number.')
        break
    elif (num1 >n and num1<21):
        print('Decrease your number by a little difference')
        count = count - 1
        print('Number of guesses left : ',count)
while (count == 0):
    print('Game Over! Better Luck Next Time.')
    break