print("hello world")

# this is a comment
age = 20
name = "Alice"
sentence = "learn python programming"
long_string = """ The first name is Alice
She is 20 years old
"""
dash = "_ " * 20

print(dash)

print (sentence.title())

# conditional statements
temp = 24

if temp > 25:
    print ("It's a hot day!")
elif temp < 25:
    print("not hot")  
else:
    print("It's a nice day!") 

for i in range(5):
    print(i)         
# lists 
my_list = ["Alice", 25, age, True, 3.14]
name = my_list[-5]
print(name)
# dictionaries
person = {
    "name": "Alice",
    "age": 20,
    "is_student": True
}

print(person['name'])
print(person['age'])


print(person)
print(person.keys())
print(person.values())
print(person.items())

# Tuples
# Tuples are immutable, meaning their values cannot be changed after creation.
my_tuple = (1, 2, 3, 4, 5)
# for example, you cannot do my_tuple[0] = 10

# sets
scores = [90, 85, 92, 90, 88, 85]
unique_scores = set(scores)
print(unique_scores)


