# SQL SELECT Theory — 100 Single-Answer MCQ Questions

## Multiple Choice Questions

### 1. What is the main purpose of the `SELECT` statement in SQL?

- [ ] A. To change table structure
- [ ] B. To create a new database
- [ ] C. To retrieve data from a table
- [ ] D. To delete rows from a table

**Correct answer: C**

---

### 2. Which clause specifies the table from which data is retrieved?

- [ ] A. `ORDER BY`
- [ ] B. `GROUP BY`
- [ ] C. `WHERE`
- [ ] D. `FROM`

**Correct answer: D**

---

### 3. Which clause is used to filter rows before they are returned?

- [ ] A. `SELECT`
- [ ] B. `WHERE`
- [ ] C. `ORDER BY`
- [ ] D. `DISTINCT`

**Correct answer: B**

---

### 4. Which clause is used to sort query results?

- [ ] A. `HAVING`
- [ ] B. `FROM`
- [ ] C. `ORDER BY`
- [ ] D. `WHERE`

**Correct answer: C**

---

### 5. What does `ORDER BY OrderTotal DESC` do?

- [ ] A. Sorts order totals from largest to smallest
- [ ] B. Removes duplicate order totals
- [ ] C. Sorts order totals from smallest to largest
- [ ] D. Filters only expensive orders

**Correct answer: A**

---

### 6. Which operator is best for checking whether a value matches one value from a list?

- [ ] A. `LIKE`
- [ ] B. `IS NULL`
- [ ] C. `IN`
- [ ] D. `BETWEEN`

**Correct answer: C**

---


### 7. What does the `BETWEEN` operator check?

- [ ] A. Whether a value is missing
- [ ] B. Whether text matches a pattern
- [ ] C. Whether a value is inside an inclusive range
- [ ] D. Whether a value is equal to one item in a list

**Correct answer: C**

---

### 8. Is `BETWEEN` inclusive?

- [ ] A. Yes, it includes both boundary values
- [ ] B. It includes only the upper boundary
- [ ] C. It includes only the lower boundary
- [ ] D. No, it excludes both boundary values

**Correct answer: A**

---

### 9. Why can `BETWEEN` be risky with timestamp values such as `created_at`?

- [ ] A. The lower boundary is always excluded for timestamp columns
- [ ] B. The upper boundary may mean midnight and exclude later times on the final date
- [ ] C. Timestamp columns cannot be compared with range conditions
- [ ] D. `BETWEEN` always treats dates as text, not temporal values

**Correct answer: B**

---

### 10. What is the main purpose of `LIKE`?

- [ ] A. Pattern matching in text
- [ ] B. Date calculation
- [ ] C. Numeric comparison
- [ ] D. Grouping rows

**Correct answer: A**

---

### 11. What does `%` mean in a `LIKE` pattern?

- [ ] A. Any number of characters
- [ ] B. A numeric percentage only
- [ ] C. A missing value
- [ ] D. Exactly one character

**Correct answer: A**

---


### 12. Which condition finds customer names starting with `Nino`?

- [ ] A. `CustomerName = '%Nino%'`
- [ ] B. `CustomerName LIKE '%Nino%'`
- [ ] C. `CustomerName LIKE 'Nino%'`
- [ ] D. `CustomerName LIKE '%Nino'`

**Correct answer: C**

---

### 13. Which condition finds emails ending with `@example.com`?

- [ ] A. `CustomerEmail LIKE '@example.com%'`
- [ ] B. `CustomerEmail IN '@example.com'`
- [ ] C. `CustomerEmail = '%@example.com'`
- [ ] D. `CustomerEmail LIKE '%@example.com'`

**Correct answer: D**

---

### 14. What does `NULL` mean in SQL?

- [ ] A. Empty string only
- [ ] B. False
- [ ] C. Zero
- [ ] D. Unknown, missing, or not applicable

**Correct answer: D**

---

### 15. Which condition correctly checks for missing delivery date?

- [ ] A. `DeliveredAt == NULL`
- [ ] B. `DeliveredAt LIKE NULL`
- [ ] C. `DeliveredAt IS NULL`
- [ ] D. `DeliveredAt = NULL`

**Correct answer: C**

---


### 16. Which standard SQL function returns the first non-`NULL` expression from a list?

