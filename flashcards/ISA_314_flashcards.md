# ISA 314: Visual Basic Programming - Flashcard Reference Bank

---

## Visual Basic .NET

### Key Terms & Definitions
- **VB.NET**: An object-oriented programming language developed by Microsoft as part of the .NET Framework, featuring English-like syntax for building type-safe applications.
- **Object-Oriented Programming (OOP)**: A programming paradigm where code is organized around objects that combine data (properties) and behavior (methods), supporting encapsulation, inheritance, and polymorphism.
- **Event-Driven Programming**: A paradigm where program flow is determined by events such as user actions (clicks, keystrokes) or system-generated signals rather than sequential execution.
- **RAD (Rapid Application Development)**: A development methodology emphasizing quick prototyping and iterative delivery, supported in VB.NET by Visual Studio's drag-and-drop designers.
- **.NET Framework**: Microsoft's software platform providing a large class library (FCL) and a runtime environment (CLR) for building and running applications.
- **CLR (Common Language Runtime)**: The virtual machine component of .NET that manages code execution, memory allocation, garbage collection, and type safety.
- **Option Strict**: A VB.NET compiler directive that, when enabled, disallows implicit narrowing conversions and late binding, enforcing strict type safety.
- **Option Explicit**: A VB.NET compiler directive that requires all variables to be explicitly declared before use, preventing accidental creation of new variables through typos.
- **Namespace**: An organizational container in .NET that groups related classes, structures, and interfaces to avoid naming conflicts (e.g., System.IO, System.Data).
- **IDE (Integrated Development Environment)**: A software application (e.g., Visual Studio) that provides comprehensive facilities for coding, debugging, and testing in one interface.

### Core Concepts (Q&A Format)
- Q: What are the three pillars of object-oriented programming supported by VB.NET?
- A: Encapsulation (hiding internal data), inheritance (deriving new classes from existing ones), and polymorphism (objects taking multiple forms through method overriding).

- Q: What is the difference between Option Strict and Option Explicit in VB.NET?
- A: Option Explicit requires all variables to be declared before use. Option Strict additionally disallows implicit narrowing type conversions and late binding, enforcing stricter type safety.

- Q: How does VB.NET differ from the original Visual Basic (VB6)?
- A: VB.NET is fully object-oriented, runs on the .NET CLR, supports structured exception handling (Try/Catch), inheritance, and multithreading -- whereas VB6 was component-based and ran on the COM runtime.

- Q: What is the role of the CLR in VB.NET program execution?
- A: The CLR compiles VB.NET code into Intermediate Language (IL), then uses Just-In-Time (JIT) compilation to convert IL to native machine code at runtime. It also manages memory through garbage collection.

- Q: What makes VB.NET suitable for Rapid Application Development?
- A: Visual Studio provides drag-and-drop form designers, built-in controls, IntelliSense code completion, and visual data binding tools that speed up UI and application creation.

- Q: What are the primary VB.NET data types?
- A: Integer, Double, String, Boolean, Decimal, Date, Char, Long, Single, and Object. Each defines the size and type of data a variable can hold.

- Q: What is a global variable vs. a local variable in VB.NET?
- A: A global (module-level) variable is declared at the class/module level and accessible to all procedures in that module. A local variable is declared inside a procedure and only accessible within that procedure.

### Important Facts & Figures
- VB.NET was first released in 2002 as part of the .NET Framework 1.0.
- In VB.NET, everything is an object, including primitive types like Integer and String (they inherit from System.Object).
- VB.NET uses the Dim keyword to declare variables (e.g., Dim count As Integer = 0).
- The Sub keyword defines a procedure that does not return a value; Function defines one that does.
- VB.NET supports structured exception handling with Try...Catch...Finally blocks, replacing VB6's On Error GoTo.
- VB.NET applications compile to MSIL (Microsoft Intermediate Language) before being JIT-compiled to native code.
- VB.NET can target Windows, Linux, and macOS through .NET Core and .NET 5+.

### Common Exam Questions
- Q: What is the output of: Dim x As Integer = 5.9 with Option Strict On?
- A: A compile-time error, because Option Strict disallows implicit narrowing conversions from Double to Integer.

- Q: Explain the difference between ByVal and ByRef parameter passing.
- A: ByVal passes a copy of the variable (changes inside the procedure do not affect the original). ByRef passes a reference to the original variable (changes inside the procedure modify the original).

- Q: What keyword is used to create a new instance of a class in VB.NET?
- A: The New keyword (e.g., Dim obj As New ClassName()).

