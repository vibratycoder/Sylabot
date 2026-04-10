# ISA 500: Programming Foundations for Analytics - Flashcard Reference Bank

---

## Python Programming

### Key Terms & Definitions
- **Python**: A high-level, interpreted programming language known for readable syntax and extensive library ecosystem
- **Interpreted Language**: Code is executed line-by-line at runtime rather than compiled into machine code beforehand
- **High-Level Language**: A programming language abstracted from hardware details, closer to human-readable syntax
- **IDE (Integrated Development Environment)**: Software application providing tools for writing, testing, and debugging code (e.g., VS Code, PyCharm)
- **Jupyter Notebook**: An interactive computing environment that combines code, output, and narrative text in a single document
- **pip**: Python's default package manager used to install and manage third-party libraries
- **Anaconda**: A distribution of Python bundled with data science libraries and the conda package manager
- **Library/Module**: A collection of pre-written code that extends Python's functionality (e.g., pandas, NumPy)
- **pandas**: Python library for data manipulation and analysis using DataFrames
- **NumPy**: Library for numerical computing, providing support for arrays and mathematical operations
- **matplotlib**: Foundational Python library for creating static, animated, and interactive visualizations
- **scikit-learn**: Machine learning library providing tools for classification, regression, and clustering

### Core Concepts (Q&A Format)
- Q: Why is Python considered the leading language for data analytics?
- A: Python combines readable syntax, extensive data science libraries (pandas, NumPy, scikit-learn), a large community, and versatility across the entire analytics pipeline from data collection to visualization.

- Q: What is the difference between a compiled and interpreted language?
- A: Compiled languages (C, Java) translate entire source code to machine code before execution; interpreted languages (Python) execute code line-by-line at runtime, allowing faster development but generally slower execution.

- Q: What is PEP 8?
- A: PEP 8 is Python's official style guide that provides conventions for writing readable, consistent Python code, including rules on indentation, naming, and line length.

- Q: What does it mean that Python is dynamically typed?
- A: Variable types are determined at runtime based on assigned values, not declared explicitly in advance. A variable can change type during execution.

- Q: Why are Jupyter Notebooks popular in data analytics?
- A: They allow combining executable code, visualizations, and explanatory text in one document, making them ideal for exploratory data analysis and sharing reproducible analyses.

- Q: What is the Python REPL?
- A: Read-Eval-Print Loop -- an interactive shell where Python commands are entered, executed, and results displayed immediately.

### Important Facts & Figures
- Python is used by over 80% of Fortune 500 companies for data tasks
- Python was created by Guido van Rossum and first released in 1991
- Python 3 is the current major version; Python 2 reached end-of-life in January 2020
- Python uses indentation (whitespace) to define code blocks, not curly braces
- Python is case-sensitive: `Variable` and `variable` are different names
- The Python Package Index (PyPI) hosts over 400,000 third-party packages
- Python supports multiple paradigms: procedural, object-oriented, and functional programming

### Common Exam Questions
- Q: Name three core Python libraries used in data analytics and their primary purpose.
- A: pandas (data manipulation/DataFrames), NumPy (numerical computing/arrays), matplotlib (data visualization/plotting).

- Q: What makes Python an interpreted language and how does this affect development?
- A: Python code is executed line-by-line by the interpreter at runtime. This enables rapid prototyping and interactive debugging but may run slower than compiled languages.

- Q: What is the significance of PEP 8 in Python programming?
- A: PEP 8 is the official style guide that standardizes code formatting (indentation, naming conventions, line length) to improve readability and maintainability.

- Q: Explain why Python uses indentation instead of braces for code blocks.
- A: Python enforces indentation as part of its syntax to improve readability and reduce visual clutter, making code structure immediately visible.

---

## Variables

### Key Terms & Definitions
- **Variable**: A named reference that stores a data value in memory, created by assignment
- **Assignment Operator (=)**: Binds a value to a variable name; e.g., `x = 5`
- **Dynamic Typing**: Python determines a variable's type at runtime based on the assigned value, not by explicit declaration
- **Data Type**: The classification of data (int, float, str, bool, list, dict, tuple, set)
- **int**: Integer data type for whole numbers (e.g., 42, -7)
- **float**: Floating-point data type for decimal numbers (e.g., 3.14, -0.5)
- **str**: String data type for text, enclosed in single or double quotes
- **bool**: Boolean data type with only two values: True or False
- **list**: Ordered, mutable collection enclosed in square brackets []; allows duplicates
- **dict**: Dictionary -- unordered collection of key-value pairs enclosed in curly braces {}
- **tuple**: Ordered, immutable collection enclosed in parentheses ()
- **Mutable**: A data type whose value can be changed after creation (list, dict, set)
- **Immutable**: A data type whose value cannot be changed after creation (int, float, str, tuple, bool)