- [ ] A. `NULLVALUE()`
- [ ] B. `COALESCE()`
- [ ] C. `REPLACENULL()`
- [ ] D. `ISNULL()`

**Correct answer: B**

---


### 17. What is the purpose of `DISTINCT`?

- [ ] A. To filter rows by condition
- [ ] B. To group rows after aggregation
- [ ] C. To sort rows
- [ ] D. To remove duplicate rows from the result

**Correct answer: D**

---


### 18. What does `ASC` mean in `ORDER BY`?

- [ ] A. Aggregate sort calculation
- [ ] B. Automatic search condition
- [ ] C. Ascending order
- [ ] D. Alias sort column

**Correct answer: C**

---

### 19. What does `DESC` mean in `ORDER BY`?

- [ ] A. Descending order
- [ ] B. Distinct search
- [ ] C. Delete selected column
- [ ] D. Describe table

**Correct answer: A**

---

### 20. What is pagination in query results?

- [ ] A. Joining every row from two tables
- [ ] B. Grouping rows before aggregation
- [ ] C. Removing duplicate rows from a table permanently
- [ ] D. Returning a limited, ordered portion of a larger result set

**Correct answer: D**

---

### 21. Which aggregate function counts rows?

- [ ] A. `AVG()`
- [ ] B. `COUNT()`
- [ ] C. `MAX()`
- [ ] D. `SUM()`

**Correct answer: B**

---

### 22. What does `COUNT(*)` count?

- [ ] A. Only distinct rows
- [ ] B. Only text values
- [ ] C. All rows
- [ ] D. Only non-null values in one column

**Correct answer: C**

---

### 23. What does `COUNT(SatisfactionScore)` count?

- [ ] A. Only rows where `SatisfactionScore` is zero
- [ ] B. Only rows where `SatisfactionScore` is not null
- [ ] C. Only distinct satisfaction scores
- [ ] D. All rows

**Correct answer: B**

---

### 24. What does `COUNT(DISTINCT CustomerID)` count?

- [ ] A. Duplicate customers
- [ ] B. Unique customers
- [ ] C. Null customer IDs only
- [ ] D. All orders

**Correct answer: B**

---


### 25. What is the purpose of `GROUP BY`?

- [ ] A. To remove all nulls
- [ ] B. To group rows with the same values for aggregation
- [ ] C. To delete duplicate rows
- [ ] D. To sort rows alphabetically

**Correct answer: B**

---

### 26. Which clause is usually used together with aggregate functions?

- [ ] A. `IS NULL`
- [ ] B. `GROUP BY`
- [ ] C. `OFFSET`
- [ ] D. `LIKE`

**Correct answer: B**

---

### 27. When grouping by multiple columns, what happens?

- [ ] A. the database system returns only one row
- [ ] B. the database system ignores aggregate functions
- [ ] C. the database system groups by only the first column
- [ ] D. the database system groups by unique combinations of those columns

**Correct answer: D**

---

### 29. Which clause filters grouped results?

- [ ] A. `WHERE`
- [ ] B. `HAVING`
- [ ] C. `ORDER BY`
- [ ] D. `SELECT`

**Correct answer: B**

---

### 30. Which clause filters individual rows before grouping?

- [ ] A. `GROUP BY`
- [ ] B. `COUNT`
- [ ] C. `HAVING`
- [ ] D. `WHERE`

**Correct answer: D**

---


### 31. What is the correct logical meaning of using both `WHERE` and `HAVING`?

- [ ] A. `HAVING` filters rows first, then `WHERE` filters groups
- [ ] B. Both filter only individual rows
- [ ] C. Both filter only selected columns
- [ ] D. `WHERE` filters rows first, then `HAVING` filters groups

**Correct answer: D**

---

### 32. Which function rounds upward?

- [ ] A. `FLOOR()`
- [ ] B. `CEILING()`
- [ ] C. `ABS()`
- [ ] D. `SIGN()`

**Correct answer: B**

---

### 33. Which function rounds downward?

- [ ] A. `FLOOR()`
- [ ] B. `SQRT()`
- [ ] C. `POWER()`
- [ ] D. `CEILING()`

**Correct answer: A**

---


### 34. Which function removes spaces from both sides of a string?

