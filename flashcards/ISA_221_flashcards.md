# ISA 221: Introduction to Programming - Flashcard Reference Bank

---

## Structured Programming

### Key Terms & Definitions
- **Structured Programming**: A programming paradigm that uses only sequence, selection, and iteration to control program flow, avoiding arbitrary jumps like `goto`.
- **Sequence**: Statements executed one after another in linear, top-to-bottom order.
- **Selection**: Conditional branching (if/else, switch) that chooses execution paths based on Boolean conditions.
- **Iteration**: Loop constructs (for, while, do-while) that repeat a code block until a termination condition is met.
- **Structured Program Theorem**: The Bohm-Jacopini theorem (1966) proving any computable function can be expressed using only sequence, selection, and iteration.
- **Spaghetti Code**: Disorganized, hard-to-follow code that results from excessive use of goto statements and poor structure.
- **Modular Decomposition**: Breaking a program into self-contained subroutines or modules, each responsible for a single task.
- **Block Structure**: Grouping related statements into blocks (using braces or indentation) to clarify scope and logical grouping.
- **Subroutine**: A named, reusable block of code that performs a specific task, callable from other parts of the program.
- **Edsger Dijkstra**: Dutch computer scientist who published "Go To Statement Considered Harmful" (1968) and championed structured programming.

### Core Concepts (Q&A Format)
- Q: What are the three fundamental control structures of structured programming?
- A: Sequence (linear execution), selection (conditional branching), and iteration (loops).

- Q: What did the Bohm-Jacopini theorem prove?
- A: That any computable function can be expressed using only sequence, selection, and iteration, making goto unnecessary.

- Q: Why is goto considered harmful in structured programming?
- A: It creates unpredictable jumps in control flow, producing "spaghetti code" that is difficult to read, debug, and maintain.

- Q: What is the relationship between structured programming and modular design?
- A: Structured programming encourages breaking programs into self-contained modules/subroutines, each handling one task, promoting reuse and easier debugging.

- Q: How does block structure support structured programming?
- A: Blocks group related statements together (using braces or indentation), making scope and logical groupings explicit and code more readable.

- Q: What was the historical significance of Dijkstra's 1968 letter?
- A: It argued against goto statements and catalyzed the shift toward structured programming as the standard paradigm in software development.

- Q: What is the difference between a structured and unstructured program?
- A: A structured program uses only sequence, selection, and iteration with clear block structure; an unstructured program uses arbitrary jumps (goto) with no enforced logical organization.

### Important Facts & Figures
- The structured program theorem was published by Corrado Bohm and Giuseppe Jacopini in 1966.
- Dijkstra's "Go To Statement Considered Harmful" was published in 1968 in Communications of the ACM.
- Structured programming became the dominant paradigm in the 1970s and remains the foundation of modern programming.
- All modern programming languages (Python, Java, C++, JavaScript) are built on structured programming principles.
- Structured programming reduces debugging time by making control flow predictable and traceable.
- The three structures (sequence, selection, iteration) are sufficient to write any algorithm.

### Common Exam Questions
- Q: List and define the three control structures used in structured programming.
- A: Sequence (linear execution), selection (if/else conditional branching), iteration (loop repetition).

- Q: Who proposed that goto statements are harmful, and why?
- A: Edsger Dijkstra, because goto creates unpredictable control flow ("spaghetti code") that is hard to read and maintain.

- Q: What does the structured program theorem state?
- A: Any computable function can be implemented using only sequence, selection, and iteration -- goto is never necessary.

- Q: Give two advantages of structured programming over unstructured programming.
- A: Improved readability/maintainability and easier debugging due to predictable, logical control flow.

---

## Control Structures

### Key Terms & Definitions
- **Control Structure**: A programming construct that determines the order in which statements are executed.
- **Sequential Control**: The default execution mode where statements run one after another in written order.
- **If Statement**: A selection structure that executes a block of code only if a specified Boolean condition is true.
- **If-Else Statement**: A selection structure providing two paths: one if the condition is true, another if false.
- **Else-If Chain**: Multiple conditions checked in sequence; the first true condition's block executes, and the rest are skipped.
- **Switch/Case Statement**: A multi-way selection structure that matches a variable's value against predefined cases.
- **For Loop**: A count-controlled loop that executes a fixed number of times, with an initializer, condition, and increment.
- **While Loop**: A pre-test loop that checks its condition before each iteration; executes zero or more times.
- **Do-While Loop**: A post-test loop that executes its body at least once, then checks the condition.
- **Break**: A keyword that immediately exits the innermost loop or switch statement.
- **Continue**: A keyword that skips the remainder of the current loop iteration and proceeds to the next.
- **Boolean Expression**: An expression that evaluates to true or false, used to drive selection and iteration.

