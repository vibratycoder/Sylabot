# ISA 341: Database Management Systems Principles - Flashcard Reference Bank

---

## Relational Database Design

### Key Terms & Definitions
- **Relation**: A two-dimensional table consisting of rows (tuples) and columns (attributes) that stores data about a single entity type
- **Tuple**: A single row in a relation representing one record or instance of an entity
- **Attribute**: A single column in a relation representing a property or characteristic of the entity
- **Primary Key**: A column (or set of columns) that uniquely identifies every row in a table; cannot be NULL
- **Foreign Key**: A column that references the primary key of another table, establishing a relationship and enforcing referential integrity
- **Candidate Key**: Any column or combination of columns that could serve as a primary key (unique and non-null); only one is chosen as the primary key
- **Composite Key**: A primary key made up of two or more columns together, used when no single column can uniquely identify a row
- **Surrogate Key**: A system-generated artificial key (e.g., auto-increment integer) with no business meaning, used purely for unique identification
- **Referential Integrity**: A constraint ensuring that every foreign key value must match an existing primary key value in the referenced table, or be NULL
- **Domain Constraint**: A rule that restricts the set of allowable values for an attribute (e.g., data type, range, format)
- **Entity Integrity**: A rule stating that no primary key column can contain a NULL value
- **Junction Table**: An intermediary table used to resolve a many-to-many relationship by holding foreign keys to both related tables

### Core Concepts (Q&A Format)
- Q: What is the difference between a candidate key and a primary key?
- A: A candidate key is any column or combination that can uniquely identify rows; the primary key is the one candidate key selected for actual use in the table.

- Q: How is a many-to-many (M:N) relationship implemented in a relational database?
- A: By creating a junction (associative) table that contains foreign keys referencing the primary keys of both related tables, decomposing the M:N into two one-to-many relationships.

- Q: What is an orphaned record?
- A: A record whose foreign key value does not match any primary key in the referenced table, violating referential integrity.

- Q: Why is data redundancy a problem in database design?
- A: Redundancy wastes storage, creates inconsistency when duplicate data is updated in one place but not others, and leads to insertion, update, and deletion anomalies.

- Q: What are the three fundamental relational operations?
- A: SELECT (filter rows), PROJECT (choose columns), and JOIN (combine tables based on related columns).

- Q: What is the difference between a one-to-one and a one-to-many relationship?
- A: In 1:1, each row in Table A relates to at most one row in Table B and vice versa. In 1:N, one row in Table A can relate to many rows in Table B, but each row in Table B relates to only one row in Table A.

- Q: Who created the relational model and when?
- A: E.F. Codd introduced the relational model in 1970 while working at IBM.

### Important Facts & Figures
- The relational model was proposed by E.F. Codd in his 1970 paper "A Relational Model of Data for Large Shared Data Banks"
- One-to-many (1:N) is the most common relationship type in relational databases
- A table must have exactly one primary key, but can have multiple candidate keys and multiple foreign keys
- Entity integrity + referential integrity + domain constraints = the three core integrity rules of the relational model
- Logical and physical data independence means schema changes do not require application code changes
- The five core relational algebra operations are: SELECT, PROJECT, UNION, SET DIFFERENCE, and CARTESIAN PRODUCT
- SQL is the standard language for interacting with relational databases, based on relational algebra and relational calculus

### Common Exam Questions
- Q: A table has columns (StudentID, CourseID, Grade). What is the primary key?
- A: The composite key (StudentID, CourseID), since neither alone can uniquely identify each enrollment record.

- Q: If you delete a Department record and Employee records reference that Department via a foreign key, what happens?
- A: The DBMS will reject the deletion (or cascade it, depending on the ON DELETE rule) to maintain referential integrity.

- Q: Name three types of data integrity constraints in the relational model.
- A: Domain constraints (valid values), entity integrity (no null primary keys), and referential integrity (foreign keys match existing primary keys).

- Q: What is the difference between a surrogate key and a natural key?
- A: A surrogate key is system-generated with no business meaning (e.g., auto-increment ID); a natural key uses real-world data (e.g., SSN, email) that has inherent meaning.

---

## Normalization

