# ISA 540: Data Management in the Age of AI - Flashcard Reference Bank

---

## Relational Databases

### Key Terms & Definitions
- **Relation**: A table in a relational database consisting of rows and columns
- **Tuple**: A single row (record) in a table representing one instance of an entity
- **Attribute**: A single column (field) in a table representing a property of the entity
- **Primary Key**: A column (or set of columns) that uniquely identifies each row in a table
- **Foreign Key**: A column that references the primary key of another table, establishing a relationship between them
- **Index**: A data structure that speeds up data retrieval by providing quick lookup paths to rows
- **Schema**: The formal definition of a database's structure, including tables, columns, types, and constraints
- **Constraint**: A rule enforced on data columns to maintain accuracy and integrity (e.g., NOT NULL, UNIQUE, CHECK)
- **Referential Integrity**: A property ensuring that foreign key values always point to existing primary key values
- **RDBMS**: Relational Database Management System -- software that manages relational databases (e.g., PostgreSQL, MySQL, Oracle)
- **Composite Key**: A primary key made up of two or more columns together

### Core Concepts (Q&A Format)
- Q: What are the four ACID properties and what does each guarantee?
- A: Atomicity (transactions are all-or-nothing), Consistency (database moves from one valid state to another), Isolation (concurrent transactions do not interfere with each other), Durability (committed data survives system failures).

- Q: What is normalization and why is it performed?
- A: Normalization is the process of organizing tables to reduce data redundancy and eliminate update, insert, and delete anomalies. It applies progressively stricter rules (normal forms) to table structures.

- Q: What is the difference between 1NF, 2NF, and 3NF?
- A: 1NF requires atomic (indivisible) values with no repeating groups. 2NF requires 1NF plus removal of partial dependencies on composite keys. 3NF requires 2NF plus removal of transitive dependencies (non-key columns depending on other non-key columns).

- Q: What is BCNF and how does it differ from 3NF?
- A: Boyce-Codd Normal Form (BCNF) requires that every determinant is a candidate key. It is stricter than 3NF and resolves certain anomalies that 3NF does not address when a table has multiple overlapping candidate keys.

- Q: When would you choose PostgreSQL over SQLite?
- A: PostgreSQL is a full-featured, multi-user server database suited for enterprise applications with concurrent access. SQLite is an embedded, file-based database suited for lightweight, single-user, or mobile applications.

- Q: What is a transaction in a relational database?
- A: A transaction is a logical unit of work consisting of one or more SQL operations that must either all succeed (commit) or all fail (rollback), ensuring data integrity.

- Q: Why are relational databases preferred for financial records and transactional systems?
- A: Their strong ACID compliance guarantees data integrity, consistency, and reliable audit trails, which are essential when accuracy and completeness of records are non-negotiable.

### Important Facts & Figures
- Edgar F. Codd published the relational model in 1970 while at IBM
- The relational model is based on mathematical set theory and first-order predicate logic
- PostgreSQL, MySQL, SQL Server, Oracle, and SQLite are the five most widely used relational databases
- ACID properties are the foundation of transaction management in all relational databases
- Normalization progresses through forms: 1NF, 2NF, 3NF, BCNF, 4NF, 5NF
- Relational databases use vertical scaling (bigger hardware) as the primary scaling strategy
- Indexes trade write performance for faster read performance
- A well-designed relational database can serve both OLTP and OLAP workloads with proper indexing

### Common Exam Questions
- Q: A table has columns (StudentID, CourseID, Instructor, Grade). StudentID + CourseID is the primary key. Instructor depends only on CourseID. What normal form violation exists?
- A: This violates 2NF because Instructor has a partial dependency on only part of the composite key (CourseID), not the full key.

- Q: Explain the difference between a primary key and a foreign key with an example.
- A: A primary key uniquely identifies rows in its own table (e.g., StudentID in Students). A foreign key is a column in another table that references that primary key to establish a relationship (e.g., StudentID in Enrollments references Students.StudentID).

- Q: What happens if the Durability property is violated?
- A: Committed transactions could be lost after a system crash, meaning data that was confirmed as saved could disappear, breaking trust in the database.

