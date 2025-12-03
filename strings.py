# strings.py
# Examples of Python string operations

# Creating strings
name = "Deekshi"
greeting = "Hello, " + name
print(greeting)

# String length
print("Length of name:", len(name))

# Indexing
print("First character:", name[0])
print("Last character:", name[-1])

# Slicing
print("First three letters:", name[:3])
print("Last three letters:", name[-3:])

# String methods
msg = "python programming"
print(msg.upper())
print(msg.capitalize())
print(msg.title())
print(msg.replace("python", "Python"))
print("Contains 'python'?", "python" in msg)

# Loop through string
for ch in name:
    print(ch)