### Key Terms & Definitions
- **Normalization**: The systematic process of organizing database tables to minimize redundancy and prevent insertion, update, and deletion anomalies
- **Functional Dependency**: A relationship where the value of one attribute (determinant) uniquely determines the value of another attribute (e.g., StudentID -> StudentName)
- **Partial Dependency**: When a non-key attribute depends on only part of a composite primary key, violating 2NF
- **Transitive Dependency**: When a non-key attribute depends on another non-key attribute rather than directly on the primary key, violating 3NF
- **First Normal Form (1NF)**: Every column contains only atomic (indivisible) values, each row is unique, and there are no repeating groups
- **Second Normal Form (2NF)**: In 1NF and every non-key attribute is fully functionally dependent on the entire primary key (no partial dependencies)
- **Third Normal Form (3NF)**: In 2NF and no non-key attribute depends on another non-key attribute (no transitive dependencies)
- **Boyce-Codd Normal Form (BCNF)**: Every non-trivial functional dependency has a superkey as its determinant; stricter than 3NF
- **Insertion Anomaly**: Inability to add data because other required (but unrelated) data is missing
- **Update Anomaly**: Inconsistency caused by updating a fact in one row but not in duplicate rows
- **Deletion Anomaly**: Unintended loss of data when deleting a row removes the only record of unrelated information
- **Denormalization**: Intentionally introducing redundancy back into a schema to improve read performance for reporting or analytics workloads

### Core Concepts (Q&A Format)
- Q: What problem does normalization solve?
- A: It eliminates data redundancy and prevents insertion, update, and deletion anomalies by organizing data into well-structured tables.

- Q: If a table has a single-column primary key, can it violate 2NF?
- A: No. Partial dependencies only occur with composite keys, so a single-column primary key table in 1NF is automatically in 2NF.

- Q: Give an example of a transitive dependency.
- A: In a table with (StudentID, AdvisorID, AdvisorOffice), AdvisorOffice depends on AdvisorID (a non-key attribute), not directly on StudentID.

- Q: What is the relationship between BCNF and 3NF?
- A: BCNF is strictly stronger than 3NF. Every table in BCNF is in 3NF, but not every 3NF table is in BCNF.

- Q: When is denormalization appropriate?
- A: In read-heavy environments like data warehouses and reporting systems where query speed is more important than eliminating redundancy.

- Q: How do you decompose a table from 1NF to 2NF?
- A: Identify partial dependencies on the composite key and move the partially dependent attributes into a separate table with the part of the key they depend on.

- Q: What is a determinant in a functional dependency?
- A: The attribute(s) on the left side of the arrow that uniquely determine the attribute(s) on the right side (e.g., in A -> B, A is the determinant).

### Important Facts & Figures
- Normalization was introduced by E.F. Codd in 1970 alongside the relational model
- The most common target for transactional databases is 3NF (Third Normal Form)
- There are six recognized normal forms: 1NF, 2NF, 3NF, BCNF, 4NF, and 5NF
- A common mnemonic for 3NF: "Every non-key attribute must depend on the key, the whole key, and nothing but the key"
- BCNF handles the edge case where a non-key attribute is a determinant of part of the primary key
- Denormalization is standard practice in OLAP (Online Analytical Processing) and star/snowflake schema data warehouses
- Splitting a flat spreadsheet into Customers, Products, and OrderDetails is a classic normalization example

### Common Exam Questions
- Q: A table (OrderID, ProductID, ProductName, Quantity) has composite key (OrderID, ProductID). ProductName depends only on ProductID. What normal form is violated?
- A: 2NF is violated because ProductName is partially dependent on only ProductID, not the full composite key.

- Q: A table (EmpID, DeptID, DeptName) where DeptName depends on DeptID. What normal form is violated and why?
- A: 3NF is violated because DeptName transitively depends on EmpID through DeptID (a non-key attribute).

- Q: What is the difference between an update anomaly and a deletion anomaly?
- A: Update anomaly: changing data in one row but not its duplicates causes inconsistency. Deletion anomaly: removing a row causes unintended loss of unrelated information.

- Q: Normalize the following into 3NF: Student(StudentID, Name, AdvisorID, AdvisorName, AdvisorPhone).
- A: Split into Student(StudentID, Name, AdvisorID) and Advisor(AdvisorID, AdvisorName, AdvisorPhone) to remove the transitive dependency.

---

## SQL