- Q: What is referential integrity and how is it enforced?
- A: Referential integrity ensures foreign keys always reference valid primary keys. It is enforced through foreign key constraints that prevent inserting orphan records or deleting referenced parent records.

---

## SQL

### Key Terms & Definitions
- **SELECT**: SQL statement used to retrieve (read) data from one or more tables
- **INSERT**: SQL statement used to add new rows into a table
- **UPDATE**: SQL statement used to modify existing rows in a table
- **DELETE**: SQL statement used to remove rows from a table
- **JOIN**: A clause that combines rows from two or more tables based on a related column (INNER, LEFT, RIGHT, FULL, CROSS)
- **WHERE**: A clause that filters rows based on specified conditions
- **GROUP BY**: A clause that groups rows sharing a value in specified columns, used with aggregate functions
- **HAVING**: A clause that filters groups created by GROUP BY (like WHERE, but for aggregated results)
- **Subquery**: A query nested inside another SQL statement, returning results used by the outer query
- **CTE (Common Table Expression)**: A named temporary result set defined with the WITH keyword, improving query readability
- **Window Function**: A function that performs calculations across a set of rows related to the current row without collapsing them (e.g., ROW_NUMBER, RANK, LAG, LEAD)
- **Aggregate Function**: A function that computes a single value from a set of rows (SUM, COUNT, AVG, MIN, MAX)

### Core Concepts (Q&A Format)
- Q: What is the difference between WHERE and HAVING?
- A: WHERE filters individual rows before grouping. HAVING filters groups after GROUP BY and aggregation have been applied.

- Q: What is the difference between INNER JOIN and LEFT JOIN?
- A: INNER JOIN returns only rows with matching values in both tables. LEFT JOIN returns all rows from the left table and matched rows from the right table (NULLs where no match exists).

- Q: What is a window function and how does it differ from an aggregate function?
- A: A window function performs calculations across a set of rows related to the current row but retains all individual rows in the output. An aggregate function collapses multiple rows into a single summary row.

- Q: What is a query execution plan and why is it important?
- A: A query execution plan (viewed with EXPLAIN) shows the steps the database engine will take to execute a query. It helps identify performance bottlenecks like full table scans, missing indexes, and inefficient joins.

- Q: What is the N+1 query problem?
- A: The N+1 problem occurs when code executes one query to fetch a list of N items, then executes N additional queries to fetch related data for each item, leading to poor performance. It is solved by using JOINs or batch fetching.

- Q: What does the DISTINCT keyword do?
- A: DISTINCT eliminates duplicate rows from the result set, returning only unique combinations of the selected columns.

- Q: Explain the order of SQL clause execution.
- A: FROM/JOIN (identify tables) -> WHERE (filter rows) -> GROUP BY (group rows) -> HAVING (filter groups) -> SELECT (choose columns) -> ORDER BY (sort results) -> LIMIT (restrict output count).

### Important Facts & Figures
- SQL was originally developed at IBM in the 1970s as SEQUEL (Structured English Query Language)
- SQL is an ISO/ANSI standard language, though vendors add proprietary extensions
- SQL is consistently the most requested skill in data analytics job postings
- The four CRUD operations map to: CREATE (INSERT), READ (SELECT), UPDATE (UPDATE), DELETE (DELETE)
- DDL (Data Definition Language): CREATE, ALTER, DROP; DML (Data Manipulation Language): SELECT, INSERT, UPDATE, DELETE; DCL (Data Control Language): GRANT, REVOKE
- Window functions were added in the SQL:2003 standard
- CTEs improve readability and allow recursive queries for hierarchical data
- Indexes can speed up SELECT queries by orders of magnitude but slow down INSERT/UPDATE/DELETE operations

### Common Exam Questions
- Q: Write a query to find the second-highest salary from an Employees table.
- A: `SELECT MAX(salary) FROM Employees WHERE salary < (SELECT MAX(salary) FROM Employees);` -- or using window functions: `SELECT salary FROM (SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) as rnk FROM Employees) t WHERE rnk = 2;`

- Q: What is the difference between DELETE and TRUNCATE?
- A: DELETE removes rows one by one, can use WHERE to filter, and is logged/rollbackable. TRUNCATE removes all rows at once, cannot use WHERE, is faster, and resets auto-increment counters.