- [ ] A. `TRIM()`
- [ ] B. `CONCAT()`
- [ ] C. `POSITION()`
- [ ] D. `CHAR_LENGTH()`

**Correct answer: A**

---

### 35. Which function joins strings together?

- [ ] A. `EXTRACT()`
- [ ] B. `CONCAT()`
- [ ] C. `COUNT()`
- [ ] D. `SUM()`

**Correct answer: B**

---

### 36. What is a candidate key?

- [ ] A. A possible unique identifier
- [ ] B. A temporary table
- [ ] C. A nullable text field
- [ ] D. A duplicated column

**Correct answer: A**

---

### 37. What is a primary key?

- [ ] A. A repeated value
- [ ] B. A the database system login
- [ ] C. Any nullable column
- [ ] D. The chosen unique identifier

**Correct answer: D**

---

### 38. What is a foreign key?

- [ ] A. A key that references another table
- [ ] B. A command for deleting rows
- [ ] C. A type of string function
- [ ] D. A column that must contain duplicate values

**Correct answer: A**

---

### 39. What does a unique constraint prevent?

- [ ] A. Duplicate values in the constrained column or columns
- [ ] B. Table joins
- [ ] C. Missing values only
- [ ] D. Query sorting

**Correct answer: A**

---

### 40. Can a table have more than one unique constraint?

- [ ] A. Only for numeric columns
- [ ] B. Only if it has no primary key
- [ ] C. Yes
- [ ] D. No

**Correct answer: C**

---

### 41. How many primary keys can a table have?

- [ ] A. Unlimited
- [ ] B. One per column
- [ ] C. Zero or one
- [ ] D. Exactly two

**Correct answer: C**

---


### 42. What does a foreign key connect?

- [ ] A. A query to an alias
- [ ] B. A child table to a parent table
- [ ] C. A broader condition than required
- [ ] D. A column to a function

**Correct answer: B**

---

### 43. What is referential integrity?

- [ ] A. Sorting rows correctly
- [ ] B. Removing all duplicate names
- [ ] C. Encrypting table data
- [ ] D. Keeping relationships between tables valid

**Correct answer: D**

---

### 44. What is a one-to-many relationship?

- [ ] A. One table cannot reference another table
- [ ] B. One row in a parent table can connect to many rows in a child table
- [ ] C. Every row connects only to itself
- [ ] D. Many rows must have the same primary key

**Correct answer: B**

---

### 45. Which is an example of a one-to-many relationship?

- [ ] A. Customers to Orders
- [ ] B. Orders to Customers only
- [ ] C. Products to Suppliers directly without a junction table
- [ ] D. Categories to themselves only

**Correct answer: A**

---


### 46. What is a many-to-many relationship?

- [ ] A. One row can relate only to one row
- [ ] B. One table has no keys
- [ ] C. A table stores repeated groups
- [ ] D. Many rows in table A can relate to many rows in table B

**Correct answer: D**

---

### 47. Which example represents a many-to-many relationship?

- [ ] A. Orders and OrderItems only
- [ ] B. Products and Suppliers
- [ ] C. Customers and Orders only
- [ ] D. Customers and Addresses only

**Correct answer: B**

---

### 48. How is a many-to-many relationship implemented in relational databases?

- [ ] A. By storing comma-separated values
- [ ] B. By duplicating columns
- [ ] C. By using a junction (joint) table
- [ ] D. By removing primary keys

**Correct answer: C**

---

### 49. What is normalization?

- [ ] A. Sorting data alphabetically
- [ ] B. Deleting old records
- [ ] C. Organizing data into related tables to reduce duplication and improve integrity
- [ ] D. Backing up the database

**Correct answer: C**

---

### 50. What does Second Normal Form require?

- [ ] A. Every column must be nullable
- [ ] B. Every row must contain duplicated data
- [ ] C. Every table must have exactly two columns
- [ ] D. Every non-key column depends on the whole primary key

**Correct answer: D**

---


### 51. What does a `NOT NULL` constraint require?

- [ ] A. The column must be a primary key
- [ ] B. The column must reference another table
- [ ] C. The column must always be unique
- [ ] D. The column must have a value

**Correct answer: D**

---

### 52. Why is scanning a large table often slow?

