def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1


while(True):
    print('This program will walk through the Collatz Sequence.')
    while(True):
        try:
            print('Enter an integer to begin from: ', end='')
            response = int(input())
        except ValueError:
            print('The value you entered was could not be converted to integer.')
            continue
        break

    notOne = True
    while(notOne):
        response = collatz(response)
        if response == 1:
            notOne = False