- Q: Name two benefits of using the .NET Framework class library in VB.NET development.
- A: Access to thousands of pre-built classes for common tasks (file I/O, database access, networking, XML processing) and cross-language interoperability with other .NET languages like C#.

---

## Business Applications

### Key Terms & Definitions
- **Windows Forms (WinForms)**: A .NET GUI class library for building desktop applications with visual controls like buttons, text boxes, labels, and data grids.
- **ADO.NET**: The .NET data access technology that provides classes for connecting to databases, executing queries, and managing data in disconnected datasets.
- **CRUD Operations**: The four basic database operations -- Create, Read, Update, Delete -- that form the foundation of most business application data management.
- **DataSet**: An in-memory representation of data in ADO.NET that can hold multiple DataTables and their relationships, enabling disconnected data access.
- **DataAdapter**: An ADO.NET component that serves as a bridge between a DataSet and a data source, handling data retrieval (Fill) and updates (Update).
- **SqlConnection**: An ADO.NET object that establishes and manages a connection to a SQL Server database.
- **SqlCommand**: An ADO.NET object used to execute SQL statements or stored procedures against a database.
- **Data Binding**: The process of connecting UI controls directly to a data source so that changes in one are automatically reflected in the other.
- **Line-of-Business (LOB) Application**: Enterprise software that manages core business workflows such as inventory tracking, invoicing, and CRM.
- **COM Interop**: A .NET mechanism that allows VB.NET applications to interact with COM-based applications like Microsoft Office (Excel, Word, Outlook).
- **Connection String**: A text string containing the parameters (server name, database, credentials) needed to establish a database connection.

### Core Concepts (Q&A Format)
- Q: What is the typical architecture of a VB.NET database-driven business application?
- A: A three-tier architecture: Presentation Layer (WinForms UI), Business Logic Layer (validation and rules), and Data Access Layer (ADO.NET communicating with the database).

- Q: What is the difference between a connected and disconnected data access model in ADO.NET?
- A: Connected model uses SqlDataReader for fast, forward-only, read-only access while maintaining an open connection. Disconnected model uses DataSet/DataAdapter to load data into memory, close the connection, work with data offline, then reconnect to save changes.

- Q: How does a DataAdapter work in ADO.NET?
- A: The DataAdapter uses a SqlConnection and SqlCommand to execute a SELECT query, fills a DataSet with the results, and later can push changes from the DataSet back to the database using INSERT, UPDATE, and DELETE commands.

- Q: What types of business applications can be built with VB.NET?
- A: Windows Forms desktop apps, ASP.NET web applications, console apps for batch processing, Windows Services for background tasks, and Office automation tools.

- Q: What is data binding in Windows Forms?
- A: Data binding links a control's property (e.g., a TextBox's Text) to a data source (e.g., a DataTable column), so the control automatically displays and updates data without manual coding.

- Q: Why is VB.NET popular for enterprise LOB applications?
- A: Its RAD tools, English-like syntax, strong database connectivity via ADO.NET, and integration with Microsoft ecosystems make it efficient for building and maintaining business-critical applications.

### Important Facts & Figures
- ADO.NET replaced ADO (ActiveX Data Objects) as the primary data access technology in .NET.
- The four main ADO.NET data providers are: SQL Server, OLE DB, ODBC, and Oracle.
- Windows Forms was introduced with .NET Framework 1.0 and remains widely used for internal enterprise tools.
- A SqlDataReader is up to 10x faster than a DataSet for read-only forward data access because it maintains a direct connection.
- VB.NET can interact with Excel, Word, and Outlook through COM Interop for report generation and email automation.
- The connection string typically includes: Data Source (server), Initial Catalog (database), and authentication parameters.
- ASP.NET Web Forms allows VB.NET developers to build web-based business apps using a similar event-driven model to WinForms.

### Common Exam Questions
- Q: Write the basic ADO.NET steps to retrieve data from a SQL Server database.
- A: (1) Create a SqlConnection with a connection string, (2) Create a SqlCommand with a SQL query, (3) Open the connection, (4) Execute the command using ExecuteReader or Fill a DataSet via DataAdapter, (5) Process results, (6) Close the connection.

- Q: What is the difference between ExecuteReader, ExecuteScalar, and ExecuteNonQuery?
- A: ExecuteReader returns a DataReader for multiple rows. ExecuteScalar returns the first column of the first row (useful for COUNT, SUM). ExecuteNonQuery returns the number of rows affected (used for INSERT, UPDATE, DELETE).

