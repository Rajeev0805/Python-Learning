# Day 1

## Concepts Learned
- print()
- Variables
- Data Types
- Input
- Type Conversion
- Operators

## Files
- hello.py
- datatype.py
- input.py
- operators.py
- student.py

## What I Found Interesting
Today, I started my Python learning journey. Coming from a Java background, the first thing I noticed was how concise and readable Python's syntax is. Unlike Java, Python doesn't require braces {}, semicolons ;, or even a main() method to execute a program. Instead, it relies on indentation to define code blocks, making the language simpler to read and write.

One concept that immediately reminded me of Java was taking user input. In Java, we use the Scanner class, which requires importing the package and creating an object before reading input. In Python, the built-in input() function handles this directly, making the process much simpler.

For example:

Java

Scanner sc = new Scanner(System.in);
int age = sc.nextInt();

Python

age = int(input("Enter your age: "))

I also learned that the input() function always returns data as a string. To work with numbers, Python provides built-in type conversion functions such as int() and float(). Understanding this helped me realize that Python prioritizes simplicity while still giving developers control over data types when needed.

Comparison with Java
Java is statically typed, so every variable must be declared with its data type.
Python is dynamically typed, meaning the interpreter automatically determines the variable's type at runtime.
Java requires more boilerplate code, whereas Python allows developers to focus more on problem-solving than syntax.
What I Found Interesting

Although Python's syntax is much shorter than Java's, I noticed that the underlying programming concepts remain the same. My Java knowledge isn't wasted; instead, it gives me a strong foundation for understanding Python more quickly. I'm not learning programming from scratch—I'm learning a new language and a new ecosystem.

# Day 2 - Python Collections 

## Date
22 June 2026

---

# Topics Covered

- Strings
- String Indexing
- Negative Indexing
- String Slicing
- String Methods
  - upper()
  - lower()
  - replace()
  - split()
  - len()
- Lists
- List Mutability
- List Operations
  - append()
  - insert()
  - remove()
  - sort()
  - reverse sorting
- Object References
- Shallow Copy
- Tuple Introduction
- Tuple Packing & Unpacking
- Variable Swapping
- Using `_` to Ignore Unused Values

---

# What I Learned

Today I learned how Python stores and manipulates collections of data.

Strings are immutable sequences of characters, whereas lists are mutable collections that allow elements to be added, removed, or modified. I also learned that variables in Python store references to objects rather than the objects themselves, which explains why modifying a list through one reference affects every variable pointing to the same list.

I understood the difference between assigning a list to another variable and creating a shallow copy using `copy()`. I also learned that tuple unpacking makes Python code concise and that the underscore (`_`) is commonly used to intentionally ignore values that are not needed.

---

# Why It Works

Python uses object references to avoid unnecessary copying of data, making memory usage more efficient.

Lists are mutable because they are designed to represent collections whose contents change over time.

Strings and tuples are immutable, making them safer to share between different parts of a program and allowing Python to optimize their usage.

Tuple unpacking allows multiple variables to receive values from a tuple in a single statement.

---

# Comparison with Java

| Java | Python |
|------|--------|
| `String` is immutable | `str` is immutable |
| `Scanner` is required for input | Built-in `input()` |
| Arrays have fixed size | Lists grow dynamically |
| `ArrayList` is mutable | Lists are mutable |
| Swapping usually needs a temporary variable | Supports tuple unpacking (`a, b = b, a`) |

---

# Mistakes I Made

- Initially thought `(5)` was a tuple. Learned that a single-element tuple requires a comma: `(5,)`.
- Thought the `+` operator would perform numerical addition on lists. Learned that it concatenates two lists.
- Mixed up Java `String` mutability before understanding that Java `String` objects are also immutable.

---

# Interesting Observations

- In Python, the comma creates a tuple, not the parentheses.
- Multiple variables can refer to the same list object.
- `copy()` creates a shallow copy, not a completely independent deep copy.
- Python code is significantly more concise than Java for many common tasks.

---

# Interview Questions

