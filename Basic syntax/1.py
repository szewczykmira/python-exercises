def sum_of_digits(number):
    if not number.isdigit():
        raise ValueError('This is not a number')
    return sum(int(digit) for digit in number)

if __name__ == '__main__':
    number = input('Provide number: ')
    print(sum_of_digits(number))
