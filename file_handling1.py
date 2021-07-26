file = open('introduction.txt', 'r')

data = file.read()
#data1 = file.read(7)
print(data)
#print(data1)

#print(file.readline())

#x = file.readlines()
#print(x)

file.close()

with open('introduction.txt', 'r') as obj:
    print(obj.read())