- Q: What is the difference between UNION and UNION ALL?
- A: UNION combines result sets and removes duplicates. UNION ALL combines result sets and keeps all rows including duplicates, making it faster.

- Q: Given tables Orders(order_id, customer_id, amount) and Customers(customer_id, name), write a query to find the total spending per customer.
- A: `SELECT c.name, SUM(o.amount) AS total_spending FROM Customers c JOIN Orders o ON c.customer_id = o.customer_id GROUP BY c.name;`

- Q: What does the LAG window function do?
- A: LAG accesses a value from a previous row in the result set without a self-join. For example, `LAG(sales, 1) OVER (ORDER BY month)` returns the sales value from the prior month.

---

## NoSQL

### Key Terms & Definitions
- **NoSQL**: "Not Only SQL" -- a category of non-relational databases designed for flexible schemas, horizontal scalability, and specific workload patterns
- **Document Store**: A NoSQL database that stores data as JSON-like documents with nested fields (e.g., MongoDB)
- **Key-Value Store**: A NoSQL database that stores data as simple key-value pairs for ultra-fast lookups (e.g., Redis)
- **Wide-Column Store**: A NoSQL database that stores data in column families rather than rows, optimized for high write throughput (e.g., Cassandra)
- **Graph Database**: A NoSQL database that stores entities as nodes and relationships as edges, optimized for relationship queries (e.g., Neo4j)
- **CAP Theorem**: States that a distributed system can guarantee at most two of three properties: Consistency, Availability, and Partition Tolerance
- **Eventual Consistency**: A consistency model where replicas will converge to the same state given enough time, but reads may return stale data temporarily
- **Horizontal Scaling (Scale-Out)**: Adding more machines/nodes to a system rather than upgrading a single machine
- **Sharding**: Distributing data across multiple nodes by partitioning it based on a shard key
- **Schema-on-Read**: Data structure is interpreted when read rather than enforced when written, allowing flexible and evolving schemas
- **BASE**: Basically Available, Soft state, Eventually consistent -- an alternative to ACID for distributed systems

### Core Concepts (Q&A Format)
- Q: What is the CAP theorem and why can you only pick two?
- A: The CAP theorem states a distributed database can guarantee at most two of: Consistency (all nodes see the same data), Availability (every request gets a response), Partition Tolerance (system works despite network failures). Since network partitions are inevitable in distributed systems, you must choose between consistency and availability during a partition.

- Q: Where does MongoDB fall in the CAP theorem?
- A: MongoDB is a CP (Consistency + Partition Tolerance) database. During a network partition, it maintains consistency by sacrificing availability -- the primary node handles writes, and if it becomes unreachable, writes pause until a new primary is elected.

- Q: Where does Cassandra fall in the CAP theorem?
- A: Cassandra is an AP (Availability + Partition Tolerance) database. It uses eventual consistency, allowing writes to any node at any time and reconciling data inconsistencies asynchronously.

- Q: When should you use a graph database over a document store?
- A: Use a graph database when relationships between entities are the primary concern (social networks, fraud detection, recommendation engines). Use a document store when you need flexible schemas for semi-structured data with varied attributes (content management, product catalogs).

- Q: What does BASE stand for and how does it contrast with ACID?
- A: BASE = Basically Available, Soft state, Eventually consistent. Unlike ACID's strong consistency guarantees, BASE prioritizes availability and accepts temporary inconsistency, making it suitable for large-scale distributed systems.

- Q: How does horizontal scaling differ from vertical scaling?
- A: Horizontal scaling adds more nodes/machines to distribute load. Vertical scaling upgrades a single machine with more CPU, RAM, or storage. NoSQL databases favor horizontal scaling; relational databases traditionally rely on vertical scaling.

