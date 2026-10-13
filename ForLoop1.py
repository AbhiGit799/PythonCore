'''

for(i=0; i<arr.len; i++) will not work in Python.

This is one of the biggest differences to remember:

| Java                               | Python                     |
| ---------------------------------- | -------------------------- |
| `for (int i=0; i<arr.length; i++)` | `for i in range(len(arr))` |
| `arr.length`                       | `len(arr)`                 |
| `{ }`                              | indentation                |
| `arr[i]`                           | `arr[i]`                   |
| `for (int x : arr)`                | `for x in arr`             |


In Java, you might write:

for (int i = 0; i < arr.length; i++) {
    System.out.println(arr[i]);
}

In Python, the equivalent is:

for i in range(len(arr)):
    print(arr[i])

Python's for loop is designed to iterate over a sequence/range directly.

If you don't need the index, you don't need range() at all:


    
'''

for i in range(5):
    print(i)

print("\n")

arr = [10, 20, 30, 40]

for i in range(len(arr)):
    print(arr[i])

print("\n")

for value in arr:
    print(value)





















