def main():
    #write your code below this line
    first = int(input('Give the first number:'))
    second = int(input('Give the second number:'))

    add = first + second
    minus = first - second
    times = first * second
    divide = first / second

    print(str(first) + ' + ' + str(second) + ' = ' + str(add))
    print(str(first) + ' - ' + str(second) + ' = ' + str(minus))
    print(str(first) + ' * ' + str(second) + ' = ' + str(times))
    print(str(first) + ' / ' + str(second) + ' = ' + str(divide))
if __name__ == '__main__':
    main()