### Key Terms & Definitions
- **SQL (Structured Query Language)**: The standard declarative language for defining, querying, and managing relational databases, standardized by ANSI/ISO
- **DDL (Data Definition Language)**: SQL commands that define or modify database structure -- CREATE, ALTER, DROP, TRUNCATE
- **DML (Data Manipulation Language)**: SQL commands that manipulate data -- INSERT, UPDATE, DELETE (and SELECT in some classifications)
- **DQL (Data Query Language)**: The SELECT statement used to retrieve data from one or more tables
- **DCL (Data Control Language)**: SQL commands that control access permissions -- GRANT and REVOKE
- **TCL (Transaction Control Language)**: SQL commands that manage transactions -- COMMIT, ROLLBACK, SAVEPOINT
- **JOIN**: An operation that combines rows from two or more tables based on a related column (INNER, LEFT, RIGHT, FULL OUTER, CROSS)
- **Subquery**: A query nested inside another query, used for filtering, comparison, or generating derived tables
- **Aggregate Function**: A function that performs a calculation on a set of values and returns a single value -- COUNT, SUM, AVG, MIN, MAX
- **GROUP BY**: A clause that groups rows sharing a common value so aggregate functions can be applied to each group
- **HAVING**: A clause that filters groups created by GROUP BY (like WHERE but for aggregated results)
- **Common Table Expression (CTE)**: A named temporary result set defined with the WITH keyword that exists only for the duration of a single query

### Core Concepts (Q&A Format)
- Q: What is the difference between WHERE and HAVING?
- A: WHERE filters individual rows before grouping; HAVING filters groups after GROUP BY and aggregation have been applied.

- Q: What is the difference between DROP and TRUNCATE?
- A: DROP removes the entire table structure and data permanently. TRUNCATE removes all rows but preserves the table structure.

- Q: What is the difference between INNER JOIN and LEFT JOIN?
- A: INNER JOIN returns only rows with matching values in both tables. LEFT JOIN returns all rows from the left table plus matched rows from the right (NULLs where no match).

- Q: What does GRANT do?
- A: GRANT assigns specific privileges (SELECT, INSERT, UPDATE, etc.) on database objects to users or roles.

- Q: What is a transaction in SQL?
- A: A group of one or more SQL statements treated as a single atomic unit -- either all succeed (COMMIT) or all are undone (ROLLBACK).

- Q: When would you use a CTE over a subquery?
- A: CTEs improve readability for complex queries, can be referenced multiple times in the same query, and support recursive queries.

- Q: What does the DISTINCT keyword do?
- A: It removes duplicate rows from the result set of a SELECT query.

- Q: What is the order of execution of a SQL SELECT statement?
- A: FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY -> LIMIT.

### Important Facts & Figures
- SQL was developed in the 1970s at IBM by Donald Chamberlin and Raymond Boyce
- SQL was first standardized by ANSI in 1986 and ISO in 1987
- The five SQL command categories are DDL, DML, DQL, DCL, and TCL
- COMMIT makes transaction changes permanent; ROLLBACK undoes them; SAVEPOINT creates a rollback point within a transaction
- NULL represents unknown or missing data and requires IS NULL / IS NOT NULL for comparison (not = or !=)
- An index speeds up SELECT queries but slows down INSERT/UPDATE/DELETE operations due to index maintenance overhead
- A VIEW is a virtual table based on a stored SELECT statement that does not store data itself
- The wildcard % matches zero or more characters in a LIKE clause; _ matches exactly one character

### Common Exam Questions
- Q: Write a query to find the average salary by department for departments with more than 5 employees.
- A: SELECT DeptID, AVG(Salary) FROM Employees GROUP BY DeptID HAVING COUNT(*) > 5;

- Q: What is the result of a CROSS JOIN between a table with 3 rows and a table with 4 rows?
- A: 12 rows (the Cartesian product: 3 x 4).

- Q: Classify each command: CREATE TABLE, INSERT INTO, GRANT, COMMIT, SELECT.
- A: CREATE TABLE = DDL, INSERT INTO = DML, GRANT = DCL, COMMIT = TCL, SELECT = DQL.

- Q: What happens if you run DELETE FROM Employees without a WHERE clause?
- A: All rows in the Employees table are deleted (but the table structure remains).

