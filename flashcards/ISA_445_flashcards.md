# ISA 445: Advanced Web Programming - Flashcard Reference Bank

---

## Server-Side Programming

### Key Terms & Definitions
- **Server-Side Programming**: Code that runs on a web server (not the browser) to process requests, interact with databases, and generate dynamic content sent back to the client.
- **HTTP (HyperText Transfer Protocol)**: The stateless application-layer protocol used for communication between clients and servers on the web.
- **Request-Response Cycle**: The process where a client sends an HTTP request, the server processes it (authentication, data retrieval, business logic), and returns an HTTP response.
- **Middleware**: Intermediate functions that sit between the incoming request and the final route handler, performing tasks like logging, authentication, input validation, and error handling.
- **Session**: A server-side mechanism for storing information associated with the current user across multiple stateless HTTP requests, identified by a unique session ID.
- **Cookie**: A small piece of data stored by the browser and sent with every subsequent request, commonly used to transmit session IDs.
- **JSON Web Token (JWT)**: A compact, URL-safe token format used for stateless authentication, consisting of a header, payload, and signature.
- **Web Framework**: A software library providing routing, templating, and security features to accelerate server-side development (e.g., Django, Express, Laravel, Rails, ASP.NET).
- **Statelessness**: The property of HTTP where each request-response pair is independent; the server does not retain information between requests without explicit session management.
- **Cross-Site Scripting (XSS)**: A security vulnerability where an attacker injects malicious scripts into web pages viewed by other users.
- **CSRF (Cross-Site Request Forgery)**: An attack that tricks a user's browser into making an unintended request to a server where the user is authenticated.

### Core Concepts (Q&A Format)
- Q: Why is HTTP considered stateless, and what problem does this create?
- A: Each HTTP request is independent with no memory of previous interactions. This means the server cannot inherently track users across requests, requiring session management techniques (cookies, JWT, server-side sessions).

- Q: What is the role of middleware in a server-side application?
- A: Middleware intercepts requests before they reach route handlers, enabling cross-cutting concerns like logging, authentication checks, input validation, CORS handling, and error management in a reusable, modular way.

- Q: How does session-based authentication differ from token-based authentication (JWT)?
- A: Session-based auth stores session data on the server and sends a session ID via cookie. JWT stores all user data in a signed token held by the client, making it stateless on the server side and easier to scale horizontally.

- Q: What are the primary responsibilities of server-side code?
- A: Processing HTTP requests, enforcing business logic, managing authentication/authorization, interacting with databases, generating dynamic content, and handling security concerns.