- [ ] A. SQL queries cannot filter rows
- [ ] B. Tables cannot contain indexes
- [ ] C. the database system cannot read rows
- [ ] D. The database must inspect a large part of the table

**Correct answer: D**

---

### 53. What is an index?

- [ ] A. An additional data structure maintained by the database
- [ ] B. A full scan of the table
- [ ] C. A replacement for the table
- [ ] D. A type of network node

**Correct answer: A**

---

### 54. Which simplified explanation of an index is correct?

- [ ] A. A deleted copy of old rows
- [ ] B. A random copy of the whole database
- [ ] C. A sorted copy of part of table data that helps find rows quickly
- [ ] D. A tool for encrypting network traffic

**Correct answer: C**

---

### 55. What does an index store?

- [ ] A. Only table permissions
- [ ] B. Selected column values and row locators
- [ ] C. A full scan of the table
- [ ] D. Only query history

**Correct answer: B**

---

### 56. Why does an index use physical storage?

- [ ] A. It deletes table pages
- [ ] B. It removes row locators
- [ ] C. It creates additional pages on disk
- [ ] D. It replaces RAM

**Correct answer: C**

---

### 57. Which is a cost of having indexes?

- [ ] A. No maintenance
- [ ] B. Extra disk space
- [ ] C. Faster inserts always
- [ ] D. No memory usage

**Correct answer: B**

---

### 58. Many relational database indexes are commonly implemented using which family of structures?

- [ ] A. B-tree or B+tree structures
- [ ] B. Stacks only
- [ ] C. Queues only
- [ ] D. Unsorted arrays only

**Correct answer: A**

---

### 59. Which question belongs to a good index strategy?

- [ ] A. Which table name is longest?
- [ ] B. Which queries are frequent and performance-critical?
- [ ] C. A full scan of the table
- [ ] D. A hash-based lookup when equality is required

**Correct answer: B**

---

### 60. Which query part is important for index design?

- [ ] A. Columns used in `WHERE`
- [ ] B. Comments only
- [ ] C. White space only
- [ ] D. A full scan of the table

**Correct answer: A**

---

### 61. What is the main tradeoff of indexes?

- [ ] A. Better networking but worse SQL syntax
- [ ] B. Faster reads but more storage and slower writes
- [ ] C. Faster writes but slower reads always
- [ ] D. No storage but high latency

**Correct answer: B**

---

### 62. What is a distributed system?

- [ ] A. One SQL query with many columns
- [ ] B. One table with many indexes
- [ ] C. One computer with a large monitor
- [ ] D. Multiple computers working together and appearing as one system

**Correct answer: D**

---

### 63. What is a node?

- [ ] A. A table row only
- [ ] B. One participating machine or process in a distributed system
- [ ] C. A B-tree key only
- [ ] D. A SQL column

**Correct answer: B**

---

### 64. A ping time of 24 ms means what?

- [ ] A. The round trip took about 24 milliseconds
- [ ] B. The server has 24 rows
- [ ] C. The network has 24 shards
- [ ] D. The database has 24 indexes

**Correct answer: A**

---

### 65. What is bandwidth?

- [ ] A. How many indexes a table has
- [ ] B. How much data can be transferred per second
- [ ] C. How many nodes are down
- [ ] D. How long a query waits in a lock

**Correct answer: B**

---

### 66. How are latency and bandwidth different?

- [ ] A. Both are the database system constraints
- [ ] B. They mean exactly the same thing
- [ ] C. Bandwidth is delay; latency is disk space
- [ ] D. Latency is delay; bandwidth is transfer capacity per second

**Correct answer: D**

---

### 67. What does the truck full of hard drives example illustrate?

- [ ] A. Index seek behavior
- [ ] B. Low bandwidth and low latency
- [ ] C. Clustered index design
- [ ] D. High bandwidth but very high latency

**Correct answer: D**

---

### 68. What is packet loss?

- [ ] A. SQL rows are deleted automatically
- [ ] B. Tables are replicated synchronously
- [ ] C. Network packets can be lost and may need retransmission
- [ ] D. Index pages are compressed

**Correct answer: C**

---

### 69. What is congestion?

- [ ] A. Too many aliases in a query
- [ ] B. Too much traffic on a network path causing slowdown
- [ ] C. Too many columns in a table
- [ ] D. Too few primary keys

