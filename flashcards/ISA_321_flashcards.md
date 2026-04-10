# ISA 321: Advanced Java Programming and Data Structures - Flashcard Reference Bank

---

## Advanced Java

### Key Terms & Definitions
- **Inheritance**: A mechanism where one class acquires the fields and methods of another using the `extends` keyword, supporting code reuse and hierarchical relationships
- **Polymorphism**: The ability of objects to take many forms; achieved through method overriding (runtime/dynamic) and method overloading (compile-time/static)
- **Encapsulation**: Wrapping data and methods into a single class unit and restricting direct access using access modifiers (private, protected, public, default)
- **Abstraction**: Hiding implementation details and exposing only essential features through abstract classes and interfaces
- **Method Overriding**: Redefining a superclass method in a subclass with the same signature; resolved at runtime (dynamic dispatch)
- **Method Overloading**: Defining multiple methods with the same name but different parameter lists; resolved at compile time
- **Abstract Class**: A class declared with `abstract` that cannot be instantiated and may contain both abstract and concrete methods
- **Interface**: A contract specifying methods a class must implement; supports multiple inheritance of type; all methods are implicitly public and abstract (pre-Java 8)
- **Access Modifiers**: Keywords that set accessibility -- `private` (class only), default (package), `protected` (package + subclasses), `public` (everywhere)
- **Lambda Expression**: An anonymous function introduced in Java 8, enabling functional-style programming with syntax `(params) -> expression`

### Core Concepts (Q&A Format)
- Q: What is the difference between an abstract class and an interface?
- A: An abstract class can have constructors, instance variables, and concrete methods; a class can extend only one. An interface defines a contract with no state (pre-Java 8); a class can implement multiple interfaces. Java 8+ interfaces can have default and static methods.

- Q: What is the difference between method overloading and method overriding?
- A: Overloading uses same method name with different parameters (compile-time polymorphism). Overriding redefines a parent method in a child class with the same signature (runtime polymorphism).

- Q: Why does Java not support multiple inheritance of classes?
- A: To avoid the "diamond problem" where ambiguity arises if two parent classes have the same method. Java solves this by allowing multiple interface implementation instead.

- Q: What is dynamic method dispatch?
- A: The mechanism by which a call to an overridden method is resolved at runtime based on the actual object type, not the reference type. This is how Java implements runtime polymorphism.

- Q: How does encapsulation improve code quality?
- A: It protects internal state from unintended modification, provides controlled access through getters/setters, makes the class easier to maintain, and reduces coupling between components.

- Q: What are the four pillars of OOP?
- A: Encapsulation, Inheritance, Polymorphism, and Abstraction (often remembered as "A PIE").

- Q: What is the `super` keyword used for?
- A: To call a parent class constructor (`super()`), to access a parent class method that has been overridden (`super.methodName()`), or to refer to a parent class field hidden by a child field.

### Important Facts & Figures
- Java supports single inheritance for classes but multiple inheritance for interfaces
- The `@Override` annotation is optional but recommended; it causes a compile error if the method does not actually override a superclass method
- All classes in Java implicitly extend `java.lang.Object`
- An abstract class can have 0% to 100% abstract methods; an interface (pre-Java 8) has 100% abstract methods
- Java 8 introduced default methods in interfaces, static methods in interfaces, and lambda expressions
- The `final` keyword prevents a class from being extended, a method from being overridden, or a variable from being reassigned
- Constructor chaining uses `this()` for same-class constructors and `super()` for parent-class constructors; must be the first statement

### Common Exam Questions
- Q: If class B extends class A and both have a method `display()`, which version runs when you call `display()` on a reference of type A pointing to a B object?
- A: Class B's version runs due to dynamic method dispatch (runtime polymorphism).

- Q: Can you instantiate an abstract class? Can you instantiate an interface?
- A: Neither can be directly instantiated. You must use a concrete subclass or an anonymous inner class.

- Q: What happens if a subclass does not implement all abstract methods of its parent?
- A: The subclass must also be declared abstract, or a compile-time error occurs.

- Q: Write a lambda expression that takes two integers and returns their sum.
- A: `(int a, int b) -> a + b` or simply `(a, b) -> a + b`

---

