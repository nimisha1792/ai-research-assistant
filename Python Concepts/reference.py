a = [1,2]
b = a
b.append(3)
print("a:",a)  # Output: [1, 2, 3]
print("b:",b)  # Output: [1, 2, 3]


x = 10
y = x
y = 20
print(x)
print(y)

a = [1, 2, 3]
b = a
c = a.copy()
b.append(4)

print("a:", a)  # Output: [1, 2, 3, 4]
print("b:", b) # Output: [1, 2, 3, 4]
print("c:", c) # Output: [1, 2, 3]

# Shallow Copy vs Deep Copy
a = [[1, 2], [3, 4]]
b = a.copy()
b[0].append(99)
print(a) # Output: [[1, 2, 99], [3, 4]]
print(b) # Output: [[1, 2, 99], [3, 4]]


# Shallow Copy vs Deep Copy (continued)
import copy
a = [[1, 2], [3, 4]]
b = a.copy()
c = copy.deepcopy(a)


# List Methods
nums = [1, 2, 3]
nums.append(4) # Output: [1, 2, 3, 4]
nums.insert(1, 100) # Output: [1, 100, 2, 3, 4]
nums.remove(2) # Output: [1, 100, 3, 4]
print(nums) # Output: [1, 100, 3, 4]

# Tuples 
point = (10, 20)
print(point[0])
# point[0] = 50 # This will raise a TypeError because tuples are immutable

# Sets - Sets Are Unordered
nums = {5, 1, 10}
print(nums)
#Common Operations on Sets
nums.add(100)
nums.remove(5)

# DICTIONARY
user = {
    "name": "Nimisha",
    "age": 25
}

print(user["name"]) #Access
user["city"] = "Bangalore" #Add
user["age"] = 26 #Update
print(user)
user.get("name") #Output: "Nimisha"
user.get("country", "Unknown") #Output: "Unknown"


# Functions Are Objects
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice")) # Output: "Hello, Alice!"