### Core Concepts (Q&A Format)
- Q: What is the key difference between a while loop and a do-while loop?
- A: A while loop checks the condition before executing (may run zero times); a do-while checks after executing (always runs at least once).

- Q: When should you use a for loop versus a while loop?
- A: Use a for loop when the number of iterations is known in advance; use a while loop when the number of iterations depends on a runtime condition.

- Q: What happens when a break statement is encountered inside a loop?
- A: Execution immediately exits the innermost enclosing loop, and the program continues with the statement after the loop.

- Q: What is an infinite loop, and how does it occur?
- A: A loop whose termination condition is never met, so it runs forever. It occurs when the loop variable is never updated or the condition is always true.

- Q: How do nested control structures work?
- A: One control structure is placed inside another (e.g., an if inside a for loop), allowing complex decision-making and data processing patterns.

- Q: What are the six comparison operators commonly used in Boolean expressions?
- A: Equal to (==), not equal (!=), less than (<), greater than (>), less than or equal (<=), greater than or equal (>=).

- Q: What are the three logical operators used to combine Boolean expressions?
- A: AND (&&), OR (||), and NOT (!).

### Important Facts & Figures
- Every program uses sequential control as its baseline execution mode.
- The if-else structure provides exactly two mutually exclusive paths of execution.
- A for loop has three components: initialization, condition, and update (e.g., `for(int i=0; i<10; i++)`).
- Switch/case statements often require a break at the end of each case to prevent "fall-through" to the next case.
- Nested loops multiply iterations: a loop of n inside a loop of m runs n * m times total.
- Short-circuit evaluation means `&&` stops evaluating if the left operand is false; `||` stops if the left operand is true.
- An off-by-one error is one of the most common bugs with loops, occurring when the loop runs one too many or one too few times.

### Common Exam Questions
- Q: What output does a do-while loop produce if its condition is initially false?
- A: The loop body executes exactly once because the condition is checked after the first execution.

- Q: Trace the output of: `for(int i = 0; i < 5; i++) { if(i == 3) continue; print(i); }`
- A: Output is 0, 1, 2, 4. When i equals 3, continue skips the print and moves to the next iteration.

- Q: What is fall-through in a switch statement, and how is it prevented?
- A: Fall-through occurs when execution continues into the next case because there is no break statement. It is prevented by placing break at the end of each case.

- Q: Explain the difference between == and = in a conditional statement.
- A: == is the comparison operator (tests equality); = is the assignment operator (assigns a value). Using = instead of == in a condition is a common bug.

---

## Object-Oriented Programming

### Key Terms & Definitions
- **Object-Oriented Programming (OOP)**: A paradigm that organizes software around objects that bundle data (attributes) and behavior (methods).
- **Object**: An instance of a class that holds its own state (attribute values) and can perform actions (methods).
- **Encapsulation**: Bundling data and methods together within a class and restricting direct access to internal data via access modifiers.
- **Inheritance**: A mechanism where a subclass acquires attributes and methods from a superclass, establishing an "is-a" relationship.
- **Polymorphism**: The ability of different objects to respond to the same method call in their own way ("many forms").
- **Abstraction**: Hiding complex implementation details behind simple interfaces (abstract classes and interfaces).
- **Method Overloading**: Compile-time polymorphism where multiple methods share the same name but differ in parameter lists.
- **Method Overriding**: Runtime polymorphism where a subclass provides its own implementation of a method inherited from its superclass.
- **Composition**: A "has-a" relationship where an object contains references to other objects, as an alternative to inheritance.
- **Message Passing**: Objects communicate by calling methods on one another, promoting loose coupling.
- **Interface**: A contract that defines method signatures without implementations; classes that implement it must provide the method bodies.
- **Abstract Class**: A class that cannot be instantiated and may contain both abstract (unimplemented) and concrete (implemented) methods.

### Core Concepts (Q&A Format)
- Q: What are the four pillars of OOP?
- A: Encapsulation, inheritance, polymorphism, and abstraction.

- Q: How does encapsulation protect data integrity?
- A: By making attributes private and providing public getter/setter methods, so external code cannot directly modify internal state in uncontrolled ways.

- Q: What is the difference between method overloading and method overriding?
- A: Overloading uses the same method name with different parameters (compile-time); overriding replaces an inherited method with a new implementation in a subclass (runtime).