### Important Facts & Figures
- MongoDB stores data as BSON (Binary JSON) documents with a maximum document size of 16 MB
- Redis operates primarily in-memory, achieving sub-millisecond latency for read/write operations
- Cassandra was originally developed at Facebook for inbox search and later open-sourced
- Neo4j uses the Cypher query language for graph traversals
- Netflix, Amazon, and Facebook are prominent users of Cassandra for high-availability workloads
- MongoDB and Cassandra can distribute data across hundreds of nodes for horizontal scaling
- The CAP theorem was proposed by Eric Brewer in 2000 and formally proven in 2002
- NoSQL databases power social media feeds, IoT data collection, real-time analytics, and e-commerce catalogs

### Common Exam Questions
- Q: Compare and contrast SQL and NoSQL databases across three dimensions.
- A: Schema: SQL uses fixed schemas (schema-on-write); NoSQL uses flexible schemas (schema-on-read). Scaling: SQL scales vertically; NoSQL scales horizontally. Consistency: SQL provides strong ACID consistency; NoSQL often uses eventual consistency (BASE).

- Q: A startup needs to store user profiles where each user has different optional fields. Which database type is most appropriate and why?
- A: A document store like MongoDB, because its schema-less design allows each document to have different fields without requiring schema migrations, supporting agile development with varied data structures.

- Q: What is sharding and why is it used in NoSQL databases?
- A: Sharding partitions data across multiple nodes based on a shard key. It enables horizontal scaling by distributing storage and query load, allowing the database to handle datasets and traffic volumes that exceed any single machine's capacity.

- Q: Explain eventual consistency with a real-world analogy.
- A: Like a change made to a shared Google Doc -- after one person edits, other viewers may briefly see the old version before their screens update. The data is temporarily inconsistent but eventually converges to the correct state across all replicas.

---

## Vector Databases

### Key Terms & Definitions
- **Vector Embedding**: A dense numerical array (e.g., 1536 dimensions) that represents the semantic meaning of text, images, or other data, generated by AI models
- **Similarity Search**: The process of finding vectors closest to a query vector in high-dimensional space, used for semantic matching
- **Cosine Similarity**: A metric measuring the angle between two vectors; values range from -1 to 1, where 1 means identical direction
- **Euclidean Distance**: A metric measuring the straight-line distance between two points in vector space; smaller values mean more similar
- **Dot Product**: A similarity metric computed by multiplying corresponding vector components and summing; higher values indicate greater similarity
- **ANN (Approximate Nearest Neighbor)**: Search algorithms that trade small accuracy losses for massive speed gains when finding similar vectors
- **HNSW (Hierarchical Navigable Small World)**: A graph-based ANN indexing algorithm with multiple layers for fast approximate similarity search
- **IVF (Inverted File Index)**: An indexing method that clusters vectors and searches only the most relevant clusters during queries
- **Product Quantization**: A compression technique that reduces vector storage size by splitting vectors into sub-vectors and quantizing each
- **RAG (Retrieval-Augmented Generation)**: An architecture where an LLM retrieves relevant documents from a vector database to ground its responses in factual information

### Core Concepts (Q&A Format)
- Q: Why can't you just use a traditional database for similarity search over embeddings?
- A: Traditional databases are optimized for exact matches and range queries on structured data. Vector similarity search requires computing distances across hundreds or thousands of dimensions simultaneously, which needs specialized indexing (like HNSW) to be performant at scale.

- Q: How does HNSW work at a high level?
- A: HNSW builds a multi-layer graph where each vector is a node connected to similar neighbors. Upper layers are sparse for fast long-range navigation; lower layers are dense for precise local search. A query traverses from the top layer downward, converging on the nearest neighbors. It offers excellent recall and speed but is memory-intensive.

- Q: What is the difference between cosine similarity and Euclidean distance?
- A: Cosine similarity measures the angle between vectors (direction), ignoring magnitude -- useful when only semantic orientation matters. Euclidean distance measures the absolute spatial distance between vectors, accounting for both direction and magnitude.

- Q: How do vector databases support RAG?
- A: Documents are split into chunks, each embedded as a vector and stored in the vector database. When a user queries an LLM, the query is also embedded, and the vector database retrieves the most semantically similar document chunks. These chunks are injected into the LLM's prompt as context, grounding the response in factual, up-to-date information.

