# # Dictionary

# # Create
# x = dict() or x = {}
x = {
    'Suryansh': 20,
    'Vaishnavi': 20,
    'Keerthana': 22,
    'Pawan': 21,
    'Sanket': 23,
    'Simran': 19,
    'Abhishek': 18,
    'Vivek': 19
}

# # Read
print(x)
print(type(x))
print(len(x))

print(x['Sanket'])
print(x.keys())
print(x.values())

# # Update
x.update({'Omkar': 20})
x['Vivek'] = 23

# # Delete
del x['Abhishek']
del x