### 1. Why are strings immutable in Python?

To prevent unintended side effects when multiple variables reference the same string object and to allow internal optimizations.

### 2. Difference between List and Tuple?

Lists are mutable, whereas tuples are immutable and can be used as dictionary keys because their values cannot change.

### 3. What is tuple unpacking?

Assigning multiple variables from a tuple in a single statement.

Example:

```python
name, age, cgpa = ("Rajeev", 22, 9.55)
```

---

# Today's Challenge

Solved problems involving:

- String slicing
- List operations
- Object references
- Shallow copy
- Tuple unpacking
- Predicting program output without executing the code

---

# Day 3 - Python Collections 

---

# Topics Covered

- Revision of Strings, Lists and Tuples
- Tuple Packing
- Tuple Unpacking
- Ignoring Values using `_`
- Swapping Variables
- Sets
- Set Operations
  - add()
  - remove()
  - discard()
  - Union
  - Intersection
  - Difference
- Dictionaries
- Dictionary Operations
  - get()
  - keys()
  - values()
  - items()
  - pop()
  - Updating Values
  - Adding New Key-Value Pairs

---

# What I Learned

Today I completed Python's collection data structures by learning Sets and Dictionaries.

I understood that a Set is designed to store unique values and performs fast searching using hashing. Unlike Lists, Sets do not preserve order and do not support indexing. I also learned common set operations such as Union, Intersection and Difference, which are useful in solving real-world problems involving unique data.

I learned that Dictionaries store information as key-value pairs, making them much more suitable than parallel lists for representing related data. Dictionary lookups are efficient because Python uses hashing internally. I also learned how to add, update, delete and retrieve values safely using dictionary methods.

---

# Why It Works

Python provides multiple collection types because each solves a different problem efficiently.

- Lists represent ordered collections.
- Tuples represent fixed collections.
- Sets represent unique collections with fast searching.
- Dictionaries represent mappings between keys and values.

Instead of creating one complex data structure that does everything, Python provides specialized collections optimized for different use cases.

---

# Comparison with Java

| Java | Python |
|------|--------|
| HashSet | Set |
| HashMap | Dictionary |
| ArrayList | List |
| Immutable String | Immutable String |
| Temporary variable needed for swapping | Tuple unpacking (`a, b = b, a`) |
---

# Interesting Observations

- A Set automatically removes duplicate values.
- Membership checking in Sets is faster than Lists because of hashing.
- Dictionaries check only Keys when using the `in` operator.
- Dictionary Keys must be immutable.
- Lists, Tuples, Sets and Dictionaries all solve different real-world problems.

---

# Interview Questions

### Why are Sets faster than Lists for searching?

Sets use hashing, allowing Python to locate elements efficiently without checking each element one by one.

---

### Why can't Lists be Dictionary Keys?

Lists are mutable. If a key changes after insertion, Python would no longer be able to locate it correctly. Dictionary keys must remain immutable.

---

### Difference between `remove()` and `discard()` in Sets?

- `remove()` raises a `KeyError` if the element is absent.
- `discard()` silently does nothing if the element does not exist.

---

### Difference between Lists and Dictionaries?

Lists store ordered elements accessed using numeric indexes.

Dictionaries store key-value mappings accessed using keys.

---

# Mini Challenges Completed

✔ Tuple unpacking

✔ Variable swapping

✔ Set operations

✔ Dictionary creation

✔ Dictionary update

✔ Dictionary deletion

✔ Dictionary traversal methods

✔ Predicted outputs without executing code

---

# Today's Challenge

Solved reasoning questions involving:

- Hashing
- Dictionary design
- Object references
- Collection selection
- Memory behavior

---


---
# Day 4 - Loops
---

# Topics Covered

- for Loop
- while Loop
- range()
- Iterating through Strings
- Iterating through Lists
- Iterating through Dictionaries
- Tuple Unpacking inside Loops
- break
- continue
- pass
- Loop else
- Nested Loops (Introduction)

---

# What I Learned

Today I learned how loops eliminate repetitive code by automating repeated execution.