## Recursion

### Key Terms & Definitions
- **Recursion**: A programming technique where a method calls itself to solve a problem by breaking it into smaller subproblems of the same type
- **Base Case**: The stopping condition in a recursive method that returns a result directly without making another recursive call
- **Recursive Case**: The part of the method where it calls itself with a modified argument, progressing toward the base case
- **Call Stack**: The memory structure that tracks each active method invocation; each recursive call adds a new frame
- **Stack Overflow**: A runtime error that occurs when recursive calls exceed the call stack's memory limit, typically from a missing or unreachable base case
- **Tail Recursion**: A form of recursion where the recursive call is the last operation in the method, potentially allowing compiler optimization to reuse stack frames
- **Single Recursion**: A recursive method that makes exactly one recursive call per invocation (e.g., factorial, linear search)
- **Multiple Recursion**: A recursive method that makes two or more recursive calls per invocation (e.g., Fibonacci, tree traversal)
- **Divide and Conquer**: An algorithm design pattern that recursively breaks a problem into sub-problems, solves each, and combines results (e.g., merge sort, quicksort)
- **Memoization**: An optimization technique that stores results of expensive recursive calls to avoid redundant computation

### Core Concepts (Q&A Format)
- Q: What happens if a recursive method has no base case?
- A: It will recurse infinitely until the call stack runs out of memory, causing a StackOverflowError.

- Q: How does recursion relate to the call stack?
- A: Each recursive call pushes a new frame onto the call stack containing the method's local variables and return address. When the base case is reached, frames are popped off as each call returns its result.

- Q: What is the time complexity of naive recursive Fibonacci?
- A: O(2^n) because each call branches into two more calls, resulting in exponential redundant computation. With memoization it becomes O(n).

- Q: When should you use recursion vs. iteration?
- A: Recursion is preferred for problems with naturally recursive structures (trees, graphs, divide-and-conquer). Iteration is generally more memory-efficient and faster for simple repetitive tasks.

- Q: What is the recursive formula for factorial?
- A: `factorial(n) = n * factorial(n-1)` with base case `factorial(0) = 1` or `factorial(1) = 1`.

- Q: How does merge sort use recursion?
- A: It recursively divides the array in half until single-element subarrays are reached (base case), then merges sorted halves back together.

### Important Facts & Figures
- Every recursive solution can be converted to an iterative solution (and vice versa), though one form may be far more natural
- Java does not optimize tail recursion; deep recursion can still cause StackOverflowError even with tail calls
- Default stack size in Java is typically 512KB to 1MB; can be adjusted with `-Xss` JVM flag
- Fibonacci sequence: naive recursion O(2^n), memoized O(n), iterative O(n) with O(1) space
- Factorial of 20 is the largest factorial that fits in a Java `long` (2,432,902,008,176,640,000)
- Binary search uses single recursion and runs in O(log n) time
- Tree traversals (inorder, preorder, postorder) are classic examples of recursion on data structures

### Common Exam Questions
- Q: Write a recursive method to compute the sum of digits of a positive integer.
- A: `int sumDigits(int n) { if (n < 10) return n; return n % 10 + sumDigits(n / 10); }`

- Q: Trace the call stack for `factorial(4)`.
- A: `factorial(4)` -> `factorial(3)` -> `factorial(2)` -> `factorial(1)` returns 1, then 2*1=2, then 3*2=6, then 4*6=24.

- Q: What is the base case and recursive case for binary search?
- A: Base case: element found at mid, or low > high (not found). Recursive case: search left half if target < mid, right half if target > mid.

- Q: Why is naive recursive Fibonacci inefficient? How do you fix it?
- A: It recomputes the same subproblems exponentially. Fix with memoization (store computed values in an array/map) or convert to iteration.

---

## File I/O

