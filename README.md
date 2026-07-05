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

Question I Still Have

If Python is dynamically typed and determines data types at runtime, how does it manage memory efficiently while maintaining good performance compared to statically typed languages like Java?

# Day 2 - Python Collections (Part 1)

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

# Question I Still Have

How does Python internally implement shallow copy and deep copy, and why are nested mutable objects shared in a shallow copy?

