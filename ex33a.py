from sys import argv

script, lmt, delta = argv

def at_the_top(lmt, delta):

    i = 0
    numbers = []

    while i < lmt:
        print('At the top i is %d' % i)
        numbers.append(i)

        i += delta
        print('Numbers now: ', numbers)
        print('At the bottom i is %d' % i)

    print('The numbers: ')

    for num in numbers:
        print(num)
