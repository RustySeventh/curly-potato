##
## EPITECH PROJECT, 2023
## groundhog-boot
## File description:
## info
##

import sys

def reprint(smthg, value):
    sys.stderr.write(smthg + "\n")
    return value

def isSwitched(rlist, periode, index):
    if index <= periode:
        return reprint("", 0)
    else:
        if rlist[index] > 0 and rlist[index - 1] > 0:
            return reprint("", 0)
        elif rlist[index] <= 0 and rlist[index - 1] <= 0:
            return reprint("", 0)
        elif rlist[index] <= 0 and rlist[index - 1] > 0:
            return reprint("\t\ta switch occurs [pos to neg]", -1)
        else:
            return reprint("\t\ta switch occurs [neg to pos]", 1)

# def fiveWeirdest(wlist, nlist):
#     weirdest = []
#     repetor = 5

#     while repetor != 0:
#         index = wlist.index(max(wlist))
#         weirdest.append(nlist[index])
#         wlist[index] = 0
#         repetor -= 1
#     return weirdest

# def printWeird(wlist, nlist):
#     for i in range(len(wlist)):
#         if wlist[i] != 0:
#             sys.stderr.write("valeur {:.2f}".format(nlist[i]))
#             sys.stderr.write(" wierdness {}\n".format(wlist[i]))
