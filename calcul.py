##
## EPITECH PROJECT, 2023
## groundhog-boot
## File description:
## calcul
##

import statistics
import sys

def weirdness(numberlist, slist, period, index):
    limite = index - period + 1

    if index < period:
        print("\t\ts=nan", end="", file=sys.stderr)
    else:
        moyenne = sum(numberlist[limite:index]) / (period - 1)
        calcul = abs(numberlist[index] - moyenne)
        devia = statistics.pstdev(numberlist[limite:index])
        print("\t\ts={:.2f}".format(devia), end="", file=sys.stderr)
        return calcul / devia

def deviation(numberlist, period, index):
    limite = index - period
    result = 0
    newlist = []

    if index < period:
        print("\t\ts=nan", end="", file=sys.stderr)
    else:
        newlist = (numberlist[limite:index])
        result = statistics.pstdev(newlist)
        print("\t\ts={:.2f}".format(result), end="", file=sys.stderr)
    return result

def ratio(numberlist, period, index):
    number_one = 0
    number_two = 0
    result = 0

    # print(f"ratio-> index: {index}, period: {period}", file=sys.stderr)

    if index < period:
        print("\t\tr=nan%", end="", file=sys.stderr)
    else:
        number_one = numberlist[index]
        number_two = numberlist[index - period]
        result = ((number_one / number_two) - 1) * 100
        print("\t\tr={:.0f}%".format(result), end="", file=sys.stderr)
    return result

def average(numberlist, period, index):
    limite = index - period
    sublist = []
    result = 0
    sub = 0.0
    # print("n={}".format(numberlist[index]), end='', file=sys.stderr)
    # print(f"average -> index: {index}, period: {period}", file=sys.stderr)
    if index < period:
        print("g=nan", end='', file=sys.stderr)
    else:
        while limite < index:
            sub = numberlist[limite + 1] - numberlist[limite]
            sub = sub if sub > 0 else 0
            sublist.append(sub)
            limite += 1
        for number in sublist:
            result += number
        result /= period
        print("g={:.2f}".format(result), end='', file=sys.stderr)
    return result