- Q: What is the trade-off in Approximate Nearest Neighbor search?
- A: ANN algorithms sacrifice a small amount of accuracy (recall) for dramatic improvements in search speed. Instead of comparing the query to every vector (exact search), they use indexing structures to narrow the candidate set, making search feasible over millions or billions of vectors.

- Q: What is pgvector and why is it significant?
- A: pgvector is a PostgreSQL extension that adds vector similarity search to an existing relational database. It is significant because organizations can add vector capabilities without adopting a separate specialized database.

### Important Facts & Figures
- Common embedding dimensions: OpenAI's text-embedding-ada-002 produces 1536-dimensional vectors; newer models use 256-3072 dimensions
- Pinecone, Weaviate, Milvus, Chroma, Qdrant, and pgvector are the leading vector database systems
- RAG accounts for approximately 51% of enterprise AI implementations as of 2025
- HNSW is the default indexing algorithm in most modern vector databases due to its speed-recall trade-off
- Vector databases can search millions of vectors in milliseconds using ANN algorithms
- The rise of LLMs (GPT, Claude, etc.) has driven massive growth in vector database adoption since 2023
- Pinecone is a fully managed (cloud-hosted) solution; Weaviate, Milvus, and Qdrant are open-source alternatives
- Vector search enables semantic matching (meaning-based) rather than keyword matching (exact text)

### Common Exam Questions
- Q: Explain how a vector database differs from a relational database in terms of data representation and querying.
- A: A relational database stores structured data in rows/columns and queries with exact matches (SQL WHERE clauses). A vector database stores high-dimensional numerical arrays (embeddings) and queries by finding the most similar vectors using distance metrics, enabling semantic search rather than keyword search.

- Q: A company wants to build a customer support chatbot that answers questions using its internal documentation. Describe the role of a vector database in this system.
- A: Internal documents are chunked and converted to vector embeddings, then stored in the vector database. When a customer asks a question, it is embedded and the vector database retrieves the most similar document chunks. These are passed to the LLM as context, enabling accurate answers grounded in company-specific information (RAG pattern).

- Q: Compare HNSW and IVF indexing methods.
- A: HNSW uses a multi-layer graph structure providing fast search with high recall but requires more memory. IVF clusters vectors and searches only relevant clusters, using less memory but potentially lower recall. HNSW is generally preferred for accuracy-critical applications; IVF is better for memory-constrained environments.

- Q: Why is approximate nearest neighbor search preferred over exact nearest neighbor search?
- A: Exact search (brute force) compares the query against every vector, taking O(n) time -- infeasible for millions of vectors. ANN uses indexing structures to search a fraction of vectors while still returning highly relevant results, reducing latency from seconds to milliseconds.

---

## Data Management for AI

### Key Terms & Definitions
- **Data Quality**: The degree to which data is accurate, complete, consistent, timely, and fit for its intended use in AI/ML systems
- **Data Governance**: The policies, processes, and standards for managing data availability, usability, integrity, security, and compliance across an organization
- **Data Lineage**: The tracking of data's origins, transformations, and movement through systems from source to consumption
- **Feature Store**: A centralized repository for computing, storing, and serving machine learning features, ensuring consistency between training and inference
- **Data Versioning**: Tracking changes to datasets over time to enable reproducibility of ML experiments and auditability
- **Data Profiling**: The process of examining and analyzing data to collect statistics and assess quality, completeness, and structure
- **Feature Engineering**: The process of transforming raw data into meaningful input variables (features) that improve model performance
- **Data Pipeline**: An automated series of processes that collect, transform, validate, and deliver data from sources to destinations
- **Metadata Management**: The practice of organizing and maintaining information about data assets (descriptions, schemas, ownership, quality metrics)
- **DVC (Data Version Control)**: An open-source tool for versioning datasets and ML models, similar to Git but designed for large data files
- **GDPR**: General Data Protection Regulation -- EU law governing personal data privacy, requiring consent, right to erasure, and data portability

### Core Concepts (Q&A Format)
- Q: Why is data quality especially critical for AI systems compared to traditional applications?
- A: AI models learn patterns directly from data, amplifying the "garbage in, garbage out" principle. Poor data quality leads to biased, inaccurate, or unreliable model predictions, and unlike traditional reports that humans can sanity-check, AI decisions may be automated at scale.

