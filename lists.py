# lists.py
# Examples of Python List operations

# Creating a list
fruits = ["apple", "banana", "cherry"]
print("Fruits:", fruits)

# Accessing items
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Adding items
fruits.append("orange")
print("After append:", fruits)

# Inserting at index
fruits.insert(1, "grape")
print("After insert:", fruits)

# Removing items
fruits.remove("banana")
print("After remove:", fruits)

# Popping items
popped = fruits.pop()
print("Popped item:", popped)
print("List now:", fruits)

# Loop through list
for f in fruits:
    print(f)

# List comprehension
lengths = [len(f) for f in fruits]
print("Length of each fruit:", lengths)
