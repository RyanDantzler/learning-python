# Control Flow
# ----------------

# if Statements

x = 0  # int(input("Please enter an integer: "))

if x < 0:
        x = 0
        print('Negative changed to zero')
elif x == 0:
        print('Zero')
elif x == 1:
        print('Single')
else:
        print('More')

# for Statements

words = ['cat', 'window', 'defenestrate']
for w in words:
        print(w, len(w))

# Strategy: Iterate over a copy
# for user, status in users.copy().items():
#        if status == 'inactive':
#                del users[user]

# Strategy: Create a new collection
# active_users = {}
# for user, status in users.items():
#        if status == 'active':
#                active_users[users] = status

# range() Function

for i in range(5):
        print(i)

for i in range(5, 10):
        print(i)

for i in range(0, 10, 3):
        print(i)

for i in range(-10, -100, -30):
        print(i)

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
        print(i, a[i])

print(range(10))

print(sum(range(4)))

print(list(range(4)))

# break and continue Statements, and else Clauses on Loops

for n in range(2, 10):
        for x in range(2, n):
                if n % x == 0:
                        print(n, 'equals', x, '*', n//x)
                        break
        else:
                print(n, 'is a prime number')

for num in range(2, 10):
        if num % 2 == 0:
                print("Found an even number", num)
                continue
        print("Found an odd number", num)

# pass Statements
# while True:
#        pass # Busy-wait for keyboard interrupt (Ctrl+C)

# class MyEmptyClass:
#        pass

# def initlog(*args):
#        pass # Remember to implement this!

# Defining Functions


def fib(n):
        a, b = 0, 1
        for i in range(n):
                print(a, end=' ')
                a, b = b, a+b
        print()

fib(10)

f = fib
f(10)

print(fib(0))


def fib(n):
        result = []
        a, b = 0, 1
        for i in range(n):
                result.append(a)
                a, b = b, a+b
        return result

f10 = fib(10)
f10

result = [1]
result = result + [2]
result  # [1,2]

result.index(2)
result.remove(2)


def ask_ok(prompt, retries=4, reminder='Please try again!'):
        while True:
                        ok = input(prompt)
                        if ok in ('y', 'ye', 'yes'):
                                return True
                        if ok in ('n', 'no', 'nop', 'nope'):
                                return False
                        retries = retries - 1
                        if retries < 0:
                                raise ValueError('invalid user response')
                        print(reminder)

ask_ok('Would you like a cookie?')
ask_ok('Would you like a cookie?', 2)
ask_ok('Would you like a cookie?', 2, "What?! Yes or no.")

i = 5


def f(arg=i):
        print(arg)

i = 6
f()  # 5


def f(a, L=[]):
    L.append(a)
    return L

print(f(1))  # [1]
print(f(2))  # [1,2]
print(f(3))  # [1,2,3]


def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f(1))  # [1]
print(f(2))  # [2]
print(f(3))  # [3]


def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
        print("-- This parrot wouldn't", action, end=' ')
        print("if you put", voltage, "volts through it.")
        print("-- Lovely plumage, the", type)
        print("-- It's", state, "!")


parrot(1000)
parrot(voltage=1000)
parrot(voltage=10000, action='VOOOOM')
parrot(action='VOOOOM', voltage=10000)
parrot('a million', 'bereft of life', 'jump')
parrot('a thousand', state='pushing up the daisies')


def cheeseshop(kind, *arguments, **keywords):
        print("-- Do you have any", kind, "?")
        print("-- I'm sorry, we're all out of", kind)
        for arg in arguments:
                print(arg)
        print("-" * 40)
        for kw in keywords:
                print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

# -- Do you have any Limburger ?
# -- I'm sorry, we're all out of Limburger
# It's very runny, sir.
# It's really very, VERY runny, sir.
# ----------------------------------------
# shopkeeper : Michael Palin
# client : John Cleese
# sketch : Cheese Shop Sketch

# Dictionary

a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
f = dict({'one': 1, 'three': 3}, two=2)
print(a == b == c == d == e == f)


def standard_arg(arg):
        print(arg)


def pos_only_arg(arg, /):
        print(arg)


def kwd_only_arg(*, arg):
        """ some documentation

        No really, it's nothing.
        """
        print(arg)


def combined_example(pos_only, /, standard, *, kwd_only):
        print(pos_only, standard, kwd_only)

standard_arg(3)
standard_arg(arg=3)
pos_only_arg(4)
kwd_only_arg(arg=6)
combined_example(1, 2, kwd_only=3)
combined_example(1, standard=2, kwd_only=3)


def concate(*args, sep="/"):
        return sep.join(args)

print(concate("earth", "mars", "venus"))
print(concate("earth", "mars", "venus", sep="."))

list(range(3, 6))
args = [3, 6]
list(range(*args))


def parrot(voltage, state='a stiff', action='voom'):
        print("-- This parrot wouldn't", action, end=' ')
        print("if you put", voltage, "volts through it.", end=' ')
        print("E's", state, "!")

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)

# Function that returns a function


def make_incrementor(n):
        return lambda x: x + n

f = make_incrementor(42)
f(0)
f(1)

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda x: x[1])
print(pairs)