- Q: Name three common Windows Forms controls used in business applications.
- A: DataGridView (tabular data display), TextBox (user input), and ComboBox (dropdown selection lists).

- Q: What is a connection string and why is it important?
- A: A connection string is a formatted text string containing parameters (server, database, authentication) required to establish a database connection. It is critical because incorrect parameters prevent the application from accessing its data source.

---

## Program Debugging

### Key Terms & Definitions
- **Bug**: An error or defect in software that causes incorrect or unexpected behavior.
- **Debugging**: The systematic process of identifying, isolating, and fixing bugs in software code.
- **Breakpoint**: A marker set on a line of code that pauses program execution at that point, allowing inspection of the program state.
- **Conditional Breakpoint**: A breakpoint that only pauses execution when a specified condition is true (e.g., counter > 100).
- **Step Over (F10)**: A debugging command that executes the current line and moves to the next, without entering called functions.
- **Step Into (F11)**: A debugging command that enters a called subroutine or function to debug its internal execution line by line.
- **Step Out (Shift+F11)**: A debugging command that completes execution of the current function and returns to the calling code.
- **Watch Window**: A debugging tool that allows developers to monitor specific variables and expressions, updating their values as code executes.
- **Locals Window**: A debugging window that automatically displays all variables in the current scope with their names, values, and data types.
- **Autos Window**: A debugging window that shows variables used on the current line and the preceding line of execution.
- **Call Stack**: A display showing the sequence of procedure calls that led to the current point of execution, helping trace program flow.
- **Immediate Window**: An interactive console during debugging that allows evaluating expressions, executing statements, and modifying variable values on the fly.

### Core Concepts (Q&A Format)
- Q: What is the difference between Step Over, Step Into, and Step Out?
- A: Step Over (F10) executes a function call as a single step. Step Into (F11) enters the function to debug it line by line. Step Out (Shift+F11) finishes the current function and returns to the caller.

- Q: How do you set a breakpoint in Visual Studio?
- A: Click in the left margin (gutter) of the code editor next to the desired line, or place the cursor on the line and press F9. A red dot appears indicating the breakpoint.

- Q: What is the difference between the Watch window and the Locals window?
- A: The Watch window shows only variables and expressions the developer manually adds for monitoring. The Locals window automatically displays all variables in the current scope.

- Q: When would you use a conditional breakpoint instead of a regular breakpoint?
- A: When you want to pause execution only when a specific condition is met (e.g., inside a loop that runs 1000 times, break only when i = 999), avoiding the need to manually continue through irrelevant iterations.

- Q: What is the purpose of the Immediate Window?
- A: It allows developers to evaluate expressions, test code snippets, change variable values, and call functions during a paused debugging session without modifying source code.

- Q: How do Debug.Write and Trace.Write differ?
- A: Debug.Write outputs only in Debug build configuration and is stripped from Release builds. Trace.Write outputs in both Debug and Release builds, making it useful for production diagnostics.

- Q: What is a NullReferenceException and how do you debug it?
- A: It occurs when code attempts to access a member of an object that is Nothing (null). Debug by setting a breakpoint before the error line, inspecting which variable is Nothing using the Watch or Locals window, then tracing back to find why it was not initialized.

### Important Facts & Figures
- The term "bug" in computing is popularly attributed to Grace Hopper, who found an actual moth in a computer relay in 1947.
- Visual Studio provides DataTips -- hover over a variable during debugging to see its current value in a tooltip.
- Tracepoints are a variant of breakpoints that log messages to the Output window without pausing execution.
- The Debug class resides in the System.Diagnostics namespace.
- Edit and Continue allows modifying code during a debugging session without restarting the application (with some limitations).
- The Exception Settings window in Visual Studio lets you configure the debugger to break on specific exception types, even if they are handled.
- Run to Cursor (Ctrl+F10) runs the program until it reaches the line where the cursor is placed, acting as a temporary breakpoint.

### Common Exam Questions
- Q: A loop is producing incorrect results. Describe the debugging steps you would take.
- A: Set a breakpoint at the start of the loop. Use Step Over (F10) to execute each iteration. Add the loop counter and key variables to the Watch window. Observe when values deviate from expected behavior to identify the logic error.

- Q: What is the keyboard shortcut to start debugging in Visual Studio?
- A: F5 starts debugging. Ctrl+F5 runs without debugging. F10 starts with Step Over. F11 starts with Step Into.

- Q: Explain the difference between a syntax error, a runtime error, and a logic error.
- A: Syntax errors violate language rules and are caught at compile time. Runtime errors occur during execution (e.g., division by zero, file not found). Logic errors produce incorrect output but no error messages, making them the hardest to find.

