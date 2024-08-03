# Objective: Learn Python and coding!
## Motiation and Background
I recently had an interview where among other things, I could not code in Python in the time given. Over the years, my coding journey began with C++. Then Perl was the big thing for Biology, and later in 2016 I began my R journey with a little Python. Now, I believe for the next part of my Data Science journey, Python is mainstage.

Here, I will be coding some basic algorithms, in addition to following a fun book "Impractical Python Projects" by Lee Vaughan.

Out of the box, I love the quote - "You can always count on the Americans to do the right thing after they have tried everything else" - Weakly linked to Winston Churchill. So now after presenting myself as a data scientist for years, I will practice algorithms and code in Python!!

I have ideas to present this code, but for now it lies in the src folder.

## Python basics
### Python header - 
>#!/usr/bin/env python

### Resources for Python Conventions:
[_Zen of Python or any other explanatory document_](https://peps.python.org/pep-0020/)
[_PEP8 Standard_](https://peps.python.org/pep-0008/)
[_PEP 257 Style Guide_](https://peps.python.org/pep-0257/)
[_Pylint to grade your code_](https://pylint.readthedocs.io/en/stable/)
[_Pseudocode standards_](https://users.csc.calpoly.edu/~jdalbey/SWE/pdl_std.html)
[_Python Data Structures_](https://www.stationx.net/python-data-structures-cheat-sheet/)

>pylint mycode.py

R - Refactor - good practice metric violation!
C - Convention Violation
W - Warning for stylistic Problem
E - Error, likely a bug
F - Fatal error, will prevent processing!

### The __main__ and __init__ things!

>
>class MyGreetings:
>    def __init__(self, name):
>        self.name = name
>    
>    def greet(self):
>        print(f"Hello, {self.name}!")
>
>if __name__ == "__main__":
>    # Create an instance of MyGreetings
>    my_instance = MyGreetings("Jas")
>    # Call the greet method
>    my_instance.greet()
>

- Class uses CamelCase like MyClass here.
- Methods are written in snake_case like my_function

- \__init__ is a constructor that is called to initialize the Class, here "MyClass" which can have many methods
- \__name__ == "\__main__" identifies the main function to be run if the script is called directly, e.g., from the command line.
- if the function is imported into another script nothing is done.


## Presorting problems
- Sorting + binary search
- Sorting + one pass
- Sorting + two-pointer pass

## Complexity
- Need to do better than BruteForce
- Linear scan to search in non-sorted array - Cant be faster than linear O(n) - without missing a number/item!
- O(n) - good for arrays, sliding window, 2-pointer, prefix-sum
- O(log n) - typical binary search
- quadratic time - look if you can do better
- many 2D problems take quadratic time, also some dynamic sorting problem with 2D arrays
[_Interesting JAVA code bug_](https://thebittheories.com/the-curious-case-of-binary-search-the-famous-bug-that-remained-undetected-for-20-years-973e89fc212)

## Interesting exercises 
- Bar Chart for alphabet usage in dictionary words





