---
layout: page
title: Notes
permalink: /notes/
---
# Unit 3 Notes
(I've basically copy pasted these from the lessons for ease of access)
# Unit 3.1 and 3.2
## Variables and Assignments Notes

I did my best. Ya'll were speedrunning I am NOT a speedrunner.

## Python:
Variables - Name/define; other functions can be done after naming
= - Will set something equal to something else, usually a word and number or list, etc
Functions can be performed when names are applied (it tells the function to apply to things with the same name)
Floats - Decimals that can be used to do math/whatever a function asks for
Dictionaries assign keys and values

## Javascript:
'var xyz' is a variable assignment (ie; variables can be assigned using var)
Booleen is true/false
Strings are words, such as 'let' 
Lists - const (name) =

# Data Abstraction:
- For APs, indexes start at 1 rather than 0

## Python:
- Lists look like: name = ["word", "word"]
- Lists are often used to store data
- Lists can also be used to make more lists by using the format: list = ["Strawberry - Fruit", "Brocolli - Vegetable"]
And add: fruit = [] and vegetable = []
Code such as 'for fruit in list' can be used to specify what the program is supposed to do with the items under this category in the list
- Split [split()] function can be used to split a string into a list
- Join [join()] method takes all items in an iterable and joins them into one string; a string must be specified as a seperator

## Javascript:
- this.(name) can be used to specify different types of data, (name) can be used to make a category for the data to go in
- data can be displayed using var (variable name) = [ new (variable name)("Name", "Date", "Age"), etc etc.];
- A function can be used afterwards to store the data, using:
         function (function name)(name, (variable name))
         name.setRole("Name");
         this.name = name;
         this.variable name = [Name];
             Etc., etc.

-------------------------------------------------------------------------------------------------------------------------------
# Unit 3.3 and 3.4 Notes
## Vocab: fill in the blanks  
  
The symbol for exponent is ^  
The symbol for addition is +  
The symbol for subtraction is -  
The symbol for multiplication is *  
The symbol for division is /  
The symbol for modulus is %  
An algorithm is a sequence of steps that accomplishes a specific task  

Index is a number representing a position, like a character's position in a string or a string's position in a list.  
Concatenation is when two strings are combined with each other.  
Length is the amount of items in a string.
A substring is a part of a string.  

- Length - the number of characters/item in a string
- Addition, subtraction, and division are all represented by their respective symbols
- The only differences are multiplication and exponents (* and ^)
- Concatenation (which I cannot spell) is essentially adding 2 strings together
- Substrings are parts of strings
- The length of a string is the amount of items or numbers in it
- 'Str' can be used to initialize something for printing
- 'len' tells the code to consider the entirety of the string's length
-------------------------------------------------------------------------------------------------------------------------------
## Unit 3.5, 3.6, and 3.7 Notes
- Boolean - 2 options (ex: true/false, yes/no, 0/1)
- Relational Operator - Operators that can work between any two values of the same type
- Logical Operator - Operators that work on operands to produce a single boolean result (such as and or not)
- Relational operators go first, then logical

- All programs have conditionals
- Conditionals drive selection; they dictate what happens in a program based on whether something is true or false
- Usually lots of if/else statements
- Algorithm - A set of instructions that accomplish a task
- Selection - The process that determines which parts of an algoritm is being executed based on a condition that is true or false
- If/else statements change based on what has occured before
- Nested Conditionals are like conditionals within conditionals
- (Ex: If condtion 1 is met, condition 2 will occur, and if condition 2 occurs, condition 3 can occur)
-------------------------------------------------------------------------------------------------------------------------------
## Unit 3.8 and 3.10 Notes
|   Pseudocode Operation  | Python Syntax |                                                           Description                                                          |
|:-----------------------:|---------------|:------------------------------------------------------------------------------------------------------------------------------:|
|       aList[i]       |       aList[i]        | _Accesses the element of aList at index i_                                                                                     |
|       x ← aList[i]      |        x = aList(i)       | _Assigns the element of aList at index i <br>to a variable 'x'_                                                                |
|       aList[i] ← x	     |      aList(i) = x         | _Assigns the value of a variable 'x' to <br>the element of a List at index i_                                                  |
|   aList[i] ← aList[j]   |       aList[i] = aList[j]        | _Assigns value of aList[j] to aList[i]_                                                                                        |
| INSERT(aList, i, value) |       aList.insert(i, value)        | _value is placed at index i in aList. Any <br>element at an index greater than i will shift<br>one position to the right. _    |
|   APPEND(aList, value)  |      aList.append(value)         |       value is added as an element to the end of aList <br> and length of aList is increased by 1         |
|     REMOVE(aList, i)	    |      aList.pop(i)<br>OR<br>aList.remove(value)         | _Removes item at index i and any values at <br>indices greater than i shift to the left. <br>Length of aList decreased by 1. _ |

- For Loops - Loops that apply a certain algorithm or function to an entire list of similar things; iterates until told not to/until conditions are met (infinite)
- Recursive Loops - Loops that run through the code until reaching a specific break point
- While Loops - run until the end of the list (sometimes not in some cases)

-------------------------------------------------------------------------------------------------------------------------------
## Unit 3.9 and 3.11 Notes

Binary search:
- One of the two searches that can be used
- Can only be used with sorted arrays
- Can be used in a while loop or recursive function
- Uses a min/max value, halves it, and tests to see if the selected half value matches a requirement; if it doesn't, it takes either a higher or lower value (whichever is closer) to retest

Sequential search:
- Usually slower than a Binary Search, as it goes through every element in a list
- Can be used in a while loop or recursive function
- Should not be used for long calculations unless you want to explode your computer
-------------------------------------------------------------------------------------------------------------------------------
## Unit 3.12 and 3.13 Notes

Procedure: A named group of programming instructions that may have parameters and return values; can also be referred as method or function, depending on the language. 

Parameters: Input values of a procedure

Arguments: Specify the values of the parameters when a procedure is called

Modularity: Separating a program's functions into independent blocks that work together to allow a program to function

Procedural Abstraction: The name for a process that allows a procedure to be used while only knowing what it does, and not how the program executes the procedure

What are some other names for procedures?: Processes, operations, modules

Why are procedures effective?: Procedures are effective because they allow for code to be more organized while still retaining functionality

## Additional Notes:

- Procedures interrupt a series of statements and makes the program execute the procedure instead
- The original code will be run after the procedure is executed
- Procedures may or may not return values (such as numbers or booleans)
- Procedures need names to be called (Ex: 'convertDecimalToBinary' for a decimal to binary converter)
- Procedures allow for additional cells outside of code to be changed without having to change the code itself
-------------------------------------------------------------------------------------------------------------------------------
## Unit 3.14 and 3.15 Notes

Packages allow a python user to import methods from a library, and use the methods in their code. Most libraries come with documentation on the different methods they entail and how to use them, and they can be found with a quick Google search. Methods are used with the following: 

Some libraries are always installed, such as those with the list methods which we have previously discussed. But others require a special python keyword called import. We will learn different ways to import in Challenge 1.

Sometimes we only need to import a single method from the package. We can do that with the word 'from', followed by the package name, then the word 'import', then the method. This will alllow you to use the method without mentioning the package's name, unlike what we did before, however other methods from that package cannot be used. To get the best of both worlds you can use '*'.

To import a method as an easier name, just do what we did first, add the word 'as', and write the name you would like to use that package as.

- Random values - Randomly generated numbers created using a large set of numbers and a mathematical algorithm
- Random values are good for randomizing outputs, which can make sure that there are not as many similar outputs
- Random values can also be used for anything including probability, which includes gacha, dice rolls, and more
- Really not sure what other notes I can add here
- Remember to import random before trying to use a randomizer
-------------------------------------------------------------------------------------------------------------------------------
## Unit 3.16 Notes

- Simulations are used to simplify/modify certain variables
- Simulations can contain bias
- They can be used to simulate things as tests (ie, launching a bomb) when these actions are too dangerous/impractical to do in the real world 
- Simulations can also be used to create situations that are too difficult to recreate in the real world (specific weather conditions for example)
- Random modules define series of objects that can be generated randomly
- Randomization helps simulations, as they can help predict many varying probablilities of a simulation
- Abstractions use conditionals to execute one part of the code only when a particular condition is met, repeat looping, simplification, and it does not request input from the user or display output to the user
- It is far cheaper to create a simulation than to do said actions in real life