- Q: Why is composition sometimes preferred over inheritance?
- A: Composition provides greater flexibility and avoids tight coupling; you can change component behavior at runtime without rigid class hierarchies.

- Q: What is the difference between an abstract class and an interface?
- A: An abstract class can have both implemented and abstract methods and instance variables; an interface (in most languages) defines only method signatures that implementing classes must fulfill.

- Q: What does the "is-a" relationship mean in OOP?
- A: It describes inheritance: a Dog "is-a" Animal, meaning Dog inherits from Animal and can be used wherever an Animal is expected.

- Q: How does polymorphism support extensibility?
- A: New subclasses can be added with their own method implementations, and existing code that references the superclass type works with the new subclass without modification.

### Important Facts & Figures
- OOP was pioneered by Simula (1960s) and Smalltalk (1970s); it became mainstream with C++ and Java in the 1990s.
- Java, Python, C++, C#, Ruby, and Swift are all OOP languages.
- Single inheritance means a class can extend only one superclass (Java); multiple inheritance allows extending several (C++, Python).
- The SOLID principles (Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion) guide good OOP design.
- Encapsulation is often called "data hiding" because internal state is not directly accessible.
- Polymorphism reduces code duplication by allowing one interface to serve multiple implementations.

### Common Exam Questions
- Q: Define encapsulation and give an example of how it is implemented in code.
- A: Encapsulation bundles data and methods in a class with private fields and public getters/setters. Example: a private `balance` field in a BankAccount class with public `getBalance()` and `deposit()` methods.

- Q: Explain the difference between compile-time and runtime polymorphism.
- A: Compile-time polymorphism is method overloading (resolved at compilation); runtime polymorphism is method overriding (resolved during execution based on the actual object type).

- Q: What is the purpose of inheritance in OOP?
- A: To promote code reuse by allowing subclasses to inherit attributes and methods from a superclass, and to establish hierarchical relationships.

- Q: A class Dog extends Animal. If Animal has a method speak() and Dog overrides it, which version runs when you call speak() on a Dog object?
- A: The Dog version runs, because runtime polymorphism resolves the call to the overriding method in the actual object's class.

---

## Classes

### Key Terms & Definitions
- **Class**: A blueprint or template that defines the attributes (data) and methods (behavior) for objects.
- **Object/Instance**: A concrete entity created from a class, occupying its own memory and holding its own attribute values.
- **Attribute (Field/Property)**: A variable declared within a class that stores the state of each object.
- **Instance Attribute**: An attribute unique to each object (e.g., each Student has its own `name`).
- **Class Attribute (Static)**: An attribute shared by all instances of the class (e.g., a counter of total students).
- **Method**: A function defined inside a class that describes a behavior the object can perform.
- **Constructor**: A special method automatically called when an object is instantiated, used to initialize attributes (e.g., `__init__` in Python, same-name method in Java).
- **Default Constructor**: A no-argument constructor provided by the compiler if none is explicitly defined.
- **Accessor (Getter)**: A method that returns the value of a private attribute without modifying it.
- **Mutator (Setter)**: A method that modifies the value of a private attribute, often with validation logic.
- **Access Modifier**: Keywords (public, private, protected) that control visibility of class members to outside code.
- **this/self Reference**: A keyword used inside a class to refer to the current instance, allowing access to its own attributes and methods.

### Core Concepts (Q&A Format)
- Q: What is the difference between a class and an object?
- A: A class is a blueprint defining structure and behavior; an object is a specific instance of that class with its own data values in memory.

- Q: What is the purpose of a constructor?
- A: To initialize an object's attributes to starting values when the object is first created.

- Q: Why are access modifiers important?
- A: They enforce encapsulation by controlling which parts of a class are visible and modifiable by external code, protecting data integrity.

- Q: What is the difference between an instance attribute and a class (static) attribute?
- A: Instance attributes belong to each individual object; class/static attributes are shared across all instances of the class.

- Q: What happens if you do not define a constructor in your class?
- A: The compiler provides a default no-argument constructor that initializes attributes to default values (0, null, false, etc.).

- Q: What is the role of the `this` (or `self`) keyword?
- A: It refers to the current object instance, distinguishing between instance attributes and local variables with the same name.

- Q: What is instantiation?
- A: The process of creating a concrete object from a class template, typically using the `new` keyword (Java/C++) or calling the class directly (Python).

