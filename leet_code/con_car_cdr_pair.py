def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(func):
    def get_first_index(n1, n2):
        return n1
    return func(get_first_index)

def cdr(func):
    def get_last_index(n1, n2):
        return n2
    return func(get_last_index)




print(car(cons(1, 4)))
print(cdr(cons(1, 4)))