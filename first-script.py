# my first python script
the_world_is_flat = True

if the_world_is_flat:
	print("Be careful not to fall off!")
	print("I did it!")

text = ('Put several strings within parentheses '
        'to have them joined together.')

print(text)

a, b = 0, 1
while a < 100:
        if b < 100:
                print(a, end=',')
        else:
                print(a, end='')
        a, b = b, a+b
        
