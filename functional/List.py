class Cons():
    def __init__(self, data, nxt):
        self.data = data
        self.nxt = nxt

Nil = None

def new(*elems):
    if len(elems) == 0:
        return Nil
    else:
        return Cons(elems[0], new(*elems[1:]))

def printls(xs):
    i = xs
    while i != Nil:
        print(i.data)
        i = i.nxt