- Q: Name three popular server-side frameworks and their languages.
- A: Django (Python), Express.js (Node.js/JavaScript), and Laravel (PHP). Others include Rails (Ruby) and ASP.NET (C#).

- Q: How does server-side code prevent SQL injection?
- A: By using parameterized queries or prepared statements, which separate SQL code from user input, preventing malicious input from being executed as SQL commands.

### Important Facts & Figures
- Common server-side languages: Python, JavaScript (Node.js), PHP, Ruby, Java, C#.
- The HTTP request contains a method (GET, POST, PUT, DELETE), URL, headers, and optional body.
- HTTP status codes: 200 (OK), 301 (Redirect), 400 (Bad Request), 401 (Unauthorized), 403 (Forbidden), 404 (Not Found), 500 (Internal Server Error).
- Sessions typically use server-side stores (Redis, database) or in-memory storage, while JWTs are self-contained tokens stored client-side.
- OWASP Top 10 is the standard reference for web application security risks, including injection, broken authentication, and XSS.
- Middleware executes in the order it is registered, forming a pipeline or chain.

### Common Exam Questions
- Q: Explain the HTTP request-response cycle and identify what happens at each stage.
- A: Client sends HTTP request (method, URL, headers, body) -> Server receives and parses request -> Middleware processes (auth, validation) -> Route handler executes business logic -> Server returns HTTP response (status code, headers, body).

- Q: Compare and contrast cookies and JWTs for session management.
- A: Cookies are server-managed, stored on the client, sent automatically with every request, and require server-side session storage. JWTs are self-contained, stateless, scalable, but cannot be easily revoked once issued.

- Q: What security vulnerabilities must server-side code protect against?
- A: SQL injection, XSS, CSRF, insecure authentication, session hijacking, and insecure direct object references. Mitigation includes parameterized queries, input sanitization, CSRF tokens, and HTTPS.

---

## Web Application Architecture

### Key Terms & Definitions
- **Client-Server Model**: The foundational architecture where a client (browser) sends requests to a server, which processes them and returns responses.
- **Three-Tier Architecture**: Divides an application into presentation tier (UI), application/logic tier (business rules), and data tier (database), each independently developable and scalable.
- **MVC (Model-View-Controller)**: A design pattern where Model manages data/logic, View handles UI, and Controller mediates user input between Model and View.
- **Microservices Architecture**: Decomposes an application into small, independently deployable services that communicate over APIs (typically HTTP or messaging).
- **Monolithic Architecture**: A single codebase and deployment unit containing all application functionality; simpler initially but harder to scale and modify.
- **Load Balancer**: A device or software that distributes incoming network traffic across multiple servers to ensure no single server is overwhelmed.
- **CDN (Content Delivery Network)**: A geographically distributed network of servers that caches and delivers content closer to users, reducing latency.
- **Horizontal Scaling**: Adding more server instances to handle increased traffic (scaling out), as opposed to vertical scaling (upgrading a single server).
- **Service Registry**: A central directory where microservices register themselves and discover each other dynamically without hardcoded addresses.
- **API Gateway**: A single entry point for all client requests to a microservices architecture, handling routing, authentication, and rate limiting.

### Core Concepts (Q&A Format)
- Q: What are the three tiers in three-tier architecture and what does each do?
- A: Presentation tier (handles UI/user interaction), Application tier (processes business logic and rules), Data tier (manages database storage and retrieval). Each tier can be scaled independently.

- Q: What is the key difference between monolithic and microservices architecture?
- A: Monolithic bundles all functionality into a single deployable unit, while microservices decompose the application into small, independently deployable services communicating over APIs. Microservices trade simplicity for flexibility and horizontal scalability.

- Q: How does the MVC pattern separate concerns?
- A: Model handles data and business logic, View handles presentation/UI, Controller receives user input and coordinates updates between Model and View. This separation makes code more maintainable and testable.

- Q: Why do production architectures use load balancers and caching?
- A: Load balancers distribute traffic across servers to prevent overload and ensure availability. Caching (Redis, CDNs) reduces database load and improves response times by serving frequently accessed data from memory.

- Q: What is the role of an API Gateway in microservices?
- A: It acts as a single entry point for all client requests, routing them to appropriate microservices, and handling cross-cutting concerns like authentication, rate limiting, and response aggregation.

- Q: What is the difference between horizontal and vertical scaling?
- A: Horizontal scaling adds more server instances (scale out). Vertical scaling upgrades a single server's hardware (scale up). Microservices favor horizontal scaling.

### Important Facts & Figures
- MVC is implemented by frameworks like Django, Rails, Spring MVC, and ASP.NET MVC.
- Amazon uses microservices architecture to independently scale services like search, checkout, and recommendations.
- Netflix pioneered microservices adoption at scale, operating hundreds of microservices.
- Three-tier architecture is the most common enterprise web application pattern.
- A monolith requires redeploying the entire application for any change; microservices allow independent deployment.
- Common caching solutions: Redis (in-memory data store), Memcached, Varnish (HTTP cache).

### Common Exam Questions
- Q: Compare monolithic and microservices architectures, listing advantages and disadvantages of each.
- A: Monolithic: simpler development/testing, easier deployment initially, but harder to scale and modify. Microservices: independent scaling/deployment, technology flexibility, fault isolation, but increased complexity in communication, monitoring, and data consistency.

- Q: Describe how the MVC pattern works and name frameworks that implement it.
- A: User input goes to Controller, which updates Model (data/logic), which notifies View (UI) to re-render. Frameworks: Django (MTV variant), Rails, Spring MVC, ASP.NET MVC.

- Q: When would you choose three-tier architecture over microservices?
- A: Three-tier is suitable for smaller applications or teams that need clear separation of concerns without the operational complexity of microservices. Microservices are better for large-scale applications requiring independent team development and deployment.

---

## Database Connectivity

### Key Terms & Definitions
- **ODBC (Open Database Connectivity)**: A language-agnostic standard API for accessing relational databases, allowing application code to work with different vendors without modification.
- **JDBC (Java Database Connectivity)**: Java's standard API for connecting to and interacting with relational databases.
- **ORM (Object-Relational Mapping)**: A technique that maps database tables to programming language objects, generating SQL automatically to simplify CRUD operations (e.g., Hibernate, Django ORM, Entity Framework, Sequelize).
- **Connection Pooling**: A cache of reusable database connections that reduces the overhead of repeatedly opening and closing connections, dramatically improving performance under load.
- **Prepared Statement**: A precompiled SQL statement that separates SQL logic from user input, preventing SQL injection and improving performance through query plan reuse.
- **SQL Injection**: An attack where malicious SQL code is inserted into input fields to manipulate database queries and access unauthorized data.
- **CRUD**: The four basic database operations: Create, Read, Update, Delete.
- **Query Builder**: A programmatic interface for constructing SQL queries (e.g., Knex.js), offering more control than a full ORM but less boilerplate than raw SQL.
- **NoSQL Database**: Non-relational databases (MongoDB, Redis, Cassandra) offering flexible schemas suited for unstructured or rapidly evolving data.
- **TLS/SSL**: Encryption protocols used to secure database connections in transit, preventing eavesdropping and man-in-the-middle attacks.

### Core Concepts (Q&A Format)
- Q: What is the difference between ODBC and JDBC?
- A: ODBC is a language-agnostic standard API for database connectivity that works across multiple programming languages. JDBC is specifically designed for Java applications. Both provide a uniform interface to work with different database vendors.

- Q: How does an ORM simplify database interactions?
- A: ORMs map database tables to programming objects, automatically generating SQL for CRUD operations. This reduces boilerplate code, minimizes SQL injection risk, and lets developers work with familiar object-oriented patterns instead of raw SQL.

- Q: Why is connection pooling important for web applications?
- A: Opening a new database connection for every request is expensive. Connection pools maintain a cache of reusable connections, dramatically reducing latency and resource consumption, especially under heavy concurrent load.

- Q: How do prepared statements prevent SQL injection?
- A: Prepared statements separate SQL code from user-supplied data. The database engine compiles the SQL structure first, then safely binds user input as parameters, ensuring input is treated as data, not executable code.

- Q: When would you choose a NoSQL database over a relational database?
- A: NoSQL is better for unstructured/semi-structured data, rapidly evolving schemas, horizontal scalability needs, and high-velocity data. Relational databases are better for complex queries, transactions, and strong consistency requirements.

- Q: What is the difference between a query builder and an ORM?
- A: A query builder (e.g., Knex.js) provides programmatic SQL construction with more control and flexibility than an ORM but without the full object-to-table mapping. ORMs abstract away SQL entirely.

### Important Facts & Figures
- Popular ORMs: Hibernate (Java), Entity Framework (.NET), Django ORM (Python), Sequelize (Node.js), ActiveRecord (Ruby).
- HikariCP is the highest-performance JDBC connection pool for Java applications.
- Default HDFS block size is 128 MB, but database connection pool sizes are typically configured based on expected concurrent users (commonly 10-50 connections).
- SQL databases: MySQL, PostgreSQL, SQL Server, Oracle. NoSQL databases: MongoDB (document), Redis (key-value), Cassandra (wide-column), Neo4j (graph).
- Database credentials should be stored in environment variables, never hardcoded in source code.
- Most ORMs use ODBC or JDBC under the hood for actual database communication.

### Common Exam Questions
- Q: Compare ORMs with raw SQL. What are the trade-offs?
- A: ORMs reduce boilerplate, prevent SQL injection, and improve developer productivity. However, they can generate inefficient queries, add abstraction overhead, and make complex queries harder to optimize. Raw SQL offers full control and performance but requires more code and manual injection prevention.

- Q: Explain how connection pooling works and why it improves performance.
- A: A pool maintains a set of pre-established database connections. When a request needs a connection, it borrows one from the pool and returns it when done. This avoids the overhead of creating/destroying connections per request, reducing latency and database server load.

- Q: What are the security best practices for database connectivity?
- A: Use parameterized queries/prepared statements, store credentials in environment variables, encrypt connections with TLS/SSL, implement least-privilege database accounts, and use connection pooling to limit resource exposure.

---

## APIs

### Key Terms & Definitions
- **API (Application Programming Interface)**: A set of rules and protocols allowing different software systems to communicate with each other.
- **REST (Representational State Transfer)**: An architectural style using standard HTTP methods (GET, POST, PUT, DELETE) to perform CRUD operations on resources identified by URLs; stateless, typically returns JSON.
- **SOAP (Simple Object Access Protocol)**: An XML-based messaging protocol with strict standards for security (WS-Security), transactions, and reliability; common in enterprise environments.
- **GraphQL**: A query language developed by Facebook (2012) that uses a single endpoint and lets clients request exactly the data fields they need, avoiding over-fetching and under-fetching.
- **OAuth 2.0**: An authorization framework that allows third-party applications to access user resources without exposing credentials, using access tokens.
- **API Key**: A simple authentication token passed with API requests to identify the calling application.
- **Rate Limiting**: A technique to control the number of API requests a client can make within a time window, preventing abuse and ensuring fair usage.
- **WSDL (Web Services Description Language)**: An XML-based format for describing SOAP web service interfaces.
- **Swagger/OpenAPI**: A specification for defining REST API contracts in a machine-readable format, enabling auto-generated documentation and client SDKs.
- **Endpoint**: A specific URL where an API resource can be accessed; REST APIs typically have multiple endpoints while GraphQL uses a single endpoint.
- **Idempotency**: The property where making the same API request multiple times produces the same result (GET, PUT, DELETE are idempotent; POST is not).

### Core Concepts (Q&A Format)
- Q: What are the key differences between REST, SOAP, and GraphQL?
- A: REST uses multiple endpoints, standard HTTP methods, and JSON; is lightweight and stateless. SOAP uses XML, has built-in WS-Security, and is strict/formal. GraphQL uses a single endpoint, lets clients specify exact data needs, and avoids over/under-fetching.

- Q: What is the over-fetching problem in REST and how does GraphQL solve it?
- A: REST endpoints return fixed data structures, often including fields the client doesn't need (over-fetching) or requiring multiple requests for related data (under-fetching). GraphQL lets clients specify exactly which fields they need in a single request.

- Q: How does OAuth 2.0 work at a high level?
- A: The client requests authorization from the resource owner, receives an authorization grant, exchanges it for an access token from the authorization server, and uses that token to access protected resources on the resource server.

- Q: What HTTP methods correspond to CRUD operations in REST?
- A: Create = POST, Read = GET, Update = PUT/PATCH, Delete = DELETE. GET, PUT, and DELETE are idempotent.

- Q: Why is API versioning important?
- A: Versioning (e.g., /api/v1/) allows backward-compatible evolution of endpoints. Existing clients continue using older versions while new clients adopt updated APIs, preventing breaking changes.

- Q: When would you choose SOAP over REST?
- A: SOAP is preferred in enterprise environments requiring built-in security (WS-Security), ACID-compliant transactions, formal contracts (WSDL), and reliability -- common in banking, healthcare, and government systems.

### Important Facts & Figures
- REST is the most widely used API style for web and mobile applications.
- GraphQL was developed by Facebook in 2012 and open-sourced in 2015.
- SOAP only supports XML; REST supports JSON, XML, YAML, and other formats.
- HTTP status codes for APIs: 200 (OK), 201 (Created), 204 (No Content), 400 (Bad Request), 401 (Unauthorized), 403 (Forbidden), 404 (Not Found), 429 (Too Many Requests), 500 (Server Error).
- Postman and Insomnia are popular tools for testing API endpoints during development.
- SOAP messages are larger due to XML envelope overhead, making them slower, especially on mobile networks.

### Common Exam Questions
- Q: Compare REST and GraphQL APIs. When would you use each?
- A: REST is simpler, well-established, cacheable, and ideal for straightforward CRUD operations. GraphQL is better for complex data models, mobile apps with bandwidth constraints, and scenarios where clients need flexible data retrieval from a single endpoint.

- Q: Describe three methods of API authentication and when each is appropriate.
- A: API keys (simple, for identifying apps, low security), OAuth 2.0 (delegated authorization for third-party access, high security), JWT (stateless token-based auth, good for microservices). OAuth 2.0 is best for user-facing apps; API keys for server-to-server; JWT for distributed systems.

- Q: What is rate limiting and why do production APIs implement it?
- A: Rate limiting restricts the number of requests a client can make per time window. It prevents abuse, protects server resources, ensures fair usage among clients, and mitigates denial-of-service attacks.

- Q: Explain the concept of idempotency in REST APIs with examples.
- A: An idempotent operation produces the same result regardless of how many times it is called. GET (reading data), PUT (replacing a resource), and DELETE (removing a resource) are idempotent. POST (creating a resource) is not -- calling it twice creates two resources.

---

## Backend Development

### Key Terms & Definitions
- **Backend Development**: All server-side logic, infrastructure, and data management powering a web application behind the scenes.
- **Authentication**: Verifying a user's identity (who they are) through credentials, tokens, or third-party providers.
- **Authorization**: Verifying a user's permissions (what they can access) through role-based access control (RBAC) or policy-based access control.
- **Docker**: A containerization platform that packages applications and their dependencies into isolated, portable containers for consistent deployment across environments.
- **Kubernetes**: An orchestration platform for automating deployment, scaling, and management of containerized applications across clusters.
- **CI/CD (Continuous Integration / Continuous Deployment)**: Automated pipelines that build, test, and deploy code changes. CI merges and tests code frequently; CD automatically deploys tested code to production.
- **RBAC (Role-Based Access Control)**: An authorization model where permissions are assigned to roles, and users are assigned roles, controlling access to resources.
- **Environment Variables**: Configuration values stored outside the codebase (database URLs, API keys, secrets) that vary between deployment environments.
- **Message Queue**: An asynchronous communication mechanism (RabbitMQ, Kafka) where producers send messages to a queue and consumers process them independently.
- **Caching**: Storing frequently accessed data in fast-access memory (Redis, Memcached) to reduce database queries and improve response times.
- **Reverse Proxy**: A server that sits in front of backend servers, forwarding client requests and providing load balancing, SSL termination, and caching (e.g., Nginx, Apache).

### Core Concepts (Q&A Format)
- Q: What is the difference between authentication and authorization?
- A: Authentication verifies identity (who you are) via credentials or tokens. Authorization verifies permissions (what you can do) via roles or policies. Authentication must happen before authorization.

- Q: How does Docker improve backend deployment?
- A: Docker packages an application and all its dependencies into a container that runs identically across development, staging, and production environments, eliminating "works on my machine" problems and enabling consistent, reproducible deployments.

- Q: What is a CI/CD pipeline and what are its typical stages?
- A: An automated workflow triggered by code commits. Typical stages: source (code push), build (compile/package), test (automated unit/integration tests), deploy (push to staging/production). It ensures code quality and enables rapid, reliable releases.

- Q: Why do backend systems use message queues?
- A: Message queues (RabbitMQ, Kafka) enable asynchronous processing, decoupling producers from consumers. This handles tasks like email sending, notifications, and data processing without blocking the main request-response cycle, improving scalability and resilience.

- Q: What is the purpose of caching in backend systems?
- A: Caching stores frequently accessed data in memory (Redis, Memcached) to reduce database load and improve response times. Common caching strategies include cache-aside, write-through, and write-behind.

- Q: How does horizontal scaling differ from vertical scaling in backend systems?
- A: Horizontal scaling adds more server instances behind a load balancer (scale out). Vertical scaling adds more CPU/RAM to a single server (scale up). Horizontal scaling is preferred for backend microservices because it provides better fault tolerance and near-linear capacity growth.

### Important Facts & Figures
- Popular backend frameworks: Express.js (Node.js), Django (Python), Spring Boot (Java), ASP.NET Core (C#), Rails (Ruby).
- Docker containers share the host OS kernel, making them lighter than virtual machines.
- Kubernetes was originally developed by Google and is now maintained by the CNCF.
- Common CI/CD tools: GitHub Actions, Jenkins, GitLab CI, CircleCI, Travis CI.
- Redis can handle over 100,000 operations per second, making it ideal for caching and session storage.
- The 12-Factor App methodology defines best practices for building modern backend applications, including storing config in environment variables.

### Common Exam Questions
- Q: Describe the components of a modern backend deployment pipeline.
- A: Developer pushes code to version control (Git) -> CI server detects changes -> Automated build (compile, Docker image creation) -> Automated tests (unit, integration, end-to-end) -> Deploy to staging -> Manual approval or automated promotion -> Deploy to production. Tools: GitHub Actions, Docker, Kubernetes.

- Q: Compare session-based and token-based (JWT) authentication approaches.
- A: Session-based: server stores session data, sends session ID via cookie, requires server-side storage, harder to scale horizontally. Token-based (JWT): server issues a signed token, client stores it, server validates signature on each request, stateless, scales easily but tokens cannot be revoked without additional infrastructure.

- Q: What is the role of environment variables in backend development?
- A: Environment variables store configuration that varies between environments (development, staging, production) such as database URLs, API keys, and secrets. They keep sensitive data out of source code and enable the same codebase to run in different environments without modification.

- Q: Explain the difference between Docker containers and virtual machines.
- A: Docker containers share the host OS kernel and are lightweight (MB-sized, start in seconds). VMs include a full guest OS and are heavier (GB-sized, start in minutes). Containers are more efficient for microservices; VMs provide stronger isolation.