### Key Terms & Definitions
- **Byte Stream**: Streams that handle raw binary data using `InputStream` and `OutputStream` classes; process data 8 bits at a time
- **Character Stream**: Streams that handle Unicode text data using `Reader` and `Writer` classes; process data 16 bits at a time with automatic encoding/decoding
- **BufferedReader**: A wrapper that reads text from a character stream with internal buffering for efficiency; provides `readLine()` method
- **BufferedWriter**: A wrapper that writes text to a character stream with internal buffering; provides `newLine()` method
- **FileInputStream / FileOutputStream**: Byte stream classes for reading from and writing to files as raw bytes
- **FileReader / FileWriter**: Character stream classes for reading from and writing to text files
- **try-with-resources**: A Java 7+ feature that automatically closes resources implementing `AutoCloseable` when the try block exits
- **NIO (New I/O)**: The `java.nio` package introduced in Java 1.4 providing channels, buffers, and selectors for high-performance, non-blocking I/O
- **Path**: An NIO class representing a file system path; replaces `java.io.File` in modern Java code
- **Serialization**: The process of converting an object to a byte stream for storage or transmission using `ObjectOutputStream`

### Core Concepts (Q&A Format)
- Q: What is the difference between byte streams and character streams?
- A: Byte streams (InputStream/OutputStream) handle raw binary data (images, audio). Character streams (Reader/Writer) handle text with automatic Unicode encoding/decoding. Use character streams for text files and byte streams for everything else.

- Q: Why should you use BufferedReader instead of FileReader directly?
- A: BufferedReader reads chunks of data into an internal buffer, reducing the number of disk access operations. This dramatically improves performance, especially when reading line by line.

- Q: What is try-with-resources and why is it important?
- A: A try statement that declares resources in parentheses: `try (BufferedReader br = new BufferedReader(...)) { }`. Resources are automatically closed when the block exits, preventing resource leaks even if an exception occurs.

- Q: What are the three standard streams in Java?
- A: `System.in` (standard input, keyboard), `System.out` (standard output, console), and `System.err` (standard error output).

- Q: When would you use NIO over traditional I/O?
- A: NIO is preferred for high-performance scenarios: large file transfers, non-blocking operations, multiplexed connections, and memory-mapped files. Traditional I/O is simpler and sufficient for basic file reading/writing.

- Q: How do you read a file line by line in Java?
- A: Wrap a FileReader in a BufferedReader: `BufferedReader br = new BufferedReader(new FileReader("file.txt")); String line; while ((line = br.readLine()) != null) { ... }`

### Important Facts & Figures
- Failing to close streams causes resource leaks (file handles, memory); always use try-with-resources or finally blocks
- `BufferedReader` default buffer size is 8192 characters (8KB)
- `FileWriter` overwrites by default; pass `true` as second argument to append: `new FileWriter("file.txt", true)`
- NIO `Files.readAllLines()` reads an entire file into a `List<String>` in one call
- `Scanner` is another option for reading input; simpler but slower than `BufferedReader`
- The `Paths.get()` and `Files` utility class (NIO.2, Java 7+) simplify file operations significantly
- Character encoding matters: `InputStreamReader` allows specifying charset (e.g., UTF-8); `FileReader` uses the platform default

### Common Exam Questions
- Q: What exception must be handled or declared when working with file I/O?
- A: `IOException` (a checked exception). Methods performing file I/O must either catch it in a try-catch block or declare it with `throws IOException`.

- Q: What is the output if you write to a file using FileWriter without append mode and the file already exists?
- A: The existing file contents are overwritten completely.

- Q: Write code to copy a text file line by line using BufferedReader and BufferedWriter.
- A: `try (BufferedReader br = new BufferedReader(new FileReader("in.txt")); BufferedWriter bw = new BufferedWriter(new FileWriter("out.txt"))) { String line; while ((line = br.readLine()) != null) { bw.write(line); bw.newLine(); } }`

- Q: What is the difference between `flush()` and `close()`?
- A: `flush()` forces buffered data to be written to the destination but keeps the stream open. `close()` flushes and then releases the underlying resource.

---

## Exceptions