### Core Concepts (Q&A Format)
- Q: What is the difference between mutable and immutable data types in Python?
- A: Mutable types (list, dict, set) can be modified in place after creation. Immutable types (int, float, str, tuple, bool) cannot be changed; any modification creates a new object.

- Q: How does dynamic typing work in Python?
- A: Python infers the variable type from the assigned value at runtime. The same variable can hold different types during execution: `x = 5` (int), then `x = "hello"` (str).

- Q: What is the difference between `==` and `is` when comparing variables?
- A: `==` compares values (equality), while `is` compares object identity (whether two variables reference the same object in memory).

- Q: How do you convert between data types in Python?
- A: Use built-in functions: `int()`, `float()`, `str()`, `bool()`, `list()`, `tuple()`. Example: `int("42")` converts the string "42" to integer 42.

- Q: What are Python's variable naming rules?
- A: Names can contain letters, digits, and underscores; cannot start with a digit; are case-sensitive; cannot be reserved keywords. Convention is snake_case for variables and functions.

- Q: What is variable scope?
- A: Scope determines where a variable is accessible. Local scope is within a function; global scope is at the module level. The `global` keyword allows modifying a global variable inside a function.

- Q: What does the `type()` function do?
- A: Returns the data type of a variable or value. Example: `type(3.14)` returns `<class 'float'>`.

### Important Facts & Figures
- Python has no explicit variable declaration -- variables are created upon first assignment
- None is a special constant representing the absence of a value (similar to null in other languages)
- Strings can be created with single quotes, double quotes, or triple quotes (for multi-line)
- Lists use square brackets [], tuples use parentheses (), dictionaries use curly braces {}
- Falsy values in Python: 0, 0.0, "", None, [], {}, (), False, set()
- Variables in Python are references (pointers) to objects in memory, not containers holding values directly
- The `id()` function returns the unique memory address of an object

### Common Exam Questions
- Q: What will `type(3.0)` return? What about `type(3)`?
- A: `type(3.0)` returns `<class 'float'>`; `type(3)` returns `<class 'int'>`.

- Q: Is a tuple mutable or immutable? Give an example of when you would use a tuple over a list.
- A: Tuples are immutable. Use a tuple for fixed collections that should not change, like coordinates (x, y) or dictionary keys, which require immutable types.

- Q: What happens when you assign `x = [1, 2, 3]` and then `y = x`, then modify `y.append(4)`? What is x?
- A: x becomes [1, 2, 3, 4] because y and x reference the same list object in memory (lists are mutable and assignment copies the reference, not the value).

- Q: Name all the falsy values in Python.
- A: 0, 0.0, "" (empty string), None, [] (empty list), {} (empty dict), () (empty tuple), set(), and False.

---

## Operators

