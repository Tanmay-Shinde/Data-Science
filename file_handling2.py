with open('introduction.txt', 'r') as file:
    x = file.read(4)

y = 'Start' + x + x + 'End'

with open('exported.txt', 'w') as obj:
    obj.write(y)