### Important Facts & Figures
- A class can have multiple constructors (constructor overloading) with different parameter lists.
- In Java, `private` members are accessible only within the class; `protected` adds access to subclasses; `public` allows access from anywhere.
- In Python, there are no strict access modifiers; a leading underscore `_` signals "private by convention," and `__` triggers name mangling.
- The `toString()` method (Java) or `__str__` method (Python) defines how an object is represented as a string.
- Static methods belong to the class itself, not to any instance, and cannot access instance attributes.
- Each object created from a class occupies its own space in memory (heap allocation in most languages).
- Getter/setter methods can include validation logic (e.g., preventing a negative age from being set).

### Common Exam Questions
- Q: Write a simple class with a constructor, one private attribute, and a getter method.
- A: (Java) `class Student { private String name; Student(String name) { this.name = name; } public String getName() { return name; } }`

- Q: What is the difference between a getter and a setter?
- A: A getter (accessor) returns a private attribute's value; a setter (mutator) modifies it, potentially with validation.

- Q: If you create two objects from the same class, do they share the same attribute values?
- A: No. Each object has its own copy of instance attributes. Only class/static attributes are shared.

- Q: Explain why constructors do not have a return type.
- A: Constructors are not regular methods; they are invoked automatically during object creation and their sole purpose is initialization, not returning a value.

---

## Debugging

### Key Terms & Definitions
- **Debugging**: The systematic process of identifying, isolating, and fixing errors (bugs) in a program.
- **Bug**: An error, flaw, or fault in a program that causes incorrect or unexpected behavior.
- **Syntax Error**: A violation of the programming language's grammar rules, caught by the compiler/interpreter before execution.
- **Runtime Error**: An error that occurs during program execution (e.g., division by zero, null pointer access), causing the program to crash.
- **Logic Error**: An error where the program runs without crashing but produces incorrect results due to flawed algorithm logic.
- **Breakpoint**: A marker on a line of code that tells the debugger to pause execution at that point for inspection.
- **Conditional Breakpoint**: A breakpoint that pauses execution only when a specified condition evaluates to true.
- **Step Over**: A debugger command that executes the current line and moves to the next, without entering called functions.
- **Step Into**: A debugger command that enters a called function to trace its internal execution line by line.
- **Step Out**: A debugger command that finishes executing the current function and returns to the caller.
- **Watch Variable**: A variable or expression monitored in real time by the debugger, showing its value as execution progresses.
- **Call Stack**: A display of the chain of function calls leading to the current point of execution, useful for tracing how the program arrived at a certain state.

### Core Concepts (Q&A Format)
- Q: What is the difference between a syntax error, a runtime error, and a logic error?
- A: Syntax errors violate language grammar and are caught before execution. Runtime errors occur during execution and crash the program. Logic errors produce wrong results but no crashes.

- Q: Why are logic errors the hardest type of bug to find?
- A: Because the program compiles and runs without error messages; the only indication is incorrect output, requiring careful analysis of the algorithm.

- Q: What is the advantage of a conditional breakpoint over a regular breakpoint?
- A: It pauses only when a specific condition is met, which is essential for debugging issues that occur only on certain iterations or with specific data values.

- Q: When should you use Step Into versus Step Over?
- A: Use Step Into when you suspect the bug is inside a called function; use Step Over when you trust the function and want to check the result without tracing its internals.

- Q: What is rubber duck debugging?
- A: Explaining your code line by line to another person or object, forcing you to articulate assumptions and often revealing the error through the explanation process.

- Q: How does the call stack help in debugging?
- A: It shows the sequence of function calls that led to the current execution point, helping you trace where a bad value or unexpected path originated.

### Important Facts & Figures
- The term "bug" dates back to Grace Hopper finding an actual moth in the Harvard Mark II computer in 1947.
- Studies show developers spend 35-50% of their time debugging and testing, not writing new code.
- Syntax errors are the easiest to fix because the compiler/interpreter provides the exact line number and error description.
- Print/log debugging is the simplest technique and works in any environment, but can clutter code and is inefficient for complex bugs.
- Binary search debugging narrows the bug location by half with each test, similar to a binary search algorithm.
- Modern IDEs (Visual Studio, IntelliJ, PyCharm, VS Code) all provide integrated graphical debuggers with breakpoints, stepping, and watch capabilities.
- Exception handling (try/catch) is a programming mechanism related to debugging that gracefully handles runtime errors.

### Common Exam Questions
- Q: Classify the following errors: (a) missing semicolon, (b) dividing by zero, (c) using < instead of <=.
- A: (a) Syntax error, (b) Runtime error, (c) Logic error.

- Q: Describe two techniques for locating a bug in a program.
- A: (1) Setting breakpoints and stepping through code with a debugger to inspect variable values. (2) Inserting print statements at strategic points to trace execution flow and variable changes.