### Key Terms & Definitions
- **Operator**: A special symbol or keyword that performs an operation on one or more operands
- **Operand**: A value or variable that an operator acts upon
- **Arithmetic Operators**: +, -, *, /, // (floor division), % (modulus), ** (exponentiation)
- **Floor Division (//)**: Divides and rounds down to the nearest integer; e.g., `7 // 2` equals 3
- **Modulus (%)**: Returns the remainder of division; e.g., `7 % 2` equals 1
- **Exponentiation (**)**: Raises a number to a power; e.g., `2 ** 3` equals 8
- **Comparison Operators**: ==, !=, <, >, <=, >= -- return Boolean True or False
- **Logical Operators**: `and`, `or`, `not` -- combine or invert Boolean expressions
- **Assignment Operators**: =, +=, -=, *=, /= -- assign and update variable values
- **Membership Operators**: `in`, `not in` -- test whether a value exists in a sequence
- **Identity Operators**: `is`, `is not` -- test whether two variables reference the same object in memory
- **Operator Precedence**: The order in which operators are evaluated in an expression

### Core Concepts (Q&A Format)
- Q: What is the difference between `/` and `//` in Python?
- A: `/` performs true division and returns a float (e.g., `7/2 = 3.5`). `//` performs floor division and returns the largest integer less than or equal to the result (e.g., `7//2 = 3`).

- Q: What is operator precedence and why does it matter?
- A: Operator precedence defines the order operators are evaluated. Without understanding it, expressions like `2 + 3 * 4` might be misinterpreted (it equals 14, not 20, because * has higher precedence than +).

- Q: How do `and`, `or`, and `not` work in Python?
- A: `and` returns True only if both operands are True; `or` returns True if at least one operand is True; `not` inverts the Boolean value. Python uses short-circuit evaluation.

- Q: What is short-circuit evaluation?
- A: Python stops evaluating a logical expression as soon as the result is determined. For `and`, if the first operand is False, the second is never evaluated. For `or`, if the first is True, the second is skipped.

- Q: What is the difference between `==` and `is`?
- A: `==` checks value equality; `is` checks identity (same object in memory). `[1,2] == [1,2]` is True, but `[1,2] is [1,2]` is False (different objects).

- Q: How does the `in` operator work?
- A: Tests membership in a sequence. `"a" in "apple"` returns True. `3 in [1, 2, 3]` returns True. Works with strings, lists, tuples, sets, and dictionary keys.

### Important Facts & Figures
- Python operator precedence (high to low): () > ** > +x/-x/~x > * / // % > + - > << >> > & > ^ | > == != < > <= >= > is/is not > in/not in > not > and > or
- The `%` operator is commonly used to check even/odd: `n % 2 == 0` means n is even
- `+=` is augmented assignment: `x += 5` is equivalent to `x = x + 5`
- Python does not have increment (++) or decrement (--) operators
- The `+` operator is overloaded: it adds numbers and concatenates strings/lists
- Comparison operators can be chained: `1 < x < 10` is valid Python
- Bitwise operators (&, |, ^, ~, <<, >>) operate on binary representations of integers

### Common Exam Questions
- Q: What is the output of `17 // 5` and `17 % 5`?
- A: `17 // 5` equals 3 (floor division). `17 % 5` equals 2 (remainder).

- Q: What is the output of `2 ** 3 ** 2`? Explain why.
- A: The output is 512. Exponentiation is right-associative, so it evaluates as `2 ** (3 ** 2)` = `2 ** 9` = 512, not `(2 ** 3) ** 2` = 64.

- Q: Evaluate: `True or False and False`. What is the result and why?
- A: True. `and` has higher precedence than `or`, so it evaluates as `True or (False and False)` = `True or False` = True.

- Q: Write an expression to check if variable `x` is between 1 and 100 inclusive.
- A: `1 <= x <= 100` or equivalently `x >= 1 and x <= 100`.

---

## Conditional Statements

### Key Terms & Definitions
- **if statement**: Executes a block of code only if a specified condition evaluates to True
- **elif**: Short for "else if"; checks an additional condition when the preceding if/elif is False
- **else**: Catches all cases not handled by preceding if/elif conditions
- **Ternary Expression**: A one-line conditional: `value_if_true if condition else value_if_false`
- **Boolean Expression**: An expression that evaluates to either True or False
- **Truthy**: Non-zero numbers, non-empty strings/collections evaluate as True in Boolean context
- **Falsy**: Values that evaluate as False: 0, 0.0, "", None, [], {}, (), set(), False
- **Nested Conditional**: An if/elif/else block inside another if/elif/else block
- **match-case (Python 3.10+)**: Structural pattern matching similar to switch-case in other languages
- **Short-circuit Evaluation**: Logical operators stop evaluating as soon as the result is determined
- **Guard Clause**: An early return/exit condition that simplifies nested conditional logic

### Core Concepts (Q&A Format)
- Q: What is the difference between `if/elif/else` and multiple separate `if` statements?
- A: `if/elif/else` is mutually exclusive -- only one block executes. Multiple separate `if` statements are independent -- each is evaluated regardless of the others.

- Q: How does a ternary expression work in Python?
- A: Syntax: `result = value_if_true if condition else value_if_false`. Example: `status = "pass" if score >= 60 else "fail"`.

- Q: What values are considered falsy in Python?
- A: 0, 0.0, "" (empty string), None, [] (empty list), {} (empty dict), () (empty tuple), set(), and False. Everything else is truthy.

- Q: When should you use nested conditionals vs. elif chains?
- A: Use elif for checking multiple conditions on the same variable or related tests. Use nesting when the inner condition only applies if the outer condition is True. Prefer elif chains for readability.

- Q: What is the match-case statement introduced in Python 3.10?
- A: A structural pattern matching feature that matches a value against multiple patterns, similar to switch-case. Syntax: `match variable:` followed by `case pattern:` blocks.

- Q: How does Python evaluate compound conditions like `if x > 0 and y > 0`?
- A: Left to right with short-circuit evaluation. If `x > 0` is False, Python skips evaluating `y > 0` since `and` requires both to be True.

### Important Facts & Figures
- Python uses indentation (typically 4 spaces) to define conditional blocks, not curly braces
- An if block can exist without elif or else
- There is no limit to the number of elif clauses
- The `pass` keyword creates an empty block when syntax requires a statement but no action is needed
- Ternary expressions can be nested but this reduces readability
- match-case was introduced in Python 3.10 (PEP 634)
- Conditional expressions are evaluated lazily with short-circuit logic

### Common Exam Questions
- Q: Write a conditional that assigns letter grade based on score: A (90+), B (80-89), C (70-79), D (60-69), F (below 60).
- A: `if score >= 90: grade = "A"` / `elif score >= 80: grade = "B"` / `elif score >= 70: grade = "C"` / `elif score >= 60: grade = "D"` / `else: grade = "F"`

- Q: What is the output of `print("Yes") if 0 else print("No")`?
- A: "No" -- because 0 is a falsy value, the condition evaluates to False.

- Q: Rewrite `if x > 0: result = "positive" else: result = "non-positive"` as a ternary expression.
- A: `result = "positive" if x > 0 else "non-positive"`

- Q: What happens if no condition is True in an if/elif chain with no else clause?
- A: Nothing executes. The program continues to the next statement after the conditional block.

---

## Loops

### Key Terms & Definitions
- **for loop**: Iterates over a sequence (list, string, range, dictionary) executing a block for each element
- **while loop**: Repeats a block of code as long as a condition remains True
- **range()**: Built-in function that generates a sequence of numbers; `range(start, stop, step)`
- **break**: Immediately exits the innermost loop
- **continue**: Skips the rest of the current iteration and moves to the next iteration
- **pass**: A placeholder statement that does nothing; used when syntax requires a statement
- **Infinite Loop**: A loop that never terminates because its condition never becomes False
- **List Comprehension**: Concise syntax to create lists: `[expression for item in iterable if condition]`
- **enumerate()**: Returns both the index and value when iterating: `for i, val in enumerate(list)`
- **zip()**: Iterates over multiple sequences in parallel: `for a, b in zip(list1, list2)`
- **Iterator**: An object that implements `__iter__()` and `__next__()` methods for sequential access
- **Generator**: A function using `yield` that produces values lazily, one at a time, saving memory

### Core Concepts (Q&A Format)
- Q: What is the difference between a for loop and a while loop?
- A: A for loop iterates over a known sequence (definite iteration). A while loop repeats as long as a condition is True (indefinite iteration), useful when the number of iterations is unknown.

- Q: How does `range(start, stop, step)` work?
- A: Generates integers from `start` (inclusive) to `stop` (exclusive) with `step` increment. `range(0, 10, 2)` produces 0, 2, 4, 6, 8. Default start=0, step=1.

- Q: What is a list comprehension and why is it preferred?
- A: A concise one-line syntax for creating lists: `[x**2 for x in range(5)]` produces [0, 1, 4, 9, 16]. It is more Pythonic, often faster, and more readable than equivalent for loops.

- Q: What is the difference between `break` and `continue`?
- A: `break` exits the entire loop immediately. `continue` skips the remaining code in the current iteration and proceeds to the next iteration.

- Q: How do you avoid an infinite while loop?
- A: Ensure the loop condition will eventually become False by modifying the control variable within the loop body. Always include a clear termination condition.

- Q: What does `enumerate()` do and when is it useful?
- A: Returns (index, value) pairs when iterating. Useful when you need both the position and the element: `for i, name in enumerate(names)`.

- Q: What is a generator and how does it differ from a list comprehension?
- A: A generator uses `yield` or parentheses syntax `(x for x in range(n))` and produces values one at a time (lazy evaluation), using much less memory than a list comprehension which creates the entire list in memory.

### Important Facts & Figures
- `range()` stop value is exclusive: `range(5)` produces 0, 1, 2, 3, 4 (not 5)
- Nested loops multiply iterations: a loop of 100 inside a loop of 100 = 10,000 iterations
- List comprehensions can include conditions: `[x for x in range(20) if x % 2 == 0]`
- `break` and `continue` cannot be used directly in list comprehensions
- The `else` clause on a loop executes only if the loop completes without hitting `break`
- Iterating over a dictionary by default iterates over its keys
- `zip()` stops at the shortest input sequence

### Common Exam Questions
- Q: What is the output of `[x**2 for x in range(5)]`?
- A: [0, 1, 4, 9, 16]

- Q: Write a while loop that prints numbers 1 through 5.
- A: `i = 1` / `while i <= 5:` / `    print(i)` / `    i += 1`

- Q: What does the `else` clause on a for loop do?
- A: The else block executes after the loop finishes normally (without a `break` statement). If `break` is triggered, the else block is skipped.

- Q: What is the output of: `for i in range(10): if i == 3: continue; if i == 7: break; print(i)`?
- A: Prints 0, 1, 2, 4, 5, 6. The number 3 is skipped by `continue`, and the loop exits at 7 due to `break`.

- Q: Convert this loop to a list comprehension: `result = []; for x in range(10): if x % 3 == 0: result.append(x * 2)`
- A: `result = [x * 2 for x in range(10) if x % 3 == 0]` -- produces [0, 6, 12, 18].

---

## Functions

### Key Terms & Definitions
- **Function**: A reusable block of code defined with `def` that performs a specific task and optionally returns a value
- **def**: Keyword used to define a function in Python
- **Parameter**: A variable listed in the function definition that receives a value when called
- **Argument**: The actual value passed to a function when it is called
- **return**: Statement that exits the function and sends a value back to the caller
- **Default Parameter**: A parameter with a pre-assigned value used when no argument is provided
- ***args**: Allows a function to accept any number of positional arguments as a tuple
- ****kwargs**: Allows a function to accept any number of keyword arguments as a dictionary
- **Lambda Function**: An anonymous, single-expression function: `lambda x: x * 2`
- **Docstring**: A triple-quoted string as the first statement in a function documenting its purpose
- **Scope**: The region of code where a variable is accessible (local, enclosing, global, built-in)
- **LEGB Rule**: Python's variable resolution order: Local, Enclosing, Global, Built-in
- **Recursion**: A function that calls itself to solve a problem by breaking it into smaller subproblems

### Core Concepts (Q&A Format)
- Q: What is the difference between a parameter and an argument?
- A: A parameter is the variable name in the function definition. An argument is the actual value passed when calling the function. In `def add(a, b)`, a and b are parameters; in `add(3, 5)`, 3 and 5 are arguments.

- Q: How do *args and **kwargs work?
- A: `*args` collects extra positional arguments into a tuple. `**kwargs` collects extra keyword arguments into a dictionary. They allow functions to accept a variable number of arguments.

- Q: What is the LEGB rule?
- A: Python resolves variable names by searching scopes in order: Local (inside current function), Enclosing (outer function in nested functions), Global (module level), Built-in (Python built-ins like len, print).

- Q: What is a lambda function and when should you use it?
- A: An anonymous single-expression function defined with `lambda`. Used for short, throwaway functions, especially with `map()`, `filter()`, and `sorted()`. Example: `sorted(names, key=lambda x: x.lower())`.

- Q: What happens if a function has no return statement?
- A: The function returns `None` by default.

- Q: What is the difference between a local and global variable?
- A: A local variable is defined inside a function and accessible only within that function. A global variable is defined at the module level and accessible throughout the module. Use the `global` keyword to modify a global variable inside a function.

- Q: What is recursion and what are its requirements?
- A: Recursion is when a function calls itself. It requires a base case (stopping condition) and a recursive case that moves toward the base case. Example: factorial: `def fact(n): return 1 if n <= 1 else n * fact(n-1)`.

### Important Facts & Figures
- Functions are first-class objects in Python -- they can be assigned to variables, passed as arguments, and returned from other functions
- Default parameter values are evaluated once at function definition time, not at each call (mutable default gotcha)
- The order of parameters must be: positional, *args, keyword-only, **kwargs
- `map(function, iterable)` applies a function to every item in an iterable
- `filter(function, iterable)` returns items for which the function returns True
- Python has a default recursion limit of 1000 (can be changed with `sys.setrecursionlimit()`)
- Docstrings are accessed with `function_name.__doc__` or `help(function_name)`
- Type hints (Python 3.5+) annotate parameters and return types: `def add(a: int, b: int) -> int:`

### Common Exam Questions
- Q: What is the output of: `def greet(name="World"): return f"Hello, {name}!"` followed by `greet()`?
- A: `"Hello, World!"` -- the default parameter value is used when no argument is provided.

- Q: Write a lambda function that takes two numbers and returns their sum.
- A: `add = lambda a, b: a + b`

- Q: What is wrong with this function: `def append_to(element, lst=[]):`? Explain the mutable default argument problem.
- A: The default list `[]` is created once at definition time and shared across all calls. Each call that uses the default appends to the same list. Fix: use `lst=None` and set `lst = [] if lst is None else lst` inside the function.

- Q: Explain what this code returns: `def outer(): x = 10; def inner(): return x; return inner`. What is `outer()()`?
- A: `outer()()` returns 10. `outer()` returns the `inner` function (a closure), which retains access to `x` from the enclosing scope. Calling the returned function executes `inner()`.

- Q: What scope does Python search first when resolving a variable name inside a function?
- A: Local scope (the current function), followed by Enclosing, Global, then Built-in (LEGB rule).