- Q: What is a feature store and why is it important?
- A: A feature store is a centralized system for defining, storing, and serving ML features. It ensures the same feature transformations used in training are applied at inference time (avoiding training-serving skew), enables feature sharing across teams, and maintains historical feature values for reproducibility.

- Q: What is the difference between data governance and data management?
- A: Data management is the broad practice of collecting, storing, and using data. Data governance is the framework of policies, roles, and standards that ensures data management is done consistently, securely, and in compliance with regulations.

- Q: What is training-serving skew and how does a feature store prevent it?
- A: Training-serving skew occurs when features computed during model training differ from those computed during real-time inference, causing degraded model performance. A feature store prevents this by providing a single source of feature definitions used in both environments.

- Q: How does data versioning support reproducible ML experiments?
- A: Data versioning tracks exact dataset snapshots used for each experiment, allowing researchers to reproduce results, compare model performance across different data versions, and roll back to previous datasets if issues arise.

- Q: What are the key dimensions of data quality?
- A: Accuracy (data correctly represents reality), Completeness (no missing values), Consistency (uniform rules across sources), Validity (data in correct format), and Timeliness (data is current and relevant).

### Important Facts & Figures
- "Garbage in, garbage out" is amplified in ML: data scientists spend 60-80% of their time on data preparation
- GDPR (EU, 2018) and CCPA (California, 2020) are the two most influential data privacy regulations
- Feast and Tecton are leading open-source and commercial feature store platforms
- DVC and LakeFS are popular tools for dataset versioning
- Feature stores maintain historical feature values, enabling point-in-time reconstruction of training conditions
- Data lineage is critical for regulatory compliance, debugging model issues, and impact analysis
- Bias in training data leads to biased AI outputs -- a key concern in responsible AI practices
- Organizations with robust data management infrastructure see faster model development and better regulatory compliance

### Common Exam Questions
- Q: A model performs well in testing but poorly in production. What data management issue could cause this?
- A: Training-serving skew -- the features or data transformations used during training differ from those in production. A feature store addresses this by ensuring consistent feature computation in both environments.

- Q: Explain why data lineage is important for AI compliance.
- A: Data lineage tracks where data originated, how it was transformed, and where it was used. This is critical for demonstrating compliance with regulations like GDPR (proving data handling practices), auditing model decisions, and identifying the impact when source data quality issues are discovered.

- Q: What role does metadata management play in data governance?
- A: Metadata management catalogs information about data assets (ownership, definitions, quality scores, access policies), enabling discovery, understanding, and proper use of data across the organization while supporting compliance and audit requirements.

- Q: Describe three strategies for handling missing values in a dataset.
- A: (1) Deletion: remove rows/columns with missing values (acceptable if data is missing completely at random and the dataset is large). (2) Imputation: fill missing values with mean, median, mode, or model-predicted values. (3) Flagging: create a binary indicator column noting missingness, allowing the model to learn from the pattern of missing data.

---

## Database Design

### Key Terms & Definitions
- **Entity-Relationship (ER) Diagram**: A visual representation of entities, their attributes, and relationships used in conceptual database design
- **Entity**: A real-world object or concept represented as a table in a database (e.g., Customer, Order, Product)
- **Cardinality**: The numerical relationship between entities: one-to-one (1:1), one-to-many (1:N), or many-to-many (M:N)
- **Normalization**: The process of structuring tables to minimize redundancy and dependency, progressing through normal forms
- **Denormalization**: Intentionally introducing redundancy into a database design to improve read/query performance
- **Star Schema**: A data warehouse design with a central fact table connected to surrounding dimension tables (denormalized)
- **Snowflake Schema**: A data warehouse design extending the star schema where dimension tables are further normalized into sub-dimensions
- **Fact Table**: The central table in a star/snowflake schema containing measurable, quantitative data (metrics, transactions)
- **Dimension Table**: A table surrounding the fact table containing descriptive attributes used for filtering and grouping (e.g., time, product, location)
- **OLTP (Online Transaction Processing)**: Database systems optimized for fast, frequent, short transactions (inserts, updates, deletes)
- **OLAP (Online Analytical Processing)**: Database systems optimized for complex queries and aggregations over large historical datasets
- **Data Warehouse**: A centralized repository of integrated data from multiple sources, structured for analytical querying