I understood that Python's `for` loop is used when iterating over a sequence or when the number of iterations is known. The `while` loop is used when execution depends on a condition and the number of iterations is unknown.

I also learned how `break`, `continue`, and `pass` behave differently and where each should be used.

Finally, I learned that dictionaries can be traversed using `items()`, where Python automatically performs tuple unpacking.

---

# Why It Works

Loops allow the CPU to execute the same block of code multiple times without duplicating code.

Python's `range()` object generates values lazily instead of storing millions of integers in memory, making loops memory efficient.

The language follows a consistent "end exclusive" rule across slicing and `range()`, reducing off-by-one errors.

---

# Comparison with Java

| Java | Python |
|------|--------|
| `for(int i=0;i<n;i++)` | `for i in range(n)` |
| Enhanced for-loop | Direct iteration (`for item in list`) |
| while loop | while loop |
| break | break |
| continue | continue |
| No equivalent of loop-else | loop-else |

---
# Interesting Observations

- `range()` is memory efficient because it generates values lazily.
- Loop variables remain accessible after a loop finishes.
- Python automatically performs tuple unpacking when iterating over `dictionary.items()`.
- Every collection learned so far becomes significantly more useful when combined with loops.

---

# Interview Questions

### Difference between `break`, `continue` and `pass`

- `break` exits the loop completely.
- `continue` skips only the current iteration.
- `pass` performs no operation and acts as a placeholder.

---

### Why is `range()` end-exclusive?

To maintain consistency with Python's indexing and slicing model while avoiding common off-by-one errors.

---

### When should we use `for` and `while`?

Use `for` when the number of iterations or iterable is known.

Use `while` when repetition depends on a condition that is evaluated during execution.

---

# Mini Challenges Completed

✔ for Loop

✔ while Loop

✔ range()

✔ Dictionary Iteration

✔ break

✔ continue

✔ pass

✔ Output Prediction

---
# Day 5 - Functions


# Topics Covered

- Function Definition
- Function Calling
- Parameters
- Arguments
- Local Variables
- Function Execution Flow
- return Statement
- Difference between print() and return
- Returning Multiple Values
- Default Parameters
- Keyword Arguments
- Variable Length Arguments (*args)

---

# What I Learned

Today I learned that functions are reusable blocks of code designed to perform a specific task.

I understood that parameters act as placeholders while arguments are the actual values supplied during a function call.

The most important concept I learned today was the difference between `print()` and `return()`. Printing only displays information to the user, whereas `return` sends the computed value back to the caller, allowing other parts of the program to reuse it.

I also learned that Python supports default parameter values, keyword arguments, and variable-length arguments (`*args`), making functions flexible and reusable.

---

# Key Concepts

## Parameters vs Arguments

- Parameters are variables defined in the function.
- Arguments are actual values passed during the function call.

---

## print() vs return()

- `print()` displays output.
- `return` gives the computed value back to the caller.

---

## Default Parameters

Default values are used when the caller doesn't provide an argument.

---

## Keyword Arguments

Arguments can be matched by parameter name instead of position.

---

## *args

`*args` collects multiple positional arguments into a tuple.

---

# Comparison with Java

| Java | Python |
|------|--------|
| Method | Function |
| Method Parameters | Parameters |
| Method Arguments | Arguments |
| return | return |
| Varargs (`int...`) | *args |

---

# Interview Questions Covered

- Parameter vs Argument
- print() vs return()
- Why return is important
- Default Parameters
- Keyword Arguments
- *args
- Function Execution Flow

---

# Mini Challenges Completed

✔ Function Creation

✔ Parameters

✔ Return Values

✔ Default Parameters

✔ Keyword Arguments

✔ Variable Length Arguments

✔ Nested Function Calls

---

# Project Readiness

Python Fundamentals Completed So Far:

- Variables
- Data Types
- Strings
- Lists
- Tuples
- Sets
- Dictionaries
- Loops
- Functions

The next learning session begins with the Contact Book project, where these concepts will be combined into a real application.

---