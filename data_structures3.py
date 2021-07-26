# # Set

# # Create
a = set()
x = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'}

# # Read
print(x)
print(type(x))
print(len(x))

# # Update
x.add('K')
print(x)
print(type(x))
print(len(x))

# # Delete
del x

# # Special Ability of Sets
cricket = {'Harsh', 'Chandana', 'Abhishek', 'Vennu', 'Swathi'}
hockey = {'Chandana', 'Abhishek', 'Vennu', 'Gurjot', 'Swathi'}
football = {'Gurjot', 'Keerthana', 'Gurpreet', 'Swathi'}

print(len(cricket))
print(len(hockey))
print(len(football))

print("Hockey but not football - ", hockey.difference(football))
print("Hockey or Cricket but not football - ", hockey.union(cricket).difference(football))
print("Only football - ", football.difference(cricket).difference(hockey))
print("Play everything - ", hockey.intersection(football).intersection(cricket))
print("Total players - ", hockey.union(football).union(cricket))
