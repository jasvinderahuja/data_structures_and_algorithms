# Objective: Learn Python and coding!
## Motiation and Background
I recently had an interview where among other things, I could not code in Python in the time given. Over the years, my coding journey began with C++. Then Perl was the big thing for Biology, and later in 2016 I began my R journey with a little Python. Now, I believe for the next part of my Data Science journey, Python is mainstage.

Here, I will be coding some basic algorithms, and go onto leetcode questions for practicing Python.

I love the quote from - "Impractical Python Projects" by Lee Vaughan. - "You can always count on the Americans to do the right thing after they have tried everything else" - Weakly linked to Winston Churchill. 

So now after using data science methods for years, I will practice algorithms and learn to code fluently in Python!!

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

## [For Sorting methods](SortingAlgorithms.md)