### Key Terms & Definitions
- **Exception**: An event that disrupts the normal flow of a program; represented by objects that are instances of classes in the `java.lang.Throwable` hierarchy
- **Checked Exception**: An exception that must be either caught or declared in the method signature at compile time (e.g., `IOException`, `SQLException`); extends `Exception` but not `RuntimeException`
- **Unchecked Exception**: A runtime exception not enforced by the compiler (e.g., `NullPointerException`, `ArrayIndexOutOfBoundsException`); extends `RuntimeException`
- **Error**: A serious problem that a program should not try to catch (e.g., `OutOfMemoryError`, `StackOverflowError`); extends `Error`
- **try block**: Encloses code that might throw an exception
- **catch block**: Handles a specific exception type thrown by the try block
- **finally block**: Executes after try/catch regardless of whether an exception occurred; used for cleanup
- **throw**: A statement used to explicitly throw an exception object: `throw new IllegalArgumentException("msg")`
- **throws**: A keyword in a method signature declaring that the method may throw specified checked exceptions
- **Custom Exception**: A user-defined exception class created by extending `Exception` (checked) or `RuntimeException` (unchecked)

### Core Concepts (Q&A Format)
- Q: What is the difference between checked and unchecked exceptions?
- A: Checked exceptions are verified at compile time and must be handled or declared (e.g., IOException). Unchecked exceptions occur at runtime and are not enforced by the compiler (e.g., NullPointerException). Checked exceptions represent recoverable conditions; unchecked represent programming errors.

- Q: What is the difference between `throw` and `throws`?
- A: `throw` is used inside a method to explicitly throw an exception object. `throws` is used in the method signature to declare that the method might throw certain checked exceptions, delegating handling to the caller.

- Q: Does the finally block always execute?
- A: Yes, except when `System.exit()` is called, the JVM crashes, or the thread is killed. The finally block executes even if a return statement is in the try or catch block.

- Q: Can a try block exist without a catch block?
- A: Yes, if it has a finally block (try-finally) or uses try-with-resources. A try block must have at least one catch or a finally.

- Q: What is the exception hierarchy in Java?
- A: `Throwable` is the root. It has two children: `Error` (unrecoverable) and `Exception` (recoverable). `Exception` has child `RuntimeException` (unchecked). All other `Exception` subclasses are checked.

- Q: What happens if an exception is thrown but never caught?
- A: The exception propagates up the call stack. If no method catches it, the JVM terminates the thread and prints the stack trace.

### Important Facts & Figures
- Multi-catch syntax (Java 7+): `catch (IOException | SQLException e)` handles multiple exception types in one block
- The exception in a multi-catch is implicitly `final` and cannot be reassigned
- Try-with-resources (Java 7+) automatically closes resources that implement `AutoCloseable`
- Catching `Exception` or `Throwable` is considered bad practice as it catches too broadly
- Best practice: throw early (fail fast), catch late (let the caller decide how to handle)
- A `finally` block return value overrides a `try` block return value (avoid returning from finally)
- Common unchecked exceptions: `NullPointerException`, `ArrayIndexOutOfBoundsException`, `ClassCastException`, `IllegalArgumentException`, `ArithmeticException`

### Common Exam Questions
- Q: What is the output of: `try { return 1; } finally { return 2; }`?
- A: Returns 2. The finally block's return overrides the try block's return.

- Q: Can you catch an Error? Should you?
- A: You can (Error extends Throwable), but you generally should not because Errors represent unrecoverable conditions like OutOfMemoryError.

- Q: Write a custom checked exception class.
- A: `public class InsufficientFundsException extends Exception { public InsufficientFundsException(String msg) { super(msg); } }`

- Q: What exception is thrown by `int x = 5/0;`?
- A: `ArithmeticException` (an unchecked exception) with the message "/ by zero".

- Q: In what order are catch blocks evaluated, and why does order matter?
- A: Catch blocks are evaluated top to bottom. A more specific exception must come before a more general one, or the code will not compile (the general catch would shadow the specific one).

---

## Generics

### Key Terms & Definitions
- **Generics**: A Java feature allowing classes, interfaces, and methods to be parameterized by type, providing compile-time type safety
- **Type Parameter**: A placeholder for a type, conventionally named `T` (type), `E` (element), `K` (key), `V` (value), `N` (number)
- **Type Erasure**: The compiler process that removes generic type information at compile time, replacing type parameters with their bounds (or Object if unbounded) in the bytecode
- **Bounded Type Parameter**: A restriction on a type parameter using `extends`: `<T extends Number>` means T must be Number or a subclass
- **Upper Bounded Wildcard**: `? extends T` -- accepts T or any subtype; used for reading (producer)
- **Lower Bounded Wildcard**: `? super T` -- accepts T or any supertype; used for writing (consumer)
- **Unbounded Wildcard**: `?` -- accepts any type; equivalent to `? extends Object`
- **Generic Class**: A class with one or more type parameters: `class Box<T> { T item; }`
- **Generic Method**: A method with its own type parameter: `<T> T getFirst(List<T> list)`
- **Raw Type**: Using a generic class without specifying a type parameter (e.g., `List` instead of `List<String>`); produces compiler warnings