- Q: What is the Call Stack and when is it useful?
- A: The Call Stack shows the chain of method calls leading to the current execution point. It is especially useful for tracing how execution reached a particular function, diagnosing unexpected code paths, and debugging recursive functions.

---

## Testing

### Key Terms & Definitions
- **Software Testing**: The process of evaluating a program to verify it behaves as expected and meets specified requirements.
- **Unit Testing**: Testing individual methods, functions, or classes in isolation to verify each unit produces correct output for given inputs.
- **Integration Testing**: Testing the interaction between combined modules or components to verify they work correctly together.
- **Regression Testing**: Re-running existing test suites after code changes to ensure new modifications have not broken previously working functionality.
- **Test-Driven Development (TDD)**: A development methodology where failing tests are written before the production code, following a Red-Green-Refactor cycle.
- **Boundary Testing**: Testing input values at the edges of valid ranges (minimum, maximum, just inside, just outside) where bugs are most likely.
- **Test Case**: A set of conditions or inputs and expected results used to determine whether a software feature works correctly.
- **Test Suite**: A collection of test cases grouped together for organized execution.
- **Assertion**: A statement in a test that checks whether a condition is true; if false, the test fails (e.g., Assert.AreEqual(expected, actual)).
- **Code Coverage**: A metric measuring the percentage of source code exercised by tests, indicating how thoroughly the code has been tested.
- **Mock Object**: A simulated object that mimics the behavior of a real dependency (e.g., a database), allowing unit tests to run in isolation.
- **Test Pyramid**: A testing strategy recommending many fast unit tests (70%), fewer integration tests (20%), and limited end-to-end tests (10%).

### Core Concepts (Q&A Format)
- Q: What is the Red-Green-Refactor cycle in TDD?
- A: Red: Write a failing test for desired functionality. Green: Write the minimum code to make the test pass. Refactor: Clean up the code while keeping all tests passing.

- Q: What is the difference between unit testing and integration testing?
- A: Unit testing tests individual functions/methods in isolation using mocks for dependencies. Integration testing tests how multiple components work together with real or near-real dependencies.

- Q: Why is boundary testing important?
- A: Bugs most frequently occur at input boundaries (e.g., off-by-one errors). Testing at minimum, maximum, and edge values catches defects that normal-range testing misses.