- Q: What is the difference between DELETE and TRUNCATE?
- A: DELETE removes rows one by one and can use WHERE to filter; it is logged and can be rolled back. TRUNCATE removes all rows at once, is faster, and typically cannot be rolled back.

---

## ER Diagrams

### Key Terms & Definitions
- **Entity**: A real-world object or concept represented as a rectangle in an ER diagram (e.g., Student, Course, Employee)
- **Entity Set**: The collection of all instances of a particular entity type
- **Weak Entity**: An entity that cannot be uniquely identified by its own attributes alone and depends on a related "owner" entity; shown as a double-bordered rectangle
- **Attribute**: A property describing an entity, shown as an oval (simple, composite, derived, or multivalued)
- **Key Attribute**: An attribute that uniquely identifies each entity instance, shown underlined in the ER diagram (becomes the primary key)
- **Composite Attribute**: An attribute that can be divided into smaller sub-attributes (e.g., FullName -> FirstName, LastName)
- **Derived Attribute**: An attribute whose value is calculated from other attributes (e.g., Age derived from DateOfBirth), shown as a dashed oval
- **Multivalued Attribute**: An attribute that can hold multiple values for a single entity (e.g., PhoneNumbers), shown as a double oval
- **Relationship**: An association between two or more entities, depicted as a diamond shape (e.g., "Enrolls" connects Student and Course)
- **Cardinality Ratio**: Specifies the number of instances of one entity that can be associated with instances of another: 1:1, 1:N, or M:N
- **Total Participation**: Every instance of the entity must participate in the relationship, shown as a double line
- **Partial Participation**: Not every instance must participate in the relationship, shown as a single line

### Core Concepts (Q&A Format)
- Q: Who introduced the ER model and when?
- A: Peter Chen introduced the Entity-Relationship model in 1976.

- Q: What is the difference between total and partial participation?
- A: Total participation (double line) means every entity instance must be in the relationship. Partial participation (single line) means participation is optional.

- Q: How is a weak entity identified?
- A: Through a combination of its own partial key (discriminator) and the primary key of its owner entity, connected by an identifying relationship (double diamond).

- Q: What are the three levels of ER diagrams?
- A: Conceptual (high-level business entities), Logical (adds attributes and keys), and Physical (adds data types, indexes, platform-specific details).

- Q: How do cardinality and participation constraints differ?
- A: Cardinality defines the maximum number of relationship instances (1:1, 1:N, M:N). Participation defines whether each entity instance must participate (total) or may optionally participate (partial).

- Q: How is a multivalued attribute handled when converting an ER diagram to a relational schema?
- A: It is moved to a separate table with a foreign key back to the original entity's primary key.

### Important Facts & Figures
- The ER model was introduced by Peter Chen in 1976
- Standard ER symbols: rectangles (entities), diamonds (relationships), ovals (attributes), lines (connections)
- Weak entities use double-bordered rectangles and identifying relationships use double-bordered diamonds
- Cardinality ratios and participation constraints together are called structural constraints
- A relationship can have its own descriptive attributes (e.g., "Enrolls" may have a Grade attribute)
- Common tools for ER diagrams: ERDPlus, Lucidchart, draw.io, MySQL Workbench
- When converting M:N relationships to tables, a new junction table is always created
- Composite attributes are flattened into simple attributes during conversion to relational schema

### Common Exam Questions
- Q: An Employee must belong to exactly one Department, but a Department can have many Employees. Draw the participation and cardinality.
- A: Employee has total participation (double line) with cardinality N toward Department. Department has partial participation (single line) with cardinality 1 toward Employee. Relationship: 1:N.

- Q: When would you use a weak entity?
- A: When an entity cannot be uniquely identified without the primary key of another entity (e.g., Dependent cannot exist without Employee).

- Q: How do you convert a ternary (three-way) relationship to a relational schema?
- A: Create a new table whose primary key is a composite of the primary keys of all three participating entities, plus any relationship attributes.

- Q: A Student can enroll in many Courses, and a Course can have many Students. What cardinality is this and how is it implemented?
- A: M:N cardinality, implemented with a junction table (e.g., Enrollment) containing StudentID and CourseID as a composite primary key plus any attributes like Grade.

---

## Database Application Development

