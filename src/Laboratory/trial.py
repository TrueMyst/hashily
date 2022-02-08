#--------------------------- Nested List Function ---------------------------

# Here is a nested list :)
# nested = [[1, 2, 3], [4, 5], [6]]

# #Way 1: Traditional way, in short for loop
# new_array = []

# for items in nested:
#     for i in items:
#         new_array.append(i)

# print(new_array)

# # Way 2: Using list comprehensions
# print([i for items in nested for i in items])

# --------------------------- Enumerate ---------------------------

# fruits = ["apple", "banana", "orange", "jackfruit", "cherry"]
# print("".join(str([f"{i}) {items}" for i, items in enumerate(fruits, 1)])))


# numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
# print([i for i in numbers if i%2 == 0])

# --------------------------- Times Table ---------------------------
# print(i*6 for i in range(1, 12+1))


# --------------------------- Times Table ---------------------------