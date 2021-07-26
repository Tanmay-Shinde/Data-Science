# Create, Read, Update, Delete

a = list()
print(a)
print(type(a))

# # Create
# x = list() or x = []
# print(x)
# print(type(x))
x = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
z = ['Monday', 1, True, 'False', 'Tuesday', 2, 'Wednesday', 3]
# All of the above are valid lists

# # Read
print(x)
print(type(x))
print(len(x))

# Read by indexing
print(x[0])
print(x[17])

# Read by slicing
print(x[0:8])
print(x[2:9:2])

print(x.index('G'))

# # Update
x.append('New Alphabet')
x[6] = 'g'
del x[5]

print(x)
print(len(x))

# # Delete
del x