### Key Terms & Definitions
- **CRUD**: The four fundamental database operations -- Create (INSERT), Read (SELECT), Update (UPDATE), Delete (DELETE)
- **Stored Procedure**: A precompiled set of SQL statements stored on the database server that can be called by name, improving performance and security
- **Trigger**: A special stored procedure that automatically executes in response to specific database events (INSERT, UPDATE, DELETE on a table)
- **ACID Properties**: The four guarantees of reliable transaction processing -- Atomicity, Consistency, Isolation, Durability
- **Atomicity**: A transaction is all-or-nothing; either all operations succeed or none do
- **Consistency**: A transaction brings the database from one valid state to another, maintaining all defined rules and constraints
- **Isolation**: Concurrent transactions do not interfere with each other; each appears to execute in isolation
- **Durability**: Once a transaction is committed, its changes persist permanently even if the system crashes
- **Connection Pooling**: A technique that reuses a pool of pre-established database connections to reduce the overhead of creating new connections for each request
- **ORM (Object-Relational Mapping)**: A framework that maps database tables to programming language objects, allowing developers to interact with data without writing raw SQL
- **SQL Injection**: A security vulnerability where malicious SQL code is inserted into application inputs to manipulate the database
- **Parameterized Query**: A query using placeholders for input values that are bound at execution time, preventing SQL injection attacks

### Core Concepts (Q&A Format)
- Q: How do CRUD operations map to HTTP methods in REST APIs?
- A: Create = POST, Read = GET, Update = PUT/PATCH, Delete = DELETE.

- Q: What are the advantages of stored procedures over inline SQL?
- A: Precompiled for better performance, reduced network traffic, encapsulated business logic, and enhanced security by limiting direct table access.

- Q: How does connection pooling improve application performance?
- A: By reusing existing database connections instead of opening and closing new ones for each request, reducing connection overhead and improving response time.

- Q: What is the difference between optimistic and pessimistic locking?
- A: Optimistic locking checks for conflicts at commit time (using version numbers). Pessimistic locking acquires locks at read time, preventing other transactions from modifying the data until the lock is released.

- Q: How does a parameterized query prevent SQL injection?
- A: It separates SQL code from user input -- input values are treated as data parameters, not executable SQL, so malicious code cannot alter the query structure.

