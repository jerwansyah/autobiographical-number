#!/usr/bin/env python3
from datetime import datetime


def findAutobioNum(base):
    num = list()
    i = 0
    while True:
        while (i < base):
            # digit terakhir
            if base == 8:
                new = '{:o}'.format(int(oct(i), base=base))
            elif base == 16:
                new = '{:X}'.format(int(hex(i), base=base))
            else:
                new = i

            temp = list(num)
            if len(temp) == base:
                temp.pop()
            temp.append(str(new))

            if isPossible(''.join(temp), base):
                if len(num) == base:
                    num.pop()
                num.append(str(new))

                # print(''.join(num))

                if isAutobiographical(num, base):
                    return ''.join(num)
                else:
                    if len(num) == base:
                        if int(num[-1], base=base) == base-1:
                            i = base
                        else:
                            i = int(num[-1], base=base) + 1
                    else:
                        i = 0
            else:
                i += 1
        num = num[:-1]
        num = list(increment(''.join(num), base))
        i = 0


def isPossible(num, base):
    if not num.startswith("0") and len(num) <= base and\
        sumOfAllNonZeroDigits(num, base) <= base:
            return True
    return False


def sumOfAllNonZeroDigits(num, base):
    total = 0

    for _, digit in enumerate(num):
        total = total + int(digit, base=base)

    return total


def isAutobiographical(num, base):
    if len(num) == base and sumOfAllNonZeroDigits(num, base) == base:
        for position, digit in enumerate(num):
            if not num.count(str(position)) == int(digit, base=base):
                return False
        return True
    else:
        return False


def increment(num, base):
    if base == 8:
        return '{:o}'.format(int(num, base=base) + 1)
    elif base == 16:
        return '{:X}'.format(int(num, base=base) + 1)
    else:
        return str(int(num, base=base) + 1)


if __name__ == '__main__':
    basis = int(input("Masukan basis (8/10/16): "))
    while basis != 8 and basis != 10 and basis != 16:
        basis = int(input("Masukan basis (8/10/16): "))

    start = datetime.now()
    sol = findAutobioNum(basis)

    try:
        autonum = int(str(sol), base=basis)
        print("Autobiographical number dengan {}-angka dalam basis {}\t: ".format(basis, basis), end="")
        if basis == 8:
            print('{:o}'.format(autonum))
        elif basis == 16:
            print('{:x}'.format(autonum).upper())
        else:
            print('{}'.format(autonum))
        end = datetime.now()
        print(f'Waktu eksekusi\t\t\t\t\t\t: {end - start}')
    except ValueError:
        print("Galat kode")