### Core Concepts (Q&A Format)
- Q: What is type erasure and why does Java use it?
- A: Type erasure removes generic type info at compile time so bytecode is compatible with pre-generics Java. `List<String>` and `List<Integer>` become the same `List` class at runtime. This was done for backward compatibility.

- Q: What is the PECS principle?
- A: Producer Extends, Consumer Super. Use `? extends T` when you only read from a structure (it produces values). Use `? super T` when you only write to a structure (it consumes values).

- Q: Why can you not create an array of a generic type like `new T[10]`?
- A: Due to type erasure, the JVM does not know the actual type of T at runtime, so it cannot create a properly typed array. Use `ArrayList<T>` instead.

- Q: What is the difference between `List<Object>` and `List<?>`?
- A: `List<Object>` only accepts `List<Object>`. `List<?>` accepts a List of any type (`List<String>`, `List<Integer>`, etc.) but you can only read from it as Object, not add to it.

- Q: Can you overload methods that differ only by generic type parameter?
- A: No. Due to type erasure, `void print(List<String> l)` and `void print(List<Integer> l)` have the same erasure and cause a compile error.

- Q: What is a bounded type parameter? Give an example.
- A: A restriction using `extends`: `<T extends Comparable<T>>` means T must implement Comparable, allowing you to call `compareTo()` on T objects.

### Important Facts & Figures
- Generics were introduced in Java 5 (J2SE 5.0, released 2004)
- Type parameters cannot be primitive types; use wrapper classes (`Integer` not `int`)
- You cannot use `instanceof` with parameterized types (e.g., `x instanceof List<String>` is illegal)
- The diamond operator `<>` (Java 7+) infers type arguments: `List<String> list = new ArrayList<>()`
- Generics are purely a compile-time feature; at runtime, all generic types appear as their raw types
- Common generic collections: `ArrayList<E>`, `HashMap<K,V>`, `HashSet<E>`, `LinkedList<E>`, `TreeMap<K,V>`
- Multiple bounds are allowed: `<T extends Comparable<T> & Serializable>` (class first, then interfaces)

### Common Exam Questions
- Q: What is the output of: `List<String> l1 = new ArrayList<>(); List<Integer> l2 = new ArrayList<>(); System.out.println(l1.getClass() == l2.getClass());`?
- A: `true`. Due to type erasure, both are `ArrayList` at runtime.

- Q: Write a generic method that returns the maximum of three Comparable objects.
- A: `public static <T extends Comparable<T>> T max(T a, T b, T c) { T m = a; if (b.compareTo(m) > 0) m = b; if (c.compareTo(m) > 0) m = c; return m; }`

- Q: Why does `List<Dog>` not extend `List<Animal>` even though Dog extends Animal?
- A: Generics are invariant. If `List<Dog>` were a subtype of `List<Animal>`, you could add a Cat to a Dog list through the Animal reference, violating type safety.

- Q: What is a raw type and why should you avoid it?
- A: A raw type is a generic class used without type parameters (e.g., `List` instead of `List<String>`). It bypasses compile-time type checking, risking ClassCastException at runtime.

---

## Data Structures

