# # Tuple

# Create
# x = tuple() or x = ()
# print(type(x))

x = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')

# # Read
print(x)
print(type(x))
print(len(x))
print(x.index('g'))

# Read by indexing
print(x[0])
print(x[17])

# Read by slicing
print(x[0:8])
print(x[2:9:2])

# # Update
# No update operation

# # Delete
# Individual elements cannot be deleted
del x
