def backtrack(start, current):

    if len(current) == 2:
        result.append(current.copy())
        return

    for i in range(start, len(choices)):

        # 1. Choose
        current.append(choices[i])

        # 2. Explore
        backtrack(i + 1, current)

        # 3. Undo the choice
        current.pop()


choices = ["A", "B", "C"]

result = []

backtrack(0, [])

print(result)




'''

You define choice outside the function so how you are accessing inside the function?


In Python, a function can access variables defined outside that function, provided they are in the appropriate scope.

Let's understand this step by step.

1. Global variable vs Local variable
Consider this simple example:

name = "Rahul"  # Global variable

def greet():
    print(name)

greet()


Why does this work?
- name is defined outside the function.
- When Python executes print(name), it looks for name inside the function.
- It doesn't find it there.
- So Python looks in the enclosing/global scope.
- It finds name = "Rahul".
Therefore, we can access it.



Here we have three variables:
 
Variable	        Defined where?	           Accessed where?
choices	          Outside function	           Inside function
result	          Outside function	           Inside function
current	          Function parameter	       Inside function

choices and result are global variables in this example.

current is a local variable (a parameter).

3. But why can't we define choices after calling the function?
Consider:

def backtrack():
    print(choices)

backtrack()

choices = ["A", "B", "C"]

Gives Error = NameError: name 'choices' is not defined


But this works:

def backtrack():
    print(choices)

choices = ["A", "B", "C"]

backtrack()

Output => ['A', 'B', 'C']

4. One more important concept
Python allows us to read global variables inside functions without using global.


count = 10

def display():
    print(count)

display()

But if we want to reassign a global variable inside a function, we need global:

count = 10

def update():
    global count
    count = 20

update()

print(count)  # 20

For mutable objects such as lists, we can modify their contents without global:

choices = ["A", "B", "C"]

def update():
    choices.append("D")

update()

print(choices)

Output ['A', 'B', 'C', 'D']


Remember this rule:
- Reading a global variable inside a function → No global required.
- Modifying a global list's contents → No global required.
- Reassigning a global variable → Use global if you intend to modify the global binding.
This concept is called Python Variable Scope, and it is very useful when working with recursion and Backtracking.

'''






