### Key Terms & Definitions
- **Array**: A fixed-size, contiguous memory structure storing elements of the same type; O(1) index access, O(n) insertion/deletion
- **Linked List**: A sequence of nodes where each node stores data and a reference to the next node; O(1) insertion/deletion at known position, O(n) access
- **Singly Linked List**: Each node points to the next node only; traversal is one-directional
- **Doubly Linked List**: Each node points to both the next and previous nodes; supports bidirectional traversal
- **Stack**: A LIFO (Last-In, First-Out) data structure with push (add to top) and pop (remove from top) operations, both O(1)
- **Queue**: A FIFO (First-In, First-Out) data structure with enqueue (add to rear) and dequeue (remove from front) operations, both O(1)
- **Binary Tree**: A tree where each node has at most two children (left and right)
- **Binary Search Tree (BST)**: A binary tree where left child < parent < right child; O(log n) search/insert/delete when balanced, O(n) when degenerate
- **Hash Table**: A key-value data structure that uses a hash function to map keys to array indices; O(1) average lookup, O(n) worst case
- **Collision**: When two different keys produce the same hash index; resolved by chaining (linked lists) or open addressing (probing)

### Core Concepts (Q&A Format)
- Q: When would you choose a linked list over an array?
- A: When frequent insertions/deletions are needed at arbitrary positions and you do not need random access. Linked lists do not require contiguous memory or resizing.

- Q: What are the applications of a stack?
- A: Function call management (call stack), undo/redo operations, expression evaluation and parsing, balanced parentheses checking, depth-first search, and backtracking algorithms.

- Q: What is the difference between a stack and a queue?
- A: Stack is LIFO (last in, first out) -- think stack of plates. Queue is FIFO (first in, first out) -- think line at a store. Stack uses push/pop; queue uses enqueue/dequeue.

- Q: What makes a BST degenerate and why is it a problem?
- A: Inserting sorted data creates a degenerate BST (essentially a linked list), degrading all operations from O(log n) to O(n). Self-balancing trees (AVL, Red-Black) prevent this.

- Q: How does a hash table handle collisions?
- A: Chaining: each bucket holds a linked list of entries with the same hash. Open addressing: probe for the next empty slot using linear probing, quadratic probing, or double hashing.

- Q: What is the difference between ArrayList and LinkedList in Java?
- A: ArrayList uses a dynamic array (O(1) random access, O(n) insertion in middle). LinkedList uses a doubly linked list (O(n) random access, O(1) insertion at known position). ArrayList is generally faster due to cache locality.

- Q: What are the three tree traversal orders?
- A: Inorder (left, root, right) -- gives sorted order for BST. Preorder (root, left, right). Postorder (left, right, root).

### Important Facts & Figures
- Java's `ArrayList` grows by 50% when capacity is exceeded (new capacity = old * 1.5)
- Java's `HashMap` default initial capacity is 16 with load factor 0.75; rehashes when 75% full
- A balanced BST of n nodes has height O(log n); a degenerate BST has height O(n)
- AVL trees maintain balance by ensuring the height difference between left and right subtrees is at most 1
- Priority Queue is implemented as a heap (min-heap or max-heap); insert and extract in O(log n)
- A hash function should be deterministic, uniform, and efficient to minimize collisions
- Java `Stack` class extends `Vector`; prefer `Deque` (ArrayDeque) for stack operations in modern Java
- Singly linked list uses less memory per node (one pointer) vs. doubly linked list (two pointers)

### Common Exam Questions
- Q: What is the time complexity for search, insert, and delete in a hash table (average vs. worst)?
- A: Average: O(1) for all three. Worst case: O(n) when all keys collide into the same bucket.

- Q: Trace an inorder traversal of a BST with values [5, 3, 7, 2, 4, 6, 8] inserted in that order.
- A: Inorder traversal visits: 2, 3, 4, 5, 6, 7, 8 (ascending sorted order).

- Q: What data structure would you use to check if parentheses in an expression are balanced?
- A: A stack. Push opening brackets, pop when closing bracket matches. If stack is empty at the end and all brackets matched, the expression is balanced.

- Q: Compare the space complexity of an array vs. a linked list for n elements.
- A: Array: O(n) for data only. Linked list: O(n) for data plus O(n) for pointers (next, and prev if doubly linked), so higher memory overhead per element.

---

## Algorithm Analysis

