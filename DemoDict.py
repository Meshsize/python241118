

colors = {'apple':'red', 'banana':'yellow'}
print(colors)
print(colors['apple'])

colors['kiwi'] = 'green'
print(colors)

del colors['apple']
print(colors)

for item in colors.items():
    print(item)

colors.clear()

print(colors)

isRight = False
type(isRight)
print(1<2)
print(1!=2)
print(1==2)

print(True and True and False)
print(True or False or False)

bool(0)