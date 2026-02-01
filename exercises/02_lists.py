"""
TODO:
1. Create list of favorite foods
2. Print first and last
3. Add one item
4. Remove one item
5. Print all items with loop
6. List comprehension for the lengths of each food item -
 create a new list where each item is  the length of the corresponding food item in the original list.
"""
"""
1.
"""
foods = ["cookies", "kugel", "chicken soup"]

"""
2.
"""
first_name=["Rikki"]
last_name=["Mann"]
print(first_name+last_name)

"""
3.
"""
foods.append("chicken")

"""
4.
"""
foods.remove("cookies")

"""
5.
"""
for n in foods:
    print(n)

"""
6.
"""
foods = ["apple", "banana", "cherry", "kiwi"]

lengths = [len(food) for food in foods]

print("Lengths of each food item:", lengths)