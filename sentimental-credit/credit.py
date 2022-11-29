# TODO

import re

def main():
    CC = get_card_info()
    CC = first_check(CC)
    CC = second_check(CC)
    CC = third_check(CC)


def get_card_info():
    cc = input("Number: ")
    return cc

def first_check(CC):

    pattern = '^[0-9]{13,16}$'
    pattern1 = re.compile(pattern)
    if re.search(pattern1, CC):
        return CC

    else:
        print("INVALID")


def second_check(CC):
    def digits_of(n):
        return [int(d) for d in str(n)]

    digits = digits_of(CC)

    odd_digits = digits[-1 : : -2]
    even_digits = digits[-2 : : -2]
    checksum = 0
    checksum += sum(odd_digits)

    for d in even_digits:
        checksum += sum(digits_of(d*2))

    if checksum%10 == 0:
        return CC

    else:
        print("INVALID")


def third_check(CC):
    amex_pattern = '^3[47][0-9]{13}$'

    Mastercard_pattern = '^5[1-5][0-9]{14}$'

    Visacard_pattern = '^4[0-9]{12,15}$'

    if re.search(amex_pattern, CC):
        print("AMEX")

    elif re.search(Mastercard_pattern, CC):
        print("MASTERCARD")

    elif re.search(Visacard_pattern, CC):
        print("VISA")

    else:
        print("INVALID")


main()
