#!/usr/bin/env python3

from calcul import *
from info import *
import sys

def help():
    print("SYNOPSIS");
    print("    ./groundhog period\n");
    print("DESCRIPTION");
    print("    period the number of days defining a period");

def handlerror(arg):
    if len(arg) != 2:
        exit (84);
    if arg[1] == "-h":
        help()
        exit(0)

def openingfile():
    finput = open("./groundhog_example/trade_3.csv");
    stringnumber = finput.read().split("STOP");
    stringnumberlist = stringnumber[0].split('\n');
    numberlist = [];

    stringnumberlist.pop();
    for string in stringnumberlist:
        numberlist.append(float(string));
    return (numberlist);

def  fils_de_la_plage(current_closing_price, numberlist, slist, rlist, switchedCount, i, av):

    comparisons = 20
    user_input = current_closing_price
    switchedCount = 0
    # if user_input == 'STOP':
    #     break
    # else:
    # sys.stderr.write("You entered: {}\n".format(user_input))
    numberlist.append(float(user_input));
    av = average(numberlist, int(comparisons), len(numberlist) - 1);
    rlist.append(ratio(numberlist, int(comparisons), len(numberlist) - 1));
    slist.append(deviation(numberlist, int(comparisons), len(numberlist)));
    switchedCount = isSwitched(rlist, int(comparisons), len(numberlist) - 1);
    return (switchedCount, numberlist, slist, rlist, av);
    # print(f"{switchedCount}", file=sys.stderr)
    # print(f"{switchedCount}", end="")
    # weirdList.append(weirdness(numberlist, slist, int(comparisons), i));
    i += 1;

    # sys.stderr.write("Global tendency switched {} times\n".format(switchedCount))
    # weirdList = fiveWeirdest(weirdList, numberlist);
    # sys.stderr.write("{} Weirdest values are ".format(len(weirdList)))
    # sys.stderr.write(str(weirdList) + "\n")

# if __name__ == '__main__':
#     main()