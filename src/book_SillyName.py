#!/usr/bin/env python
def RandomCombine_Fname_Lname(Fname, Lname):
    """
    Fname: array of First_Names
    Lname: array of Last_Name
    Pseudocode: 
        Load a list of first names 
        Load a list of last names
        Assign a random first_name to variable
        Assign a random last_name to variable
        Return the newly combined name
    """
    import sys
    import random
    
    FirstName=random.choice(Fname)
    LastName=random.choice(Lname)
    return f'{FirstName} {LastName}'

## Maybe from Pubmed
## From Movie cast!
