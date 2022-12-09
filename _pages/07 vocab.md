---
layout: page
permalink: /vocabulary/
title: Vocab
---
# Compsci Vocab

## Unit 2 Binary/Data Terms
- Bits - the smallest unit of data that a computer can process and store
- Bytes - A unit of data that is eight binary digits long
- Hexadecimal/Nibbles - A base-16 numbering system that uses the digits 0 through 9 and the letters A through F to represent data, including nibbles and bytes

## Binary Numbers:
- Unsigned Integer - Integers that have the property that they don't have a + or - sign associated with them
- Signed Integer - Integers that can be positive or negative
- Floating Point - A variable type that is used to store floating-point number values
  - (Ex:)

## Binary Data Abstractions: 
- Boolean - A logical data type that can have only the values true or false
  - (Ex:)
- ASCII - A standard data-encoding format for electronic communication between computers
- Unicode - The universal character representation standard for text in computer processing
- RGB - A system for representing the colors to be used on a computer display

## Data Compression:
- Lossy - A data encoding and compression technique that deliberately discards some data in the compression process
- Lossless - A type of compression that restores and rebuilds file data in its original form after the file is decompressed

## Unit 3 Algorithm/Programming Terms
- Variables - an abstract storage location paired with an associated symbolic name
- Data Types - Strings, Characters,Integers, Floats, or Booleans
- Assignment Operators - An assignment statement that sets aor re-sets the value sto- - red in the storage location(s) denoted by a variable name

## Managing Complexity with Variables:
- Lists - An abstract data type that represents a finite number of ordered values, where the same value may occur more than once
- 2D Lists - A list used to store objects
  - (Ex: List = ["Item 1", "Item 2", "Item 3",])
- Dictionaries - An abstract data type that defines an unordered collection of data as a set of key-value pairs
  - (Ex: variable1: A, variable2: B, variable3: C)
- Class - A template definition of the method s and variable s in a particular kind of object
- Algorithms - A specific procedure for solving a well-defined computational problem
  - (Ex: def convertDecToBinary being stated then recalled later in the code using only 'convertDecToBinary')
- Sequence - When your computer will run your code in order, one line at a time from the top to the bottom of your program
- Selection - A programming construct where a section of code is run only if a condition is met
- Iteration - A process where a set of instructions or structures are repeated in a sequence a specified number of times or until a condition is met
  - (Ex: if x > y: print x, else: (etc., etc.))
- Expressions - A computer program statement that evaluates to some value
  - (Ex: * = Multiply, + = Add)
- Comparison Operators - Operators that compare values and return true or false
  - (Ex: if x > y: print true, else: false)
- Booleans Expressions and Selection - When one of two options are selected: True or False, Yes or No, etc.
  - (Ex: if x > y: print true, else: end loop)
- Booleans Expressions and Iteration - When one of two options are selected: True or False, Yes or No, etc. in a repeating loop
  - (Ex: if x > y: print true, else: false)
- Truth Tables - A table that shows all possible combinations of inputs and, for each combination, the output that the circuit will produce
  - (Ex: alist.append appends, alist.remove removes, etc.)
- Characters - A display unit of information equivalent to one alphabetic letter or symbol
  - (Ex: A, B, C, = 1, 2, 3 (but binary is probably better))
- Strings - An array data structure of bytes (or words) that stores a sequence of elements, typically characters, using some character encoding
  - (Ex: String = ['Item 1', 'Item 2', 'Item 3'])
- Length - The length of characters a computer's processor can handle
  - (Ex: 8-bit, 16-bit, etc.)
- Concatenation - The operation of joining two strings together
  - (Ex: string3 = string1 + string2)
- Upper - A value that is greater than or equal to every element of a set of data
- Lower - A value that is lesser than or equal to every element of a set of data
- Traversing Strings - Accessing all the elements of the string one after the other by using the subscript
  - (Ex: )

## Python:
- If, Elif, Else conditionals - Conditional statements that provide you with the decision making that is required when you want to execute code based on a particular condition
  - (Ex: if x > y: print x, else: (etc., etc.))
- Nested Selection Statements - Structures are used when more than one decision must be made before carrying out a task
  - (Ex: if x > y:, if x > 10, print x, else: print y, else: (etc., etc.))
- For, While loops with Range, with List - Loops used to repeat a section of code an unknown number of times until a specific condition is met
- Combining loops with conditionals to Break - Loops that stop when a specific condition is met, when they would normally continue forever otherwise
- Continue - A statement that forces the next iteration of the loop to take place, skipping any code in between
- Procedural Abstraction - Sections of code that have variable parameters
- Python Def procedures - Procedures that allow us to group a block of code under a name, known as a procedure name
- Parameters - A special kind of variable used in a function to refer to one of the pieces of data provided as input to the function
- Return Values - A value that a function returns to the calling script or function when it completes its task