**Correct answer: B**

---

### 70. What is big data according to the lecture?

- [ ] A. Any database with text columns
- [ ] B. A system of data processing where the amount of data could not fit into a single node
- [ ] C. Any system with a website
- [ ] D. Any table with more than ten rows

**Correct answer: B**

---

### 71. What is availability?

- [ ] A. All queries use `SELECT *`
- [ ] B. The system continues to work when some parts fail
- [ ] C. All indexes are clustered
- [ ] D. Every row has a primary key

**Correct answer: B**

---

### 72. What happens if a single-server system fails?

- [ ] A. The whole service may become unavailable
- [ ] B. All indexes become covering indexes
- [ ] C. The database becomes distributed automatically
- [ ] D. Availability always increases

**Correct answer: A**

---

### 73. What is one reason for replication?

- [ ] A. Removing all storage
- [ ] B. Preventing all reads
- [ ] C. Availability
- [ ] D. Making all writes disappear

**Correct answer: C**

---

### 74 What is geo-distribution?

- [ ] A. Creating indexes by geography only
- [ ] B. Sorting rows by country
- [ ] C. Removing regional users
- [ ] D. Placing nodes in different geographic locations

**Correct answer: D**

---

### 75. Why can geo-distribution reduce latency?

- [ ] A. SQL queries become shorter
- [ ] B. Tables disappear
- [ ] C. Users can be closer to servers
- [ ] D. Indexes become smaller automatically

**Correct answer: C**

---

### 76. Which is a benefit of geo-distribution?

- [ ] A. One node stores all data only
- [ ] B. No network communication is needed
- [ ] C. All consistency problems disappear
- [ ] D. Service can survive regional failures

**Correct answer: D**

---

### 77. Why does geo-distribution make consistency harder?

- [ ] A. Data changes must be propagated between distant locations
- [ ] B. the database system cannot compare strings
- [ ] C. Servers cannot store data
- [ ] D. Indexes cannot be used

**Correct answer: A**

---

### 78. What is redundancy?

- [ ] A. Storing or running extra copies so failure does not destroy the system
- [ ] B. Removing all backup copies
- [ ] C. Creating invalid foreign keys
- [ ] D. Storing one copy only

**Correct answer: A**

---

### 79. What question does redundancy create?

- [ ] A. How do we avoid using networks?
- [ ] B. How do we keep all copies correct?
- [ ] C. How do we delete all rows?
- [ ] D. How do we remove all users?

**Correct answer: B**

---

### 80. What is the central problem of distributed data?

- [ ] A. Indexes cannot be sorted
- [ ] B. SQL cannot filter rows
- [ ] C. Tables cannot have rows
- [ ] D. A write on one node may not be immediately visible on another node

**Correct answer: D**

---

### 81. What does the CAP theorem discuss?

- [ ] A. How to design B-tree pages
- [ ] B. How to format SQL keywords
- [ ] C. Tradeoffs in distributed data systems during network partitions
- [ ] D. How to write a row-limiting query

**Correct answer: C**

---

### 82. What does C mean in CAP?

- [ ] A. Caching only
- [ ] B. Capacity
- [ ] C. Compression
- [ ] D. Consistency

**Correct answer: D**

---

### 83. What does A mean in CAP?

- [ ] A. Aggregation
- [ ] B. Atomicity
- [ ] C. Authentication
- [ ] D. Availability

**Correct answer: D**

---

### 84. What does P mean in CAP?

- [ ] A. Packet speed
- [ ] B. Partition tolerance
- [ ] C. Primary key
- [ ] D. Page size

**Correct answer: B**

---

### 85. What does consistency mean in CAP?

- [ ] A. Every request always succeeds with any data
- [ ] B. Every read receives the latest write or an error
- [ ] C. Every index is clustered
- [ ] D. Every database has one table

**Correct answer: B**

---

### 86. What does availability mean in CAP?

- [ ] A. Every table has a clustered index
- [ ] B. Every request receives a response
- [ ] C. Every read receives the latest write only
- [ ] D. Every network packet is encrypted

**Correct answer: B**

---

### 87. What does partition tolerance mean?