- Q: What is the purpose of a watch variable in a debugger?
- A: To monitor a variable's value in real time as the program executes, helping identify where it takes on an unexpected value.

- Q: A program compiles and runs but always outputs 0 instead of the correct sum. What type of error is this, and how would you debug it?
- A: This is a logic error. Debug by setting a breakpoint at the calculation, stepping through the loop, and watching the sum variable to find where the logic deviates from expectations.

---

## Program Design

### Key Terms & Definitions
- **Program Design**: The planning phase where a programmer maps out the logic, structure, and flow of a program before writing code.
- **Top-Down Design (Stepwise Refinement)**: Starting with the overall problem and progressively breaking it into smaller sub-problems until each is simple enough to implement directly.
- **Pseudocode**: An informal, language-independent description of an algorithm using a mix of natural language and programming-like syntax.
- **Flowchart**: A visual diagram representing program logic using standardized symbols (ovals, rectangles, diamonds, arrows).
- **Algorithm**: A step-by-step procedure for solving a specific problem, defined before coding begins.
- **Modular Design**: Dividing a program into independent, self-contained modules (functions or classes), each handling one task.
- **IPO Model (Input-Process-Output)**: A design framework that defines what data a program receives, what operations it performs, and what results it produces.
- **Desk Checking (Dry Run)**: Manually tracing through pseudocode or a flowchart with sample data to verify correctness before coding.
- **Coupling**: The degree of interdependence between modules; low coupling is desirable for maintainability.
- **Cohesion**: The degree to which elements within a module belong together; high cohesion means the module does one well-defined thing.

### Core Concepts (Q&A Format)
- Q: Why should you design a program before writing code?
- A: Design reduces errors, simplifies implementation, and produces software that is easier to test and maintain by thinking through logic before syntax.

- Q: What is the difference between pseudocode and a flowchart?
- A: Pseudocode is a text-based, informal description of an algorithm; a flowchart is a visual diagram using standardized symbols to show the same logic graphically.

- Q: How does top-down design work?
- A: You start with the main problem, decompose it into sub-problems, and continue refining each sub-problem until it is simple enough to code directly as a function or module.

- Q: What are the standard flowchart symbols?
- A: Oval (start/end), rectangle (process/action), diamond (decision/condition), parallelogram (input/output), and arrows (flow direction).

- Q: What is the IPO model and how is it used?
- A: It stands for Input-Process-Output. It defines what data enters the program, what computations are performed, and what results are produced -- used as a first step in program design.

- Q: What is the difference between high cohesion and low coupling?
- A: High cohesion means a module focuses on one task (good). Low coupling means modules have minimal dependencies on each other (also good). Both are design goals.

- Q: What is desk checking?
- A: Manually tracing through an algorithm with sample data on paper to verify its logic produces the correct output before writing actual code.

### Important Facts & Figures
- The IPO model is often the first design tool taught in introductory programming courses because of its simplicity.
- Flowcharts were standardized by ANSI (American National Standards Institute) and ISO for consistent symbol usage.
- Pseudocode has no formal syntax rules -- it is meant to be readable by anyone, regardless of programming language knowledge.
- Top-down design is also called "divide and conquer" in the context of problem-solving strategy.
- Good modular design aims for modules with high cohesion (focused purpose) and low coupling (minimal interdependence).
- The Unified Modeling Language (UML) extends flowcharts for object-oriented design with class diagrams, sequence diagrams, and more.
- Studies show that time invested in design saves 10-100x the effort that would be spent fixing bugs discovered later in development.

### Common Exam Questions
- Q: Draw a flowchart for a program that reads a number and prints whether it is positive, negative, or zero.
- A: Start (oval) -> Input number (parallelogram) -> Decision: number > 0? (diamond) -> Yes: Print "Positive" (rectangle) -> End. No: Decision: number < 0? -> Yes: Print "Negative" -> End. No: Print "Zero" -> End.

- Q: Write pseudocode to calculate the average of N numbers entered by the user.
- A: `READ N; SET sum = 0; FOR i = 1 TO N: READ number; sum = sum + number; END FOR; average = sum / N; PRINT average`

- Q: What are two advantages of using pseudocode during program design?
- A: (1) It is language-independent, so anyone can understand the logic. (2) It lets you focus on algorithm correctness without worrying about syntax errors.

- Q: Explain the relationship between top-down design and modular programming.
- A: Top-down design decomposes a problem into sub-problems; modular programming implements each sub-problem as a separate, self-contained module/function. They work together naturally.

---
