'''

In python i have two list
example
List1 = A,B,C,D,E,F
List2= A,B,C
In list1 i want to keep only elements which are equal to list2 elements rest elements we can remove

Yes. In Python, you want the intersection of two lists — keep only the elements from List1 that also exist in List2.

'''

print("\n")

list1 = ["A", "B", "C", "D", "E", "F"]
list2  = ["A", "B", "C"]

list1 = [x for x in list1 if x in list2]

# This is called a list comprehension in Python. 
# It is a short way of writing a loop that creates a new list.
# Easy pattern to remember

# Most list comprehensions follow this pattern:
# [what_to_store for variable in list if condition]

# So you can mentally read it as:

# "Give me x, for every x in List1, if x is in List2."

print(list1) # Output will be ['A', 'B', 'C']


# Another way to do this is by using the set intersection method:
print("\n")
list1 = list(set(list1) & set(list2)) 
print(list1) # Output will be ['A', 'B', 'C']


print("\n")
result = []
for x in list1:
    if x in list2:
        result.append(x)
print(result) # Output will be ['A', 'B', 'C']