- [ ] A. The system continues operating despite communication failure between nodes
- [ ] B. The table is divided into columns
- [ ] C. The query uses `PARTITION BY` only
- [ ] D. The database has no failures

**Correct answer: A**

---

### 88. What is the real CAP choice during a network partition?

- [ ] A. Indexes versus tables
- [ ] B. Memory versus CPU only
- [ ] C. Consistency versus availability
- [ ] D. SQL versus NoSQL only

**Correct answer: C**


---

### 89. Traditional single-node RDBMS usually prioritizes what?

- [ ] A. Eventual inconsistency
- [ ] B. Random writes
- [ ] C. Network partition tolerance inside one node
- [ ] D. Consistency

**Correct answer: D**

---

### 90. Why is CAP not the main issue for a single database node?

- [ ] A. There is no distributed network partition inside one standalone node
- [ ] B. A single node cannot provide consistency
- [ ] C. Indexes remove all availability problems
- [ ] D. Single-node systems cannot store durable data

**Correct answer: A**

---

### 91. When do CAP tradeoffs appear for relational databases?

- [ ] A. When `SELECT *` is used
- [ ] B. When an index is created
- [ ] C. When they are distributed through replication
- [ ] D. When a table has a primary key

**Correct answer: C**

---

### 92. What is replication?

- [ ] A. Storing copies of the same data on multiple nodes
- [ ] B. Removing all data copies
- [ ] C. Splitting different data across nodes only
- [ ] D. Creating a SQL alias

**Correct answer: A**

---

### 93. Which is a reason to replicate data?

- [ ] A. Fault tolerance
- [ ] B. Removing all read capacity
- [ ] C. Increasing write conflicts intentionally
- [ ] D. Making one copy only

**Correct answer: A**


---

### 94. In main-follower replication, which node accepts writes?

- [ ] A. Every follower independently
- [ ] B. No node
- [ ] C. Main node
- [ ] D. Follower only

**Correct answer: C**


---

### 95. Which type of application often benefits from read replicas?

- [ ] A. Applications with only network partitions
- [ ] B. Applications with no reads
- [ ] C. Applications with no data
- [ ] D. Applications with many more reads than writes

**Correct answer: D**

---

### 96. What is replication lag?

- [ ] A. Difference between clustered and nonclustered indexes
- [ ] B. Delay between a write on main and the same data appearing on follower
- [ ] C. Delay between typing and saving a SQL file
- [ ] D. Number of keys in a B-tree page

**Correct answer: B**

---

### 97. What can happen during replication lag?

- [ ] A. A follower always has the latest data
- [ ] B. The main cannot accept writes
- [ ] C. Indexes disappear
- [ ] D. A follower may return old data

**Correct answer: D**


---

### 98. Replication copies what?

- [ ] A. Same data to many nodes
- [ ] B. Different data to each node only
- [ ] C. Only indexes
- [ ] D. Only query text

**Correct answer: A**

---

### 99. What is partitioning?

- [ ] A. Creating only primary keys
- [ ] B. Copying all data to every node only
- [ ] C. Running `ping`
- [ ] D. Dividing data into parts

**Correct answer: D**


---

### 100. Large systems often use which combination?

- [ ] A. No replication and no sharding
- [ ] B. Only one server forever
- [ ] C. Replication plus sharding
- [ ] D. Only table scans

**Correct answer: C**

---

### 101. What does replication plus sharding provide?

- [ ] A. No complexity
- [ ] B. No need for failover
- [ ] C. No need for routing
- [ ] D. Capacity from sharding and availability/read scalability from replication

**Correct answer: D**

---

### 102. What is majority quorum?

- [ ] A. Majority of nodes required for a decision
- [ ] B. All indexes in a database
- [ ] C. All SQL commands in a script
- [ ] D. All rows in a table

**Correct answer: A**

---

### 103. What is the majority formula for distributed systems?

- [ ] A. `N - 2`
- [ ] B. `N * 2`
- [ ] C. `floor(N / 2) + 1`
- [ ] D. `N / 10`

**Correct answer: C**

---

### 104. In a 3-node cluster, if Node A is alone after partition, can it make majority decisions?

- [ ] A. Only if it has an index
- [ ] B. Only if it is a follower
- [ ] C. Yes, always
- [ ] D. No

**Correct answer: D**


