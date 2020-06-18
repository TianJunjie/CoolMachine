# capital data
import string
# data ((0/1, X, Y), ....)
# 0 -> pen up, 1 -> pen down
# X -> x distance move
# Y -> y distance move


def A():
    data = ((1, 0, 2),
            (1, 0, -2),
            (1, 1, 0),
            (1, 0, 2),
            (1, 0, -1),
            (1, -1, 0),
            (1, 0, -1))
    return data


def B():
    data = ((1, 1, 0),
            (1, 0, 2),
            (1, -1, 0),
            (1, 0, -2),
            (1, 0, 1),
            (1, 1, 0),
            (1, -1, 0),
            (1, 0, -1))
    return data


def C():
    data = ((1, 1, 0),
            (1, 0, 2),
            (1, -1, 0),
            (0, 0, -2))
    return data


def D():
    data = ((1, 1, 0),
            (1, 0, 2),
            (1, -1, 0),
            (1, 0, -2))
    return data


def E():
    data = ((1, 1, 0),
            (1, 0, 1),
            (1, -1, 0),
            (1, 1, 0),
            (1, 0, 1),
            (1, -1, 0),
            (0, 0, -2))
    return data


def F():
    data = ((1, 1, 0),
            (1, 0, 1),
            (1, -1, 0),
            (1, 1, 0),
            (1, 0, 1),
            (0, -1, 0),
            (0, 0, -2))
    return data


def G():
    data = ((1, 1, 0),
            (1, 0, 2),
            (1, -1, 0),
            (1, 0, -1),
            (1, 1, 0),
            (0, -1, 0),
            (0, 0, -1))
    return data


def H():
    data = ((1, 0, 2),
            (1, 0, -1),
            (1, 1, 0),
            (1, 0, 1),
            (1, 0, -2),
            (0, -1, 0))
    return data


def I():
    data = ((1, 0, 2),
            (1, 0, -2))
    return data


def J():
    data = ((1, 0, 2),
            (1, 1, 0),
            (1, 0, -1),
            (0, -1, 0),
            (0, 0, -1))
    return data


def K():
    data = ((0, 1, 0),
            (1, 0, 2),
            (1, 0, -1),
            (1, -1, 0),
            (1, 0, 1),
            (0, 1, 0),
            (0, 0, -1),
            (1, -1, -1))
    return data


def L():
    data = ((0, 1, 0),
            (1, 0, 2),
            (1, -1, 0),
            (0, 0, -2))
    return data


def M():
    data = ((1, 2, 0),
            (1, 0, 2),
            (1, 0, -2),
            (1, -1, 0),
            (1, 0, 2),
            (1, 0, -2),
            (1, -1, 0),
            (1, 0, 2),
            (1, 0, -2))
    return data


def N():
    data = ((0, 0, 2),
            (1, 0, -2),
            (1, 1, 0),
            (1, 0, 2),
            (0, 0, -2),
            (0, -1, 0))
    return data


def O():
    data = ((0, 0, 1),
            (1, 0, 1),
            (1, 1, 0),
            (1, 0, -1),
            (1, -1, 0),
            (0, -0, -1))
    return data


def P():
    data = ((1, 1, 0),
            (1, 0, 2),
            (1, 0, -1),
            (1, -1, 0),
            (1, 0, -1))
    return data


def Q():
    data = ((1, 1, 0),
            (1, 0, 2),
            (1, -1, 0),
            (1, 0, -2),
            (1, 0, 2),
            (1, -0.5, 0.5),
            (0, 0.5, -0.5),
            (0, 0, -2))
    return data


def R():
    data = ((1, 1, 0),
            (1, 0, 2),
            (1, 0, -1),
            (1, -1, 0),
            (1, 0, -1),
            (1, 1, 0),
            (1, 0, 1),
            (1, -1, 1),
            (0, 1, -1),
            (0, -1, 0),
            (0, 0, -1))
    return data


def S():
    data = ((1, 1, 0),
            (1, 0, 1),
            (1, -1, 0),
            (1, 0, 1),
            (1, 1, 0),
            (0, -1, 0),
            (0, 0, -2))
    return data


def T():
    data = ((1, 2, 0),
            (1, -1, 0),
            (1, 0, 2),
            (0, 0, -2),
            (0, -1, 0))
    return data


def U():
    data = ((1, 0, 2),
            (1, 1, 0),
            (1, 0, -2),
            (0, -1, 0))
    return data


def V():
    data = ((1, 0, 1),
            (1, 1, 1),
            (1, 1, -1),
            (1, 0, -1),
            (0, -2, 0))
    return data


def W():
    data = ((1, 0, 2),
            (1, 1, 0),
            (1, 0, -2),
            (1, 0, 2),
            (1, 1, 0),
            (1, 0, -2),
            (0, -2, 0))
    return data


def X():
    data = ((1, 2, 2),
            (0, 0, -2),
            (1, -2, 2),
            (0, 0, -2))
    return data


def Y():
    data = ((1, 0, 1),
            (1, 2, 0),
            (1, 0, -1),
            (1, 0, 1),
            (1, -1, 0),
            (1, 0, 1),
            (0, 0, -2),
            (0, -1, 0))
    return data


def Z():
    data = ((0, 1, 0),
            (1, -1, 0),
            (1, 1, 1),
            (1, -1, 0),
            (0, 0, -1))
    return data


def _1():
    data = ((0, 0, 2),
            (0, 0, -2))
    return data


def _2():
    data = ((0, 1, 0),
            (1, -1, 0),
            (1, 0, 1),
            (1, 1, 0),
            (1, 0, 1),
            (1, -1, 0),
            (0, 0, -2))
    return data


def _3():
    data = ((0, 1, 0),
            (1, -1, 0),
            (1, 0, 1),
            (1, 1, 0),
            (1, -1, 0),
            (1, 0, 1),
            (1, 1, 0),
            (0, 0, -2),
            (0, -1, 0))
    return data


capitals = {
    "A": A,
    "B": B,
    "C": C,
    "D": D,
    "E": E,
    "F": F,
    "G": G,
    "H": H,
    "I": I,
    "J": J,
    "K": K,
    "L": L,
    "M": M,
    "N": N,
    "O": O,
    "P": P,
    "Q": Q,
    "R": R,
    "S": S,
    "T": T,
    "U": U,
    "V": V,
    "W": W,
    "X": X,
    "Y": Y,
    "Z": Z
}

def verify():
    caps = string.ascii_uppercase
    for cap in caps:
        data = capitals[cap]()
        xdis = 0
        ydis = 0
        for linexy in data:
            xdis = xdis + linexy[1]
            ydis = ydis + linexy[2]
        if xdis == 0 and ydis == 0:
            print("{} data is OK".format(cap))
        else:
            print("{} data is not OK".format(cap))