### Core Concepts (Q&A Format)
- Q: What are the four stages of the database design process?
- A: (1) Requirements analysis -- gather business needs. (2) Conceptual design -- create ER diagrams. (3) Logical design -- define schemas and normalize. (4) Physical design -- optimize with indexes, partitioning, and storage configuration.

- Q: What is the difference between a star schema and a snowflake schema?
- A: A star schema has denormalized dimension tables directly connected to the fact table, creating a star shape -- simpler and faster for queries. A snowflake schema normalizes dimension tables into sub-dimensions, reducing redundancy but increasing query complexity with more joins.

- Q: When would you choose denormalization over normalization?
- A: Denormalization is chosen for read-heavy analytical workloads (OLAP) where query speed is prioritized over storage efficiency. Normalized designs are preferred for write-heavy transactional workloads (OLTP) where data integrity and minimal redundancy matter most.

- Q: What is the difference between OLTP and OLAP systems?
- A: OLTP handles frequent, short transactions (e.g., processing an order) with normalized schemas optimized for writes. OLAP handles complex analytical queries over large historical datasets (e.g., sales trends) with denormalized schemas optimized for reads.

- Q: What are the three types of data anomalies that normalization prevents?
- A: Insert anomaly (cannot add data without unrelated data), Update anomaly (updating one copy of duplicated data but not others), Delete anomaly (deleting data unintentionally removes other needed data).

- Q: What is a many-to-many relationship and how is it implemented?
- A: A many-to-many relationship exists when multiple records in one table relate to multiple records in another (e.g., students and courses). It is implemented using a junction (bridge) table that contains foreign keys to both tables, breaking the M:N into two 1:N relationships.

- Q: What is a surrogate key and when is it preferred over a natural key?
- A: A surrogate key is a system-generated identifier (auto-incrementing integer or UUID) with no business meaning. It is preferred when natural keys are long, composite, or subject to change, as it provides a stable, efficient primary key.

### Important Facts & Figures
- The ER model was proposed by Peter Chen in 1976
- Star schemas are the most common design pattern in data warehouses and BI systems
- Snowflake schemas use 10-20% less storage than star schemas but require more joins
- OLTP systems typically use 3NF or BCNF; OLAP systems typically use star or snowflake schemas
- Data lakes store raw, unprocessed data; data warehouses store processed, structured data
- Indexing strategies include B-tree (default for most queries), hash (equality lookups), and bitmap (low-cardinality columns)
- Partitioning divides large tables into smaller segments (by range, list, or hash) for faster queries and easier maintenance
- Modern architectures often combine OLTP and OLAP using data lakehouse patterns (e.g., Delta Lake, Apache Iceberg)

### Common Exam Questions
- Q: Draw an ER diagram for a university registration system with Students, Courses, and Instructors. Identify entities, relationships, and cardinalities.
- A: Entities: Student (StudentID, Name, Major), Course (CourseID, Title, Credits), Instructor (InstructorID, Name, Department). Relationships: Students ENROLL in Courses (M:N via Enrollment junction table), Instructors TEACH Courses (1:N). The Enrollment table contains StudentID, CourseID, Grade, and Semester.

- Q: A reporting query on a normalized OLTP database is running slowly. What design change would you recommend?
- A: Create a denormalized star schema in a separate data warehouse or materialized view. The fact table holds transaction metrics; dimension tables hold descriptive attributes. This reduces the number of joins needed for analytical queries.

- Q: Explain the trade-off between normalization and denormalization.
- A: Normalization minimizes redundancy and prevents anomalies, ensuring data integrity for transactional systems but requiring more joins for complex queries. Denormalization duplicates data to reduce joins and speed up reads for analytical workloads but increases storage and the risk of inconsistencies during writes.

- Q: What is the purpose of partitioning a database table?
- A: Partitioning splits a large table into smaller, more manageable segments based on a key (e.g., date range). This improves query performance (only relevant partitions are scanned), simplifies maintenance (e.g., dropping old partitions), and enables parallel processing.

---