### Key Terms & Definitions
- **Big O Notation**: Describes the upper bound (worst-case) growth rate of an algorithm's time or space as input size n increases
- **O(1) - Constant**: Runtime does not change with input size (e.g., array index access, hash table lookup)
- **O(log n) - Logarithmic**: Runtime grows logarithmically; halves the problem each step (e.g., binary search)
- **O(n) - Linear**: Runtime grows proportionally with input size (e.g., linear search, single loop)
- **O(n log n) - Linearithmic**: Typical of efficient sorting algorithms (e.g., merge sort, quicksort average case)
- **O(n^2) - Quadratic**: Runtime grows with the square of input; nested loops (e.g., bubble sort, selection sort, insertion sort)
- **O(2^n) - Exponential**: Runtime doubles with each additional input element (e.g., naive recursive Fibonacci, power set)
- **Time Complexity**: A measure of how the number of operations grows relative to input size
- **Space Complexity**: A measure of how much additional memory an algorithm requires relative to input size
- **Omega Notation**: Describes the best-case (lower bound) growth rate of an algorithm
- **Theta Notation**: Describes the tight bound (both upper and lower) growth rate when best and worst cases match

### Core Concepts (Q&A Format)
- Q: Why do we use Big O notation instead of measuring actual execution time?
- A: Actual time depends on hardware, language, and system load. Big O provides a hardware-independent measure of how an algorithm scales as input grows, focusing on the dominant term.

- Q: What is the time complexity of merge sort vs. quicksort?
- A: Merge sort: O(n log n) in all cases. Quicksort: O(n log n) average, O(n^2) worst case (when pivot is always the smallest/largest). Quicksort is typically faster in practice due to lower constant factors and better cache performance.

- Q: How do you determine the Big O of nested loops?
- A: Multiply the complexities of each loop. Two nested loops each iterating n times = O(n * n) = O(n^2). A loop of n containing a loop of m = O(n * m).

- Q: What is the space complexity of merge sort vs. quicksort?
- A: Merge sort: O(n) extra space for the temporary arrays. Quicksort: O(log n) extra space for the recursive call stack (in-place partitioning).

- Q: What does "drop the constants and lower-order terms" mean?
- A: In Big O, we focus on growth rate for large n. So 3n^2 + 5n + 100 simplifies to O(n^2) because n^2 dominates as n grows large.

- Q: What is amortized analysis?
- A: It averages the time per operation over a worst-case sequence. For example, ArrayList resizing is O(n) occasionally, but amortized O(1) per insertion because resizes are infrequent.

### Important Facts & Figures
- Complexity hierarchy (slowest to fastest): O(n!) > O(2^n) > O(n^2) > O(n log n) > O(n) > O(log n) > O(1)
- Sorting 1 million items: bubble sort ~10^12 operations vs. merge sort ~20 million operations
- Binary search requires a sorted array and runs in O(log n) -- searching 1 billion items takes at most ~30 comparisons
- Stable sorting algorithms maintain the relative order of equal elements: merge sort (stable), quicksort (not stable), heapsort (not stable)
- In-place algorithms use O(1) extra space: insertion sort, heapsort. Not in-place: merge sort O(n)
- Hash table operations are O(1) average but O(n) worst case; BST operations are O(log n) when balanced
- Logarithmic time means the problem is halved at each step; log2(1,000,000) is approximately 20
- The lower bound for comparison-based sorting is O(n log n); no comparison sort can do better

### Common Exam Questions
- Q: Rank the following from fastest to slowest: O(n^2), O(1), O(n log n), O(log n), O(n), O(2^n).
- A: O(1) < O(log n) < O(n) < O(n log n) < O(n^2) < O(2^n)

- Q: What is the time complexity of this code? `for (int i = 0; i < n; i++) { for (int j = i; j < n; j++) { ... } }`
- A: O(n^2). The inner loop runs n + (n-1) + (n-2) + ... + 1 = n(n+1)/2 times, which is O(n^2).

- Q: Compare bubble sort, selection sort, insertion sort, and merge sort by time complexity.
- A: Bubble sort: O(n^2) all cases. Selection sort: O(n^2) all cases. Insertion sort: O(n) best, O(n^2) worst. Merge sort: O(n log n) all cases.

- Q: What is the best-case time complexity of insertion sort and why?
- A: O(n), when the array is already sorted. Each element only needs one comparison to confirm it is in the right position.

- Q: An algorithm's runtime is T(n) = 5n^3 + 2n^2 + 10n + 7. What is its Big O?
- A: O(n^3). The highest-order term dominates; constants and lower-order terms are dropped.