- Q: Name three popular ORM frameworks and their languages.
- A: Hibernate (Java), Entity Framework (.NET/C#), SQLAlchemy (Python).

- Q: What is the difference between a stored procedure and a function?
- A: A stored procedure can perform actions and may or may not return a value. A function must return a value and is typically used in expressions and SELECT statements.

### Important Facts & Figures
- CRUD maps to SQL: INSERT (Create), SELECT (Read), UPDATE (Update), DELETE (Delete)
- The ACID acronym was coined by Andreas Reuter and Theo Harder in 1983
- Common isolation levels (from least to most strict): Read Uncommitted, Read Committed, Repeatable Read, Serializable
- SQL injection is consistently ranked in the OWASP Top 10 web application security risks
- Three-tier architecture: Presentation Layer (UI) -> Application Layer (business logic) -> Data Layer (database)
- Connection pools typically maintain 5-20 connections for small apps, scaling to hundreds for enterprise systems
- ORMs trade some query performance for developer productivity and code maintainability
- Prepared statements (parameterized queries) are the primary defense against SQL injection

### Common Exam Questions
- Q: Explain why Atomicity is important with a real-world example.
- A: In a bank transfer, if $100 is debited from Account A but the system crashes before crediting Account B, atomicity ensures both operations are rolled back so no money is lost.

- Q: What isolation level allows dirty reads, and what does that mean?
- A: Read Uncommitted allows dirty reads -- reading data that another transaction has modified but not yet committed, risking seeing data that may be rolled back.

- Q: A web form takes a username and runs: SELECT * FROM Users WHERE name = '{input}'. What is the vulnerability and fix?
- A: SQL injection vulnerability. Fix: use parameterized queries (e.g., WHERE name = ?) so user input is never concatenated into SQL.

- Q: What are the four ACID properties? Define each in one sentence.
- A: Atomicity (all or nothing), Consistency (valid state to valid state), Isolation (concurrent transactions don't interfere), Durability (committed data survives crashes).

---

## Data Modeling

### Key Terms & Definitions
- **Data Model**: A visual and logical representation of data elements, their relationships, and the rules governing them within a system
- **Conceptual Data Model**: The highest-level, technology-independent model showing major business entities and their relationships without data types or constraints
- **Logical Data Model**: A detailed model defining tables, columns, keys, and relationships independent of any specific DBMS platform
- **Physical Data Model**: The implementation-ready design specifying exact data types, indexes, partitioning, storage engines, and platform-specific configurations
- **Forward Engineering**: The process of generating a physical database schema (DDL scripts) from a data model
- **Reverse Engineering**: The process of extracting a data model from an existing database, used to document legacy systems
- **Chen Notation**: An ER notation using rectangles (entities), diamonds (relationships), and ovals (attributes) with numeric cardinality labels
- **Crow's Foot Notation**: An ER notation using line endings shaped like a crow's foot (fork) for "many" and a single bar for "one," popular in professional tools
- **Cardinality**: The numerical relationship between entity instances (one-to-one, one-to-many, many-to-many)
- **Data Dictionary**: A centralized repository of metadata that describes the structure, meaning, and constraints of every data element
- **Data Lineage**: The documentation of data's origin, movement, and transformation as it flows through systems
- **Schema**: The overall logical structure of a database, including tables, columns, data types, relationships, and constraints

### Core Concepts (Q&A Format)
- Q: What are the three levels of data modeling and who uses each?
- A: Conceptual (business stakeholders), Logical (analysts and architects), Physical (database administrators and developers).

- Q: What is the key difference between Chen notation and Crow's Foot notation?
- A: Chen uses separate shapes (rectangles, diamonds, ovals) and numeric cardinality labels. Crow's Foot uses line endings (fork for many, bar for one) and is more compact, preferred in professional environments.

- Q: What is forward engineering in data modeling?
- A: Converting a data model into a physical database by generating SQL DDL statements (CREATE TABLE, etc.) from the model.

- Q: Why is reverse engineering useful?
- A: It extracts a visual data model from an existing database, which is essential for understanding, documenting, and modernizing legacy systems.

- Q: How does a conceptual model differ from a logical model?
- A: A conceptual model identifies entities and relationships at a high level (no columns or data types). A logical model adds specific attributes, primary/foreign keys, and normalization details.

- Q: What role does data modeling play in data governance?
- A: It documents data lineage, ownership, business rules, and metadata, ensuring consistency, quality, and regulatory compliance across the organization.

- Q: In Crow's Foot notation, how are minimum and maximum cardinality shown?
- A: Maximum: bar (|) for one, fork (<) for many. Minimum: bar (|) for mandatory (at least one), circle (O) for optional (zero allowed).

### Important Facts & Figures
- Chen notation was introduced by Peter Chen in 1976; Crow's Foot notation originated from a 1976 paper by Gordon Everest
- The three model levels proceed from abstract to concrete: Conceptual -> Logical -> Physical
- UML class diagrams are also used as a data modeling notation, especially in object-oriented environments
- A conceptual model typically has 10-20 entities for an enterprise system; a physical model may have hundreds of tables
- IDEF1X is another formal data modeling notation used in government and defense projects
- Popular data modeling tools: ERwin, PowerDesigner, Oracle SQL Developer Data Modeler, MySQL Workbench, Lucidchart
- A well-constructed logical model should be DBMS-independent -- it can be implemented on Oracle, SQL Server, PostgreSQL, or MySQL without changes
- Data modeling is typically performed during the requirements and design phases of the Software Development Life Cycle (SDLC)

### Common Exam Questions
- Q: List the three levels of data modeling in order from most abstract to most detailed.
- A: Conceptual -> Logical -> Physical.

- Q: You have a legacy Oracle database with no documentation. What data modeling technique would you use to understand it?
- A: Reverse engineering -- connect a modeling tool to the database and extract the schema into a visual data model.

- Q: In Crow's Foot notation, draw the symbol for a mandatory one-to-many relationship.
- A: The "one" side has a single bar (|) at each end (mandatory one). The "many" side has a bar and a crow's foot fork (|<) meaning mandatory many.

- Q: What is the purpose of a data dictionary?
- A: It serves as a centralized metadata repository describing every table, column, data type, constraint, and business rule in the database, enabling consistent understanding across teams.

- Q: A business stakeholder wants to see how Customers, Orders, and Products relate. Which model level do you present?
- A: A conceptual data model, which shows entities and relationships at a high level without technical details.