- Q: What are the three major unit testing frameworks for VB.NET?
- A: MSTest (Microsoft's built-in framework), NUnit (open-source, widely used), and xUnit (modern, extensible, used by .NET Core team).

- Q: What is the purpose of regression testing?
- A: To verify that recent code changes (bug fixes, new features, refactoring) have not introduced new defects in existing, previously working functionality.

- Q: What is a stub vs. a mock in testing?
- A: A stub provides predefined responses to method calls during testing (passive). A mock additionally verifies that specific methods were called with expected parameters (active verification).

- Q: Describe top-down vs. bottom-up integration testing.
- A: Top-down starts testing from higher-level modules using stubs for unfinished lower modules. Bottom-up starts with foundational modules using drivers for upper modules. Sandwich (hybrid) combines both approaches.

### Important Facts & Figures
- The testing pyramid recommends: ~70% unit tests, ~20% integration tests, ~10% end-to-end/UI tests.
- Unit tests should run in milliseconds; integration tests in seconds; end-to-end tests in minutes.
- TDD was popularized by Kent Beck as part of Extreme Programming (XP) in the late 1990s.
- Code coverage of 80% is generally considered a good target; 100% coverage does not guarantee bug-free code.
- The [TestMethod] attribute marks a method as a test in MSTest; [Test] in NUnit; [Fact] in xUnit.
- The Arrange-Act-Assert (AAA) pattern is the standard structure for writing unit tests: set up inputs, execute the code, verify results.
- Continuous Integration (CI) servers automatically run test suites on every code commit.

### Common Exam Questions
- Q: Write a simple unit test structure using the AAA pattern.
- A: Arrange: Set up test data and expected result. Act: Call the method being tested. Assert: Compare actual result with expected result using Assert.AreEqual().

- Q: What is the difference between black-box and white-box testing?
- A: Black-box testing evaluates functionality without knowledge of internal code structure (testing inputs/outputs). White-box testing examines internal logic, paths, and code structure.

- Q: Why should unit tests be independent of each other?
- A: So that the failure of one test does not cause other tests to fail, tests can run in any order, and parallel test execution is possible.

- Q: A developer fixed a bug in the payment calculation module. What type of testing should be performed next, and why?
- A: Regression testing, to ensure the fix did not break other parts of the payment module or related functionality that depended on the original behavior.

---

## Documentation

### Key Terms & Definitions
- **Software Documentation**: Written materials that explain how code works, why design decisions were made, and how to use or maintain the software.
- **Inline Comment**: A comment placed within code using the apostrophe (') in VB.NET to explain specific lines or sections.
- **XML Documentation Comment**: A structured comment in VB.NET starting with triple apostrophes (''') that describes classes, methods, and parameters and can be auto-processed into API documentation.
- **Self-Documenting Code**: Code written with descriptive variable names, clear function names, and logical structure that communicates its purpose without excessive comments.
- **README**: A project-level document providing a concise description, setup instructions, dependencies, and usage examples for new developers.
- **API Documentation**: Reference material describing the public interfaces (classes, methods, parameters, return types) of a software library or service.
- **Changelog**: A document recording all notable changes made to a project, organized by version and date.
- **Code Comment**: An annotation in source code that is ignored by the compiler, intended to explain logic, document assumptions, or note workarounds.
- **Sandcastle**: A Microsoft documentation generation tool for .NET that creates help files and documentation websites from XML documentation comments.
- **GhostDoc**: A Visual Studio extension that automatically generates XML documentation comments for methods and properties based on their names and parameters.
- **Technical Debt**: The implied cost of future rework caused by choosing quick solutions over well-documented, maintainable approaches.

### Core Concepts (Q&A Format)
- Q: What is the difference between inline comments and XML documentation comments in VB.NET?
- A: Inline comments (') are freeform explanations for developers reading the code. XML documentation comments (''') follow a structured format with tags like <summary>, <param>, and <returns>, and can be compiled into formal API documentation.

- Q: What should comments explain: the "what" or the "why"?
- A: Comments should primarily explain the "why" -- the reasoning behind non-obvious decisions, edge case handling, and workarounds. The "what" should be communicated by writing self-documenting code with clear names.

- Q: What are the key XML documentation tags in VB.NET?
- A: <summary> (describes a class/method), <param name="x"> (describes a parameter), <returns> (describes the return value), <remarks> (additional details), <example> (usage example), and <exception> (documents thrown exceptions).

- Q: Why is self-documenting code important?
- A: It reduces the need for external documentation, makes the codebase more readable and maintainable, and ensures that the code itself serves as the primary source of truth since comments can become outdated.

- Q: When should documentation be updated?
- A: Documentation should be updated in the same changeset as the code modification. Keeping docs in sync with code prevents outdated, misleading information.

- Q: What are the risks of poor documentation?
- A: Increased onboarding time for new developers, higher maintenance costs, more bugs due to misunderstood code logic, and difficulty in auditing or extending the system.

### Important Facts & Figures
- XML documentation comments in VB.NET use triple apostrophes ('''), while C# uses triple slashes (///).
- Visual Studio can generate a skeleton XML comment automatically when you type ''' above a method.
- The DRY principle (Don't Repeat Yourself) applies to documentation: avoid duplicating information that the code already makes clear.
- Good documentation includes four levels: inline code comments, API reference docs, architectural/design docs, and end-user guides.
- Studies show that developers spend approximately 58% of their time understanding existing code, making documentation critical for productivity.
- Comments that merely restate what code does (e.g., ' Increment i by 1 above i += 1) are considered anti-patterns.
- Documentation tools like Sandcastle can output documentation in HTML, CHM (compiled help), and Microsoft Help Viewer formats.

### Common Exam Questions
- Q: Write an XML documentation comment for a VB.NET function that calculates sales tax.
- A: ''' <summary>Calculates the sales tax for a given amount.</summary> ''' <param name="amount">The purchase amount before tax.</param> ''' <param name="rate">The tax rate as a decimal (e.g., 0.07 for 7%).</param> ''' <returns>The calculated tax amount as a Decimal.</returns>

- Q: Give an example of a bad comment and explain why it is bad.
- A: ' Set x to 5 above the line x = 5. This is bad because it merely restates what the code already clearly shows. A better comment would explain why x is set to 5 (e.g., ' Default tax category per IRS regulation).

- Q: What is the difference between code documentation and user documentation?
- A: Code documentation is written for developers and explains how the code works internally (comments, API docs). User documentation is written for end users and explains how to use the software (manuals, help files, tutorials).

- Q: Name two tools that can generate documentation from VB.NET XML comments.
- A: Sandcastle (creates help files and HTML documentation) and GhostDoc (auto-generates XML comments and can export documentation).
