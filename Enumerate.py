'''
The enumerate() function in Python is a built-in tool that allows you to loop through an iterable (like a list, tuple, or string) 
while automatically keeping track of the index (position) of each item. It eliminates the need to manually create and increment 
a counter variable outside your loop.



Basic Syntax

python
enumerate(iterable, start=0)


• iterable: Any object that supports iteration (e.g., list, tuple, string, dictionary).
• start (optional): The integer value from which the counter begins. It defaults to 0.



1. Standard Loop (Starting at Index 0)

By default, enumerate() pairs each item with a zero-based index. You can unpack these into two variables 
(typically index and item) directly in the loop header.

'''

fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")











