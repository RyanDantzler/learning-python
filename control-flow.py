# Control Flow
# ----------------

# if Statements

x = 0 #int(input("Please enter an integer: "))

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
#for user, status in users.copy().items():
#        if status == 'inactive':
#                del users[user]

# Strategy: Create a new collection
#active_users = {}
#for user, status in users.items():
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
#while True:
#        pass # Busy-wait for keyboard interrupt (Ctrl+C)

#class MyEmptyClass:
#        pass

#def initlog(*args):
#        pass # Remember to implement this!

# Defining Functions
def fib(n):
        a, b = 0, 1
        for i in range(n):
                print(a, end=' ')
                a, b = b, a+b
        print()

fib(10)
