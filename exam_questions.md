# SQL SELECT Theory — 100 Single-Answer MCQ Questions

## Multiple Choice Questions

### 1. What is the main purpose of the `SELECT` statement in SQL?

A. To delete rows from a table
B. To retrieve data from a table
C. To create a new database
D. To change table structure

**Correct answer: B**

---

### 2. Which clause specifies the table from which data is retrieved?

A. `WHERE`
B. `ORDER BY`
C. `FROM`
D. `GROUP BY`

**Correct answer: C**

---

### 3. Which clause is used to filter rows before they are returned?

A. `WHERE`
B. `SELECT`
C. `ORDER BY`
D. `DISTINCT`

**Correct answer: A**

---

### 4. Which clause is used to sort query results?

A. `WHERE`
B. `ORDER BY`
C. `HAVING`
D. `FROM`

**Correct answer: B**

---

### 5. What does `ORDER BY OrderTotal DESC` do?

A. Sorts order totals from smallest to largest
B. Sorts order totals from largest to smallest
C. Removes duplicate order totals
D. Filters only expensive orders

**Correct answer: B**

---

### 6. Which operator is best for checking whether a value matches one value from a list?

A. `BETWEEN`
B. `LIKE`
C. `IN`
D. `IS NULL`

**Correct answer: C**

---

### 7. Which query condition finds orders with status `Delivered`, `Shipped`, or `Processing`?

A. `OrderStatus BETWEEN Delivered AND Processing`
B. `OrderStatus IN (N'Delivered', N'Shipped', N'Processing')`
C. `OrderStatus LIKE N'Delivered, Shipped, Processing'`
D. `OrderStatus IS NOT NULL (Delivered, Shipped, Processing)`

**Correct answer: B**

---

### 8. Which operator is the opposite of `IN`?

A. `NO IN`
B. `NOT IN`
C. `IN NOT`
D. `EXCEPT IN`

**Correct answer: B**

---

### 9. What is a common danger when using `NOT IN`?

A. It cannot compare strings
B. It always ignores indexes
C. It may behave unexpectedly if the list contains `NULL`
D. It only works with dates

**Correct answer: C**

---

### 10. Which condition correctly finds orders not having statuses `Cancelled`, `Returned`, or `Refunded`?

A. `OrderStatus NOT IN (N'Cancelled', N'Returned', N'Refunded')`
B. `OrderStatus != IN (N'Cancelled', N'Returned', N'Refunded')`
C. `OrderStatus NOT BETWEEN N'Cancelled' AND N'Refunded'`
D. `OrderStatus IS NOT (N'Cancelled', N'Returned', N'Refunded')`

**Correct answer: A**

---

### 11. What does the `BETWEEN` operator check?

A. Whether a value is equal to one item in a list
B. Whether a value is inside an inclusive range
C. Whether text matches a pattern
D. Whether a value is missing

**Correct answer: B**

---

### 12. What does `OrderTotal BETWEEN 100 AND 500` mean?

A. `OrderTotal > 100 AND OrderTotal < 500`
B. `OrderTotal >= 100 AND OrderTotal <= 500`
C. `OrderTotal = 100 OR OrderTotal = 500`
D. `OrderTotal < 100 OR OrderTotal > 500`

**Correct answer: B**

---

### 13. Is `BETWEEN` inclusive?

A. Yes, it includes both boundary values
B. No, it excludes both boundary values
C. It includes only the lower boundary
D. It includes only the upper boundary

**Correct answer: A**

---

### 14. Which condition finds orders outside the range 100 to 1000?

A. `OrderTotal BETWEEN NOT 100 AND 1000`
B. `OrderTotal NOT BETWEEN 100 AND 1000`
C. `OrderTotal OUTSIDE 100 AND 1000`
D. `OrderTotal != BETWEEN 100 AND 1000`

**Correct answer: B**

---

### 15. Why can `BETWEEN` be dangerous with `DATETIME` values?

A. Because dates cannot be compared
B. Because time is included in the value
C. Because SQL Server does not support date ranges
D. Because `BETWEEN` works only with strings

**Correct answer: B**

---

### 16. Which date condition is usually safer for a full January range with `DATETIME`?

A. `CreatedAt BETWEEN '2026-01-01' AND '2026-01-31'`
B. `CreatedAt = '2026-01-31'`
C. `CreatedAt >= '2026-01-01' AND CreatedAt < '2026-02-01'`
D. `CreatedAt LIKE '2026-01%'`

**Correct answer: C**

---

### 17. What is the main purpose of `LIKE`?

A. Numeric comparison
B. Date calculation
C. Pattern matching in text
D. Grouping rows

**Correct answer: C**

---

### 18. What does `%` mean in a `LIKE` pattern?

A. Exactly one character
B. Any number of characters
C. A numeric percentage only
D. A missing value

**Correct answer: B**

---

### 19. What does `_` mean in a `LIKE` pattern?

A. Any number of characters
B. Exactly one character
C. No character
D. A space only

**Correct answer: B**

---

### 20. Which condition finds product names containing `SQL`?

A. `ProductName LIKE N'%SQL%'`
B. `ProductName LIKE N'SQL'`
C. `ProductName IN N'SQL'`
D. `ProductName BETWEEN N'SQL' AND N'SQL'`

**Correct answer: A**

---

### 21. Which condition finds customer names starting with `Nino`?

A. `CustomerName LIKE N'%Nino'`
B. `CustomerName LIKE N'Nino%'`
C. `CustomerName LIKE N'%Nino%'`
D. `CustomerName = N'%Nino%'`

**Correct answer: B**

---

### 22. Which condition finds emails ending with `@example.com`?

A. `CustomerEmail LIKE '%@example.com'`
B. `CustomerEmail LIKE '@example.com%'`
C. `CustomerEmail = '%@example.com'`
D. `CustomerEmail IN '@example.com'`

**Correct answer: A**

---

### 23. Which `LIKE` pattern matches country codes starting with `G` and having exactly one more character?

A. `'G%'`
B. `'%G'`
C. `'G_'`
D. `'_G'`

**Correct answer: C**

---

### 24. What does `[A-D]%` mean in a SQL Server `LIKE` pattern?

A. Text ending with A, B, C, or D
B. Text starting with A, B, C, or D
C. Text containing only A and D
D. Text containing the exact string `[A-D]`

**Correct answer: B**

---

### 25. Which condition finds products not related to SQL?

A. `ProductName NOT LIKE N'%SQL%'`
B. `ProductName LIKE NOT N'%SQL%'`
C. `ProductName != LIKE N'%SQL%'`
D. `ProductName NOT IN LIKE N'%SQL%'`

**Correct answer: A**

---

### 26. Which `LIKE` pattern is usually more index-friendly?

A. `CustomerName LIKE N'%Nino%'`
B. `CustomerName LIKE N'Nino%'`
C. `CustomerName LIKE N'%ino'`
D. `CustomerName LIKE N'%Ni%'`

**Correct answer: B**

---

### 27. What does `NULL` mean in SQL?

A. Zero
B. Empty string only
C. Unknown, missing, or not applicable
D. False

**Correct answer: C**

---

### 28. Which condition correctly checks for missing delivery date?

A. `DeliveredAt = NULL`
B. `DeliveredAt IS NULL`
C. `DeliveredAt == NULL`
D. `DeliveredAt LIKE NULL`

**Correct answer: B**

---

### 29. Which condition correctly checks that a value is not missing?

A. `IS NOT NULL`
B. `!= NULL`
C. `NOT = NULL`
D. `EXISTS NULL`

**Correct answer: A**

---

### 30. Why is `DeliveredAt = NULL` wrong?

A. `NULL` must be checked with `IS NULL`
B. Dates cannot contain nulls
C. SQL Server does not allow `DeliveredAt` in `WHERE`
D. `=` works only with strings

**Correct answer: A**

---

### 31. Which function replaces `NULL` with a specified value in SQL Server?

A. `REPLACENULL()`
B. `ISNULL()`
C. `NOTNULL()`
D. `NULLVALUE()`

**Correct answer: B**

---

### 32. What does `COALESCE()` return?

A. The last value in a list
B. The first non-null value
C. Only numeric values
D. Only missing values

**Correct answer: B**

---

### 33. What is the purpose of `DISTINCT`?

A. To sort rows
B. To remove duplicate rows from the result
C. To group rows after aggregation
D. To filter rows by condition

**Correct answer: B**

---

### 34. What does `SELECT DISTINCT CountryCode` return?

A. All country values including duplicates
B. Unique country values
C. Only countries with many orders
D. Countries sorted by revenue

**Correct answer: B**

---

### 35. What does `SELECT DISTINCT CountryCode, City` return?

A. Unique countries only
B. Unique cities only
C. Unique country-city combinations
D. All rows without filtering

**Correct answer: C**

---

### 36. Does `DISTINCT` apply only to the first selected column?

A. Yes
B. No, it applies to the entire selected row
C. Only when used with `ORDER BY`
D. Only when used with `GROUP BY`

**Correct answer: B**

---

### 37. What happens if a query has no `ORDER BY`?

A. SQL Server guarantees alphabetical order
B. SQL Server guarantees insertion order
C. SQL Server does not guarantee row order
D. The query is invalid

**Correct answer: C**

---

### 38. What does `ASC` mean in `ORDER BY`?

A. Ascending order
B. Automatic search condition
C. Aggregate sort calculation
D. Alias sort column

**Correct answer: A**

---

### 39. What does `DESC` mean in `ORDER BY`?

A. Describe table
B. Descending order
C. Delete selected column
D. Distinct search

**Correct answer: B**

---

### 40. What does this sorting do: `ORDER BY ProductCategory ASC, OrderTotal DESC`?

A. Sorts only by order total
B. Sorts by category alphabetically, then by total descending inside each category
C. Sorts randomly
D. Groups the rows permanently

**Correct answer: B**

---

### 41. Can SQL Server sort by a calculated expression?

A. Yes
B. No
C. Only inside `WHERE`
D. Only inside `HAVING`

**Correct answer: A**

---

### 42. Can SQL Server sort by an alias from the `SELECT` list?

A. Yes
B. No
C. Only with `DISTINCT`
D. Only with `GROUP BY`

**Correct answer: A**

---

### 43. In SQL Server, where do `NULL` values appear in ascending sort order by default?

A. First
B. Last
C. Randomly
D. They are removed

**Correct answer: A**

---

### 44. Which clause is commonly used with `TOP` to get the most expensive orders?

A. `GROUP BY`
B. `ORDER BY OrderTotal DESC`
C. `WHERE OrderTotal IS NULL`
D. `HAVING OrderTotal DESC`

**Correct answer: B**

---

### 45. Which SQL Server syntax is used for pagination?

A. `SKIP` and `TAKE`
B. `OFFSET` and `FETCH`
C. `PAGE` and `SIZE`
D. `LIMIT` and `OFFSET` only

**Correct answer: B**

---

### 46. What does `ANY` mean?

A. True if comparison is true for at least one value from the subquery
B. True only if comparison is true for all values
C. True only if the subquery is empty
D. True only if values are null

**Correct answer: A**

---

### 47. Which keyword is equivalent to `ANY` in SQL Server?

A. `EVERY`
B. `SOME`
C. `ONE`
D. `EACH`

**Correct answer: B**

---

### 48. What does `OrderTotal > ANY (subquery)` mean?

A. Order total is greater than every value returned by the subquery
B. Order total is greater than at least one value returned by the subquery
C. Order total equals all values returned by the subquery
D. Order total is null

**Correct answer: B**

---

### 49. Which operator is similar to `= ANY (subquery)`?

A. `IN (subquery)`
B. `BETWEEN (subquery)`
C. `LIKE (subquery)`
D. `IS NULL`

**Correct answer: A**

---

### 50. What does `ALL` mean?

A. True if comparison is true for at least one value
B. True only if comparison is true for every value
C. True only for duplicate values
D. True only for text columns

**Correct answer: B**

---

### 51. What does `OrderTotal > ALL (subquery)` mean?

A. Order total is greater than at least one returned value
B. Order total is greater than every returned value
C. Order total is equal to all returned values
D. Order total is inside a text pattern

**Correct answer: B**

---

### 52. Which is stricter?

A. `ANY`
B. `ALL`
C. `LIKE`
D. `DISTINCT`

**Correct answer: B**

---

### 53. Which aggregate function counts rows?

A. `SUM()`
B. `COUNT()`
C. `AVG()`
D. `MAX()`

**Correct answer: B**

---

### 54. Which aggregate function adds numeric values?

A. `SUM()`
B. `MIN()`
C. `COUNT()`
D. `LEN()`

**Correct answer: A**

---

### 55. Which aggregate function calculates the average?

A. `COUNT()`
B. `AVG()`
C. `MAX()`
D. `ROUND()`

**Correct answer: B**

---

### 56. Which aggregate function finds the smallest value?

A. `MIN()`
B. `MAX()`
C. `SUM()`
D. `AVG()`

**Correct answer: A**

---

### 57. Which aggregate function finds the largest value?

A. `MIN()`
B. `MAX()`
C. `COUNT()`
D. `LOWER()`

**Correct answer: B**

---

### 58. What does `COUNT(*)` count?

A. Only non-null values in one column
B. All rows
C. Only distinct rows
D. Only text values

**Correct answer: B**

---

### 59. What does `COUNT(SatisfactionScore)` count?

A. All rows
B. Only rows where `SatisfactionScore` is not null
C. Only rows where `SatisfactionScore` is zero
D. Only distinct satisfaction scores

**Correct answer: B**

---

### 60. What does `COUNT(DISTINCT CustomerID)` count?

A. All orders
B. Unique customers
C. Duplicate customers
D. Null customer IDs only

**Correct answer: B**

---

### 61. What happens to `NULL` values in `AVG()`?

A. They are treated as zero
B. They are ignored
C. They cause an error
D. They are counted twice

**Correct answer: B**

---

### 62. Which query returns total revenue?

A. `SELECT COUNT(OrderTotal) FROM Training.CustomerOrders;`
B. `SELECT SUM(OrderTotal) FROM Training.CustomerOrders;`
C. `SELECT AVG(OrderTotal) FROM Training.CustomerOrders;`
D. `SELECT MIN(OrderTotal) FROM Training.CustomerOrders;`

**Correct answer: B**

---

### 63. Which query returns the highest order total?

A. `SELECT MAX(OrderTotal) FROM Training.CustomerOrders;`
B. `SELECT MIN(OrderTotal) FROM Training.CustomerOrders;`
C. `SELECT SUM(OrderTotal) FROM Training.CustomerOrders;`
D. `SELECT COUNT(OrderTotal) FROM Training.CustomerOrders;`

**Correct answer: A**

---

### 64. What is the purpose of `GROUP BY`?

A. To sort rows alphabetically
B. To group rows with the same values for aggregation
C. To remove all nulls
D. To delete duplicate rows

**Correct answer: B**

---

### 65. Which clause is usually used together with aggregate functions?

A. `GROUP BY`
B. `LIKE`
C. `IS NULL`
D. `OFFSET`

**Correct answer: A**

---

### 66. Which query structure is correct for revenue by category?

A. `SELECT ProductCategory, SUM(OrderTotal) FROM Training.CustomerOrders GROUP BY ProductCategory;`
B. `SELECT ProductCategory, SUM(OrderTotal) FROM Training.CustomerOrders WHERE ProductCategory;`
C. `SELECT ProductCategory, SUM(OrderTotal) FROM Training.CustomerOrders ORDER BY ProductCategory;`
D. `SELECT ProductCategory, SUM(OrderTotal) FROM Training.CustomerOrders DISTINCT ProductCategory;`

**Correct answer: A**

---

### 67. When grouping by multiple columns, what happens?

A. SQL Server groups by only the first column
B. SQL Server groups by unique combinations of those columns
C. SQL Server ignores aggregate functions
D. SQL Server returns only one row

**Correct answer: B**

---

### 68. Which clause filters grouped results?

A. `WHERE`
B. `HAVING`
C. `ORDER BY`
D. `SELECT`

**Correct answer: B**

---

### 69. Which clause filters individual rows before grouping?

A. `WHERE`
B. `HAVING`
C. `GROUP BY`
D. `COUNT`

**Correct answer: A**

---

### 70. Which clause filters groups after aggregation?

A. `WHERE`
B. `HAVING`
C. `FROM`
D. `DISTINCT`

**Correct answer: B**

---

### 71. Which condition is valid for filtering categories with revenue above 5000?

A. `WHERE SUM(OrderTotal) > 5000`
B. `HAVING SUM(OrderTotal) > 5000`
C. `ORDER BY SUM(OrderTotal) > 5000`
D. `GROUP BY SUM(OrderTotal) > 5000`

**Correct answer: B**

---

### 72. Why is `WHERE SUM(OrderTotal) > 1000` invalid?

A. Aggregate functions cannot be used in `WHERE`
B. `WHERE` cannot compare numbers
C. `SUM()` works only with dates
D. `WHERE` must always be after `GROUP BY`

**Correct answer: A**

---

### 73. What is the correct logical meaning of using both `WHERE` and `HAVING`?

A. `HAVING` filters rows first, then `WHERE` filters groups
B. `WHERE` filters rows first, then `HAVING` filters groups
C. Both filter only individual rows
D. Both filter only selected columns

**Correct answer: B**

---

### 74. Which function rounds a number?

A. `ROUND()`
B. `LEN()`
C. `LEFT()`
D. `DATEADD()`

**Correct answer: A**

---

### 75. Which function rounds upward?

A. `FLOOR()`
B. `CEILING()`
C. `ABS()`
D. `SIGN()`

**Correct answer: B**

---

### 76. Which function rounds downward?

A. `CEILING()`
B. `FLOOR()`
C. `POWER()`
D. `SQRT()`

**Correct answer: B**

---

### 77. Which function returns an absolute value?

A. `ABS()`
B. `AVG()`
C. `LEN()`
D. `TRIM()`

**Correct answer: A**

---

### 78. Which function calculates a power?

A. `POWER()`
B. `SQRT()`
C. `ROUND()`
D. `SIGN()`

**Correct answer: A**

---

### 79. Which function calculates a square root?

A. `ABS()`
B. `SQRT()`
C. `FLOOR()`
D. `RAND()`

**Correct answer: B**

---

### 80. Which function returns -1, 0, or 1 depending on a number’s sign?

A. `SIGN()`
B. `RAND()`
C. `ROUND()`
D. `CEILING()`

**Correct answer: A**

---

### 81. Which function returns the length of text?

A. `LEN()`
B. `LEFT()`
C. `LOWER()`
D. `CONCAT()`

**Correct answer: A**

---

### 82. Which function returns characters from the beginning of a string?

A. `RIGHT()`
B. `LEFT()`
C. `SUBSTRING()`
D. `CHARINDEX()`

**Correct answer: B**

---

### 83. Which function returns characters from the end of a string?

A. `LEFT()`
B. `RIGHT()`
C. `UPPER()`
D. `TRIM()`

**Correct answer: B**

---

### 84. Which function extracts part of a string?

A. `SUBSTRING()`
B. `SUM()`
C. `DATEADD()`
D. `EOMONTH()`

**Correct answer: A**

---

### 85. Which function finds the position of text inside another text?

A. `CHARINDEX()`
B. `REPLACE()`
C. `CONCAT()`
D. `LOWER()`

**Correct answer: A**

---

### 86. Which function replaces text inside a string?

A. `REPLACE()`
B. `SUBSTRING()`
C. `COUNT()`
D. `DATEDIFF()`

**Correct answer: A**

---

### 87. Which function converts text to uppercase?

A. `LOWER()`
B. `UPPER()`
C. `TRIM()`
D. `CONCAT()`

**Correct answer: B**

---

### 88. Which function converts text to lowercase?

A. `UPPER()`
B. `LOWER()`
C. `LEFT()`
D. `RIGHT()`

**Correct answer: B**

---

### 89. Which function removes spaces from both sides of a string?

A. `TRIM()`
B. `LEN()`
C. `CONCAT()`
D. `CHARINDEX()`

**Correct answer: A**

---

### 90. Which function joins strings together?

A. `CONCAT()`
B. `COUNT()`
C. `SUM()`
D. `DATEPART()`

**Correct answer: A**

---

### 91. Which function returns the current local date and time?

A. `GETDATE()`
B. `SYSUTCDATETIME()`
C. `EOMONTH()`
D. `DATEDIFF()`

**Correct answer: A**

---

### 92. Which function returns the current UTC date and time?

A. `GETDATE()`
B. `SYSUTCDATETIME()`
C. `DATEADD()`
D. `DATENAME()`

**Correct answer: B**

---

### 93. Which function adds an interval to a date?

A. `DATEADD()`
B. `DATEDIFF()`
C. `YEAR()`
D. `EOMONTH()`

**Correct answer: A**

---

### 94. Which function calculates the difference between two dates?

A. `DATEADD()`
B. `DATEDIFF()`
C. `DATENAME()`
D. `MONTH()`

**Correct answer: B**

---

### 95. Which function extracts the year from a date?

A. `YEAR()`
B. `MONTH()`
C. `DAY()`
D. `EOMONTH()`

**Correct answer: A**

---

### 96. Which function extracts a specific date part such as hour?

A. `DATEPART()`
B. `CONCAT()`
C. `ROUND()`
D. `LEFT()`

**Correct answer: A**

---

### 97. Which function can return the weekday name?

A. `DATEDIFF()`
B. `DATENAME()`
C. `DATEADD()`
D. `SYSUTCDATETIME()`

**Correct answer: B**

---

### 98. Which function returns the end date of a month?

A. `EOMONTH()`
B. `DATEPART()`
C. `GETDATE()`
D. `DAY()`

**Correct answer: A**

---

### 99. Which condition finds risky orders according to the lecture-style examples?

A. `FraudRiskScore >= 7.0 OR IsPriority = 1`
B. `FraudRiskScore IS NULL AND IsPriority IS NULL`
C. `FraudRiskScore LIKE N'%risk%'`
D. `FraudRiskScore BETWEEN N'High' AND N'Low'`

**Correct answer: A**

---

### 100. In a final report grouped by country and customer segment, which clause should be used to keep only groups with more than 3 orders?

A. `WHERE COUNT(*) > 3`
B. `HAVING COUNT(*) > 3`
C. `ORDER BY COUNT(*) > 3`
D. `DISTINCT COUNT(*) > 3`

**Correct answer: B**


# Relational Database Theory, Normalization, Joins, and Constraints — 100 Single-Answer MCQ Questions

## Multiple Choice Questions

### 1. What does a relational database store data in?

A. Files only
B. Tables
C. Images
D. Procedures only

**Correct answer: B**

---

### 2. In a relational database, what does a table usually represent?

A. One type of entity
B. One SQL command
C. One backup file
D. One user session

**Correct answer: A**

---

### 3. Which of the following is an example of an entity?

A. `SELECT`
B. Customer
C. `JOIN`
D. `WHERE`

**Correct answer: B**

---

### 4. What do columns define in a table?

A. Individual records
B. Attributes
C. Foreign servers
D. Query results only

**Correct answer: B**

---

### 5. What do rows store in a table?

A. Individual records
B. Constraints only
C. Table names
D. SQL keywords

**Correct answer: A**

---

### 6. What is the relational theory term for a SQL table?

A. Tuple
B. Attribute
C. Relation
D. Domain

**Correct answer: C**

---

### 7. What is the relational theory term for a SQL row?

A. Tuple
B. Attribute
C. Relation
D. Domain

**Correct answer: A**

---

### 8. What is the relational theory term for a SQL column?

A. Tuple
B. Attribute
C. Relation
D. Constraint

**Correct answer: B**

---

### 9. What does a domain define in relational theory?

A. Table size
B. Allowed values or data type
C. Query order
D. Number of indexes

**Correct answer: B**

---

### 10. What is a candidate key?

A. A possible unique identifier
B. A duplicated column
C. A nullable text field
D. A temporary table

**Correct answer: A**

---

### 11. What is a primary key?

A. Any nullable column
B. The chosen unique identifier
C. A repeated value
D. A SQL Server login

**Correct answer: B**

---

### 12. What is a foreign key?

A. A key that references another table
B. A column that must contain duplicate values
C. A command for deleting rows
D. A type of string function

**Correct answer: A**

---

### 13. Which SQL Server command can inspect table metadata?

A. `EXEC sp_help 'dbo.Customers';`
B. `EXEC delete_table 'dbo.Customers';`
C. `RUN metadata dbo.Customers;`
D. `SHOW ALL ROWS dbo.Customers;`

**Correct answer: A**

---

### 14. Which system view can be used to inspect columns?

A. `INFORMATION_SCHEMA.COLUMNS`
B. `INFORMATION_SCHEMA.ROWS`
C. `SQL_SERVER.TABLE_DATA`
D. `dbo.ColumnList`

**Correct answer: A**

---

### 15. What does a unique constraint prevent?

A. Missing values only
B. Duplicate values in the constrained column or columns
C. Table joins
D. Query sorting

**Correct answer: B**

---

### 16. Can a table have more than one unique constraint?

A. Yes
B. No
C. Only if it has no primary key
D. Only for numeric columns

**Correct answer: A**

---

### 17. How many primary keys can a table have?

A. Zero or one
B. Exactly two
C. Unlimited
D. One per column

**Correct answer: A**

---

### 18. In the material, which customer column is unique?

A. `FirstName`
B. `LastName`
C. `Email`
D. `Phone`

**Correct answer: C**

---

### 19. What should happen when inserting a duplicate email into `Customers`?

A. SQL Server accepts it silently
B. SQL Server rejects the insert
C. SQL Server converts it to `NULL`
D. SQL Server creates a new table

**Correct answer: B**

---

### 20. What does this query check?

```sql
SELECT Email, COUNT(*) AS EmailCount
FROM dbo.Customers
GROUP BY Email
HAVING COUNT(*) > 1;
```

A. Customers with missing emails
B. Duplicate emails
C. Customers without orders
D. Orders with duplicate products

**Correct answer: B**

---

### 21. What does a foreign key connect?

A. A child table to a parent table
B. A database to a backup file
C. A query to an alias
D. A column to a function

**Correct answer: A**

---

### 22. In `Orders.CustomerID` referencing `Customers.CustomerID`, which table is the child table?

A. `Customers`
B. `Orders`
C. Both are parent tables
D. Neither table

**Correct answer: B**

---

### 23. What does a foreign key prevent?

A. Orders for nonexistent customers
B. All customer updates
C. All joins
D. All duplicate order totals

**Correct answer: A**

---

### 24. What is referential integrity?

A. Sorting rows correctly
B. Keeping relationships between tables valid
C. Removing all duplicate names
D. Encrypting table data

**Correct answer: B**

---

### 25. Which query pattern can find invalid child rows without matching parent rows?

A. `INNER JOIN` with no `WHERE`
B. `LEFT JOIN` and checking parent key `IS NULL`
C. `CROSS JOIN` only
D. `ORDER BY` only

**Correct answer: B**

---

### 26. In a valid foreign-key relationship, what should a query searching for orders with no matching customers return?

A. All rows
B. No rows
C. Only customers
D. Only duplicate emails

**Correct answer: B**

---

### 27. What is a one-to-many relationship?

A. One row in a parent table can connect to many rows in a child table
B. Every row connects only to itself
C. Many rows must have the same primary key
D. One table cannot reference another table

**Correct answer: A**

---

### 28. Which is an example of a one-to-many relationship?

A. Customers to Orders
B. Orders to Customers only
C. Products to Suppliers directly without a junction table
D. Categories to themselves only

**Correct answer: A**

---

### 29. Why use `LEFT JOIN` when counting orders per customer?

A. To show only customers with orders
B. To show customers even if they have zero orders
C. To delete customers without orders
D. To create a Cartesian product

**Correct answer: B**

---

### 30. Why should an order not store `Product1`, `Product2`, and `Product3` columns?

A. It limits the number of products and creates poor design
B. SQL Server cannot store text columns
C. Products cannot have names
D. Orders cannot have columns

**Correct answer: A**

---

### 31. Which table is used to store products inside an order?

A. `Customers`
B. `OrderItems`
C. `Addresses`
D. `Suppliers`

**Correct answer: B**

---

### 32. What relationship exists between `Orders` and `OrderItems`?

A. One-to-many
B. Many-to-one from orders to customers
C. One-to-one only
D. No relationship

**Correct answer: A**

---

### 33. Why is `OrderItems` useful?

A. It allows each order to contain any number of products
B. It prevents orders from having customers
C. It stores only customer emails
D. It replaces all foreign keys

**Correct answer: A**

---

### 34. What relationship exists between `Customers` and `Addresses`?

A. One-to-many
B. Many-to-many without a junction table
C. One-to-one only
D. Cross join

**Correct answer: A**

---

### 35. Which query condition can find customers with more than one address?

A. `HAVING COUNT(a.AddressID) > 1`
B. `WHERE COUNT(a.AddressID) > 1`
C. `ORDER BY COUNT(a.AddressID) > 1`
D. `JOIN COUNT(a.AddressID) > 1`

**Correct answer: A**

---

### 36. What is a many-to-many relationship?

A. Many rows in table A can relate to many rows in table B
B. One row can relate only to one row
C. One table has no keys
D. A table stores repeated groups

**Correct answer: A**

---

### 37. Which example represents a many-to-many relationship?

A. Products and Suppliers
B. Customers and Orders only
C. Orders and OrderItems only
D. Customers and Addresses only

**Correct answer: A**

---

### 38. How is a many-to-many relationship implemented in relational databases?

A. By using a junction table
B. By duplicating columns
C. By storing comma-separated values
D. By removing primary keys

**Correct answer: A**

---

### 39. In the material, which table is the junction table between products and suppliers?

A. `ProductSuppliers`
B. `OrderItems`
C. `Addresses`
D. `Customers`

**Correct answer: A**

---

### 40. What does `ProductSuppliers` connect?

A. Products and Suppliers
B. Customers and Orders
C. Orders and Addresses
D. Categories and Customers

**Correct answer: A**

---

### 41. What is normalization?

A. Organizing data into related tables to reduce duplication and improve integrity
B. Sorting data alphabetically
C. Backing up the database
D. Deleting old records

**Correct answer: A**

---

### 42. What does a normalized design try to do?

A. Store each fact once
B. Repeat data in every row
C. Avoid using keys
D. Store everything in one table

**Correct answer: A**

---

### 43. Where should customer email be stored in a normalized design?

A. In `Customers`
B. In every order row
C. In every order item row
D. In every product row

**Correct answer: A**

---

### 44. What is a problem with the bad `BadOrders` design?

A. It has repeating product columns
B. It has too many foreign keys
C. It has no text columns
D. It cannot store order IDs

**Correct answer: A**

---

### 45. Why is `Product1`, `Product2`, `Product3` a warning sign?

A. It shows repeating groups
B. It improves 3NF
C. It proves a correct many-to-many design
D. It guarantees referential integrity

**Correct answer: A**

---

### 46. What happens if an order has four products in the bad design?

A. The design does not handle it naturally
B. SQL Server automatically creates `Product4`
C. The order becomes a customer
D. The primary key changes automatically

**Correct answer: A**

---

### 47. What is First Normal Form mainly concerned with?

A. Atomic values and no repeating groups
B. Index compression
C. Password encryption
D. Backup scheduling

**Correct answer: A**

---

### 48. Which violates 1NF?

A. A `Products` column containing `Laptop, Mouse, Keyboard`
B. A separate `OrderItems` table
C. A primary key column
D. A foreign key column

**Correct answer: A**

---

### 49. What does “atomic values” mean in 1NF?

A. Each column contains a single indivisible value
B. Each table has no rows
C. Each row must be encrypted
D. Each database has one table

**Correct answer: A**

---

### 50. Which design is better for multiple products in an order?

A. `Orders`, `OrderItems`, and `Products`
B. `Product1`, `Product2`, `Product3` columns
C. One text column containing all products
D. One table without keys

**Correct answer: A**

---

### 51. What is required before a table can be in 2NF?

A. It must already be in 1NF
B. It must have no primary key
C. It must have only one column
D. It must have no foreign keys

**Correct answer: A**

---

### 52. What does Second Normal Form require?

A. Every non-key column depends on the whole primary key
B. Every column must be nullable
C. Every row must contain duplicated data
D. Every table must have exactly two columns

**Correct answer: A**

---

### 53. When does 2NF mostly matter?

A. When a table has a composite primary key
B. When a table has no rows
C. When a table has only one column
D. When using `ORDER BY`

**Correct answer: A**

---

### 54. In `ProductSuppliers(ProductID, SupplierID, SupplierSKU, SupplierPrice, LeadTimeDays)`, what is the composite primary key?

A. `(ProductID, SupplierID)`
B. `(SupplierSKU, SupplierPrice)`
C. `(ProductName, SupplierName)`
D. `(LeadTimeDays, SupplierPrice)`

**Correct answer: A**

---

### 55. In `ProductSuppliers`, which value properly depends on the combination of product and supplier?

A. `SupplierPrice`
B. `ProductName` only
C. `SupplierName` only
D. `CategoryName` only

**Correct answer: A**

---

### 56. Why is storing `ProductName` in `ProductSuppliers` a bad 2NF design?

A. It depends only on `ProductID`, not the full composite key
B. It depends on both `ProductID` and `SupplierID`
C. It is always null
D. It cannot be joined

**Correct answer: A**

---

### 57. Why is storing `SupplierName` in `ProductSuppliers` a bad 2NF design?

A. It depends only on `SupplierID`, not the full composite key
B. It depends on the full key
C. It is an aggregate
D. It is a date function

**Correct answer: A**

---

### 58. What is required before a table can be in 3NF?

A. It must already be in 2NF
B. It must have no columns
C. It must have repeated groups
D. It must use `CROSS JOIN`

**Correct answer: A**

---

### 59. What does Third Normal Form require?

A. Non-key columns do not depend on other non-key columns
B. All columns depend on duplicated strings
C. Tables contain comma-separated lists
D. Every table has no foreign keys

**Correct answer: A**

---

### 60. Why is this bad for 3NF: `OrderID | CustomerID | CustomerEmail | CustomerPhone`?

A. Customer email and phone depend on `CustomerID`, not directly on `OrderID`
B. `OrderID` cannot be stored
C. SQL Server cannot join orders and customers
D. Customer email must always be stored in orders

**Correct answer: A**

---

### 61. Which is the better 3NF design?

A. `Customers(CustomerID, Email, Phone)` and `Orders(OrderID, CustomerID, OrderDate)`
B. `Orders(OrderID, CustomerEmail, CustomerPhone)` only
C. `Orders(Product1, Product2, Product3)` only
D. One table with all data duplicated

**Correct answer: A**

---

### 62. What is an insert anomaly?

A. Inability to insert one type of data without unrelated data
B. Sorting rows incorrectly
C. Joining two tables
D. Filtering rows with `WHERE`

**Correct answer: A**

---

### 63. Which situation is an insert anomaly?

A. Cannot add a customer until they place an order
B. Cannot sort orders by date
C. Cannot use aliases
D. Cannot count rows

**Correct answer: A**

---

### 64. What is an update anomaly?

A. The same fact must be updated in many places
B. A query uses `ORDER BY`
C. A table has one primary key
D. A row has a foreign key

**Correct answer: A**

---

### 65. Which situation is an update anomaly?

A. Customer email repeated in many orders must be changed many times
B. A customer has one email in `Customers`
C. An order references a customer
D. A product has a category

**Correct answer: A**

---

### 66. What is a delete anomaly?

A. Deleting one record accidentally removes the only copy of another fact
B. A query deletes no rows
C. A join returns matching rows
D. A table has a unique constraint

**Correct answer: A**

---

### 67. What is a join?

A. A way to combine rows from two or more tables using a related column
B. A way to delete a table
C. A way to create a new data type
D. A way to remove all constraints

**Correct answer: A**

---

### 68. Most relational joins use which columns?

A. Primary key and foreign key columns
B. Only text columns
C. Only nullable columns
D. Only calculated columns

**Correct answer: A**

---

### 69. In the join `Orders o JOIN Customers c ON o.CustomerID = c.CustomerID`, what is `Orders.CustomerID`?

A. Foreign key
B. Primary key of `Customers`
C. Alias only
D. Aggregate function

**Correct answer: A**

---

### 70. In the join `Orders o JOIN Customers c ON o.CustomerID = c.CustomerID`, what is `Customers.CustomerID`?

A. Primary key
B. Foreign key of `Orders`
C. String function
D. Junction table

**Correct answer: A**

---

### 71. What does `INNER JOIN` return?

A. Rows where both tables have matching values
B. All rows from the left table only
C. All possible combinations
D. Only unmatched rows

**Correct answer: A**

---

### 72. When should `INNER JOIN` be used?

A. When only matching data is needed
B. When every possible combination is needed
C. When only missing data is needed
D. When no relationship exists

**Correct answer: A**

---

### 73. What does `LEFT JOIN` return?

A. All rows from the left table and matching rows from the right table
B. Only rows from the right table
C. Only matching rows from both tables
D. Every possible combination

**Correct answer: A**

---

### 74. In a `LEFT JOIN`, what happens when there is no matching row on the right side?

A. Right-side columns become `NULL`
B. Left-side columns become `NULL`
C. The query always fails
D. SQL Server creates a new right-side row

**Correct answer: A**

---

### 75. Which join is commonly used to find customers without orders?

A. `LEFT JOIN` with `WHERE o.OrderID IS NULL`
B. `INNER JOIN` only
C. `CROSS JOIN` only
D. `RIGHT JOIN` with no condition

**Correct answer: A**

---

### 76. What does `RIGHT JOIN` return?

A. All rows from the right table and matching rows from the left table
B. All rows from the left table only
C. Only unmatched rows
D. Every possible combination

**Correct answer: A**

---

### 77. Why do many developers avoid `RIGHT JOIN`?

A. It can often be rewritten as a clearer `LEFT JOIN` by switching table order
B. SQL Server does not support it
C. It never returns rows
D. It deletes unmatched rows

**Correct answer: A**

---

### 78. What does `FULL OUTER JOIN` return?

A. Matching rows plus rows found only in either table
B. Only matching rows
C. Only left table rows
D. Only right table rows

**Correct answer: A**

---

### 79. What is a practical use of `FULL OUTER JOIN`?

A. Comparing two sets and showing unmatched records from both sides
B. Sorting rows by date
C. Creating unique constraints
D. Replacing all primary keys

**Correct answer: A**

---

### 80. What does `CROSS JOIN` return?

A. Every possible combination of rows from two tables
B. Only matching rows
C. Only unmatched rows
D. Only rows with foreign keys

**Correct answer: A**

---

### 81. If there are 8 categories and 10 suppliers, how many rows does their `CROSS JOIN` return?

A. 18
B. 80
C. 10
D. 8

**Correct answer: B**

---

### 82. Which is a valid use case for `CROSS JOIN`?

A. Generating combinations
B. Enforcing foreign keys
C. Removing duplicate emails
D. Checking null values only

**Correct answer: A**

---

### 83. What is a self join?

A. A table joined to itself
B. A table joined to a backup
C. A query without a table
D. A join that always fails

**Correct answer: A**

---

### 84. In the self join example, why are aliases `c` and `ref` needed?

A. To represent the same table in two different roles
B. To remove primary keys
C. To create duplicate rows
D. To disable foreign keys

**Correct answer: A**

---

### 85. In the self join example, what does `ref` represent?

A. The referring customer
B. The order item
C. The product category
D. The supplier price

**Correct answer: A**

---

### 86. Why are aliases useful in joins?

A. They make queries shorter and easier to read
B. They delete table names permanently
C. They remove the need for join conditions
D. They automatically create indexes

**Correct answer: A**

---

### 87. Which query is easier to read?

A. A query using aliases like `o` and `c`
B. A query repeating full table names everywhere
C. A query without join conditions
D. A query with comma joins only

**Correct answer: A**

---

### 88. What should a join condition represent?

A. A real relationship between tables
B. A random pair of columns
C. A sorting preference
D. A display alias

**Correct answer: A**

---

### 89. What is wrong with joining `Orders.OrderID` to `Customers.CustomerID`?

A. It is logically wrong because it does not represent the relationship
B. It is always faster
C. It guarantees correct results
D. It creates a primary key

**Correct answer: A**

---

### 90. What can happen if a join condition is missing?

A. A Cartesian product may be created
B. The query automatically fixes itself
C. SQL Server always rejects it
D. Only one row is returned

**Correct answer: A**

---

### 91. What is a Cartesian product?

A. Every row from one table combined with every row from another table
B. Only matching rows
C. Only rows with nulls
D. Only grouped rows

**Correct answer: A**

---

### 92. Which old-style query can accidentally create a Cartesian product?

A. `FROM dbo.Customers c, dbo.Orders o`
B. `FROM dbo.Customers c JOIN dbo.Orders o ON c.CustomerID = o.CustomerID`
C. `FROM dbo.Customers c LEFT JOIN dbo.Orders o ON c.CustomerID = o.CustomerID`
D. `FROM dbo.Orders o WHERE o.OrderID IS NULL`

**Correct answer: A**

---

### 93. When filtering joined data, which clause is commonly used?

A. `WHERE`
B. `CROSS`
C. `PRIMARY KEY`
D. `UNIQUE`

**Correct answer: A**

---

### 94. Which condition finds completed orders over 1000?

A. `WHERE o.OrderStatus = N'Completed' AND o.TotalAmount > 1000`
B. `WHERE o.OrderStatus > N'Completed' OR o.TotalAmount = N'1000'`
C. `HAVING o.OrderStatus = N'Completed'`
D. `JOIN o.TotalAmount > 1000`

**Correct answer: A**

---

### 95. What are joins often combined with for reports?

A. `GROUP BY` and aggregate functions
B. `DROP TABLE`
C. `CREATE DATABASE`
D. `TRIM()` only

**Correct answer: A**

---

### 96. Which query idea calculates total revenue per customer?

A. Join customers to orders, group by customer, and sum order totals
B. Cross join all customers and products
C. Store customer emails in every product
D. Use only `DISTINCT Email`

**Correct answer: A**

---

### 97. What does `HAVING` do in grouped join reports?

A. Filters groups after grouping
B. Filters rows before joining only
C. Deletes unmatched rows
D. Creates a foreign key

**Correct answer: A**

---

### 98. Which condition finds customers with more than three orders?

A. `HAVING COUNT(o.OrderID) > 3`
B. `WHERE COUNT(o.OrderID) > 3`
C. `ORDER BY COUNT(o.OrderID) > 3`
D. `JOIN COUNT(o.OrderID) > 3`

**Correct answer: A**

---

### 99. What does a `NOT NULL` constraint require?

A. The column must have a value
B. The column must always be unique
C. The column must reference another table
D. The column must be a primary key

**Correct answer: A**

---

### 100. What should happen if a `NOT NULL` column receives `NULL` during insert?

A. SQL Server rejects the row
B. SQL Server accepts it silently
C. SQL Server converts it to zero
D. SQL Server creates a new column

**Correct answer: A**


# SQL Server Indexes and Introduction to Distributed Systems — 200 Single-Answer MCQ Questions

## Multiple Choice Questions

### 1. What is the common idea connecting indexes and distributed systems in the lecture?

A. Both remove all data from storage
B. Both avoid unnecessary work at scale
C. Both are only used in small systems
D. Both replace SQL queries

**Correct answer: B**

---

### 2. What problem do indexes mainly solve?

A. They make table names shorter
B. They help the database find rows efficiently
C. They remove the need for primary keys
D. They prevent all network failures

**Correct answer: B**

---

### 3. What problem do distributed systems mainly solve?

A. They make one computer faster forever
B. They allow many computers to cooperate when one machine is not enough
C. They remove the need for databases
D. They make SQL syntax shorter

**Correct answer: B**

---

### 4. What may SQL Server do without an index when searching a large table?

A. Perform a table scan
B. Automatically delete rows
C. Always use a clustered index
D. Refuse to run the query

**Correct answer: A**

---

### 5. What is a table scan?

A. Looking through many rows, possibly all rows
B. Creating a new table
C. Compressing an index
D. Copying data to another server

**Correct answer: A**

---

### 6. What is a heap scan?

A. Scanning a table without a clustered index
B. Sorting all rows by date
C. Updating all indexes
D. Running a distributed transaction

**Correct answer: A**

---

### 7. Why is scanning a large table often slow?

A. The database must inspect a large part of the table
B. SQL Server cannot read rows
C. Tables cannot contain indexes
D. SQL queries cannot filter rows

**Correct answer: A**

---

### 8. What is an index?

A. An additional data structure maintained by the database
B. A replacement for the table
C. A type of network node
D. A SQL Server backup file

**Correct answer: A**

---

### 9. Which simplified explanation of an index is correct?

A. A sorted copy of part of table data that helps find rows quickly
B. A random copy of the whole database
C. A deleted copy of old rows
D. A tool for encrypting network traffic

**Correct answer: A**

---

### 10. What does an index store?

A. Selected column values and row locators
B. Only table permissions
C. Only query history
D. Only database usernames

**Correct answer: A**

---

### 11. Why does an index use physical storage?

A. It creates additional pages on disk
B. It deletes table pages
C. It replaces RAM
D. It removes row locators

**Correct answer: A**

---

### 12. Which is a cost of having indexes?

A. Extra disk space
B. Faster inserts always
C. No memory usage
D. No maintenance

**Correct answer: A**

---

### 13. Which operation can become slower because of indexes?

A. Insert
B. Simple arithmetic
C. Reading SQL keywords
D. Opening SSMS

**Correct answer: A**

---

### 14. Why can inserts become slower with many indexes?

A. SQL Server must update the table and relevant indexes
B. SQL Server cannot insert into indexed tables
C. Indexes disable primary keys
D. Inserts become network calls only

**Correct answer: A**

---

### 15. What is an index seek?

A. Navigating directly to the relevant part of an index
B. Reading every row in a table
C. Deleting unused indexes
D. Copying data to all replicas

**Correct answer: A**

---

### 16. Which is usually faster for a highly selective search?

A. Index seek
B. Full table scan
C. Cartesian product
D. Network partition

**Correct answer: A**

---

### 17. In the query `WHERE FullName = N'Anna Brown'`, which index may help?

A. Index on `FullName`
B. Index on unrelated column only
C. No index can help
D. Index on table name

**Correct answer: A**

---

### 18. What does SQL Server use instead of the command name `EXPLAIN`?

A. Execution plans
B. Ping commands
C. Shard routers
D. Replication logs only

**Correct answer: A**

---

### 19. What does an execution plan show?

A. How SQL Server plans to execute a query
B. Only the table creation script
C. Only user passwords
D. Only database size

**Correct answer: A**

---

### 20. Which command can show a text execution plan in SQL Server?

A. `SET SHOWPLAN_TEXT ON`
B. `SET PING ON`
C. `SET SHARDING ON`
D. `SET TABLE_SCAN OFF`

**Correct answer: A**

---

### 21. Which command can show XML plans in SQL Server?

A. `SET SHOWPLAN_XML ON`
B. `SET EXPLAIN_XML_ONLY`
C. `SET XML_INDEX_SCAN ON`
D. `SHOW QUERY XML`

**Correct answer: A**

---

### 22. What is an Estimated Execution Plan?

A. What SQL Server thinks it will do
B. What SQL Server already deleted
C. What the network router decided
D. What the user typed previously

**Correct answer: A**

---

### 23. What is an Actual Execution Plan?

A. What SQL Server actually did
B. A theoretical database schema
C. A backup of all indexes
D. A list of users

**Correct answer: A**

---

### 24. What is the query optimizer?

A. A component that chooses a good execution plan
B. A network testing command
C. A table constraint
D. A backup engine

**Correct answer: A**

---

### 25. Which factor does the query optimizer consider?

A. Available indexes
B. User’s screen resolution
C. Keyboard layout
D. File extension of the query

**Correct answer: A**

---

### 26. Which of the following can influence the optimizer’s decision?

A. Table sizes and statistics
B. The color of the database icon
C. The name of the SQL file only
D. The operating system wallpaper

**Correct answer: A**

---

### 27. For `WHERE CustomerId = 10 AND OrderDate >= '2026-01-01'`, which index may be especially useful?

A. Composite index on `(CustomerId, OrderDate)`
B. Index only on unrelated `Description`
C. Index on server name
D. Index on table creation date

**Correct answer: A**

---

### 28. SQL Server rowstore indexes are commonly explained as what structure?

A. B-tree indexes
B. Linked lists only
C. Hash maps only
D. Arrays only

**Correct answer: A**

---

### 29. Technically, SQL Server rowstore indexes are closer to what?

A. B+ tree structure
B. Binary heap only
C. Stack structure
D. Queue structure

**Correct answer: A**

---

### 30. What is the key idea of a B-tree-like index?

A. A balanced tree allows quick value lookup
B. Every node has exactly two children
C. It stores no keys
D. It ignores sorting

**Correct answer: A**

---

### 31. Which is a level in a B-tree-like index?

A. Root page
B. Application page
C. Web page only
D. Backup page only

**Correct answer: A**

---

### 32. What does the leaf level contain?

A. Actual sorted index entries
B. Only network errors
C. Only SQL Server usernames
D. Only database diagrams

**Correct answer: A**

---

### 33. Why are B-trees efficient?

A. Each page can contain many keys and point to many child pages
B. They always scan every row
C. They do not store sorted values
D. They require no disk pages

**Correct answer: A**

---

### 34. Why is a B-tree usually shallow?

A. One page can point to many child pages
B. It can contain only two rows
C. It cannot have intermediate pages
D. It stores no data

**Correct answer: A**

---

### 35. In a B-tree search for key 155, where does SQL Server start?

A. Root page
B. Last row of the table
C. Random row
D. Follower replica

**Correct answer: A**

---

### 36. What is a clustered index?

A. An index that defines the physical order of table data
B. An index stored on another continent
C. An index that cannot contain keys
D. A network replication method

**Correct answer: A**

---

### 37. How many clustered indexes can a SQL Server table have?

A. One
B. Two
C. Unlimited
D. One per column

**Correct answer: A**

---

### 38. Why can a table have only one clustered index?

A. Data rows can be physically ordered in only one main way
B. SQL Server supports only one table
C. Clustered indexes use no storage
D. Clustered indexes are not real indexes

**Correct answer: A**

---

### 39. In a clustered index, what is at the leaf level?

A. The actual table data
B. Only row locators
C. Only network packets
D. Only query text

**Correct answer: A**

---

### 40. What is a nonclustered index?

A. An index separate from the table data
B. The physical order of the table data
C. A deleted index
D. A distributed node

**Correct answer: A**

---

### 41. What does a nonclustered index leaf level contain?

A. Index key values and row locators
B. Only actual table rows in physical order
C. Only network messages
D. Only database permissions

**Correct answer: A**

---

### 42. What may SQL Server perform if a nonclustered index does not contain all needed columns?

A. Lookup
B. Ping
C. Failover
D. Sharding

**Correct answer: A**

---

### 43. What is a lookup?

A. Extra step to read the actual table row after using an index
B. A command to split a database across nodes
C. A method of electing a leader
D. A type of packet loss

**Correct answer: A**

---

### 44. What is a covering index?

A. An index containing all columns needed by a query
B. An index that hides data from users
C. An index stored only in memory
D. An index used only for backups

**Correct answer: A**

---

### 45. Which SQL keyword adds non-key columns to an index?

A. `INCLUDE`
B. `EXTEND`
C. `APPEND`
D. `COPY`

**Correct answer: A**

---

### 46. Why can a covering index be very fast?

A. SQL Server can answer the query using only the index
B. It disables all writes
C. It ignores filters
D. It removes all rows from the table

**Correct answer: A**

---

### 47. What is a disadvantage of covering indexes?

A. They use more storage
B. They cannot include columns
C. They always make reads slower
D. They remove table data

**Correct answer: A**

---

### 48. What is a composite index?

A. An index using more than one key column
B. An index that stores no keys
C. An index on exactly one row
D. A distributed table replica

**Correct answer: A**

---

### 49. In `(CustomerId, OrderDate)`, what is the first key column?

A. `CustomerId`
B. `OrderDate`
C. Both are first
D. Neither is a key column

**Correct answer: A**

---

### 50. In a composite index, why does column order matter?

A. The data is sorted by the first key, then the next key
B. SQL Server ignores the first column
C. It changes table ownership
D. It disables the optimizer

**Correct answer: A**

---

### 51. Which query is usually helped by index `(CustomerId, OrderDate)`?

A. `WHERE CustomerId = 10 AND OrderDate >= '2026-01-01'`
B. `WHERE ProductName LIKE '%x%'` only
C. `WHERE RandomText IS NULL` only
D. `WHERE OrderDate >= '2026-01-01'` always equally

**Correct answer: A**

---

### 52. Why may `(CustomerId, OrderDate)` be less useful for filtering only by `OrderDate`?

A. `OrderDate` is not the first key
B. SQL Server cannot compare dates
C. Composite indexes cannot store dates
D. The index is not sorted at all

**Correct answer: A**

---

### 53. What is selectivity?

A. How well a column filters rows
B. How many servers exist
C. How fast a network cable is
D. How large a SQL file is

**Correct answer: A**

---

### 54. What is a highly selective column?

A. A column with many distinct values returning few rows per value
B. A column with only two values
C. A column with no values
D. A column used only in `ORDER BY`

**Correct answer: A**

---

### 55. Which is an example of a high-selectivity column?

A. `Email`
B. `Gender`
C. `IsActive`
D. `Status` with three values

**Correct answer: A**

---

### 56. Which is an example of a low-selectivity column?

A. `IsActive`
B. `PassportNumber`
C. `StudentId`
D. `OrderId`

**Correct answer: A**

---

### 57. Why may an index on `IsActive` be useless for `IsActive = 1` if 990,000 of 1,000,000 rows are active?

A. The query returns almost the whole table
B. SQL Server cannot index bit columns
C. The table has no rows
D. The network is partitioned

**Correct answer: A**

---

### 58. Can the same low-selectivity column be useful for one value and useless for another?

A. Yes
B. No
C. Only in distributed systems
D. Only with `CROSS JOIN`

**Correct answer: A**

---

### 59. When may an index on `IsActive` be useful in the lecture’s example?

A. For `IsActive = 0` if only 10,000 out of 1,000,000 users are inactive
B. For `IsActive = 1` only if almost all users are active
C. Never
D. Only when the table is empty

**Correct answer: A**

---

### 60. Why should indexes not be created for every column automatically?

A. Indexes cost storage and slow writes
B. SQL Server allows only one index per database
C. Indexes prevent queries
D. Indexes disable foreign keys

**Correct answer: A**

---

### 61. Which question belongs to a good index strategy?

A. Which queries are frequent?
B. What color is the server case?
C. How many students like SQL?
D. Which keyboard is used?

**Correct answer: A**

---

### 62. Which query part is important for index design?

A. Columns used in `WHERE`
B. Comments only
C. White space only
D. Database logo only

**Correct answer: A**

---

### 63. Which query part can an index support besides filtering?

A. `ORDER BY`
B. `PRINT` only
C. `USE` only
D. `GO` only

**Correct answer: A**

---

### 64. For `WHERE CustomerId = 100 ORDER BY OrderDate DESC`, which index is useful?

A. `(CustomerId, OrderDate DESC) INCLUDE (TotalAmount)`
B. `(TotalAmount)` only
C. `(RandomColumn)` only
D. No index can help

**Correct answer: A**

---

### 65. What does `TotalAmount` do in the example index?

A. It is included for output
B. It is the only search key
C. It becomes a shard key
D. It is used for leader election

**Correct answer: A**

---

### 66. What is the main tradeoff of indexes?

A. Faster reads but more storage and slower writes
B. Faster writes but slower reads always
C. No storage but high latency
D. Better networking but worse SQL syntax

**Correct answer: A**

---

### 67. What is a distributed system?

A. Multiple computers working together and appearing as one system
B. One computer with a large monitor
C. One table with many indexes
D. One SQL query with many columns

**Correct answer: A**

---

### 68. How do computers in a distributed system communicate?

A. Over a network
B. By sharing the same CPU register
C. By using one memory address only
D. By reading the same keyboard

**Correct answer: A**

---

### 69. Which component may be part of a distributed website?

A. Web server
B. Only one text file
C. Only one local variable
D. Only a keyboard driver

**Correct answer: A**

---

### 70. To the user, a distributed application often looks like what?

A. One application
B. Many unrelated broken programs
C. A SQL execution plan
D. A table scan

**Correct answer: A**

---

### 71. What is a node?

A. One participating machine or process in a distributed system
B. A SQL column
C. A B-tree key only
D. A table row only

**Correct answer: A**

---

### 72. Which can be a node?

A. Container
B. SQL keyword
C. Column alias
D. Index hint only

**Correct answer: A**

---

### 73. What can a node do?

A. Compute, store data, send messages, receive messages, and fail
B. Only store SQL comments
C. Only create indexes
D. Only sort rows

**Correct answer: A**

---

### 74. Why are distributed systems difficult?

A. Nodes do not share memory and communicate through a network
B. SQL Server cannot store data
C. Tables cannot have rows
D. Indexes cannot be updated

**Correct answer: A**

---

### 75. What is `ping` used for?

A. Testing whether another machine can be reached
B. Creating SQL indexes
C. Creating database tables
D. Running backups only

**Correct answer: A**

---

### 76. What is the important number in ping output?

A. Latency
B. Table size
C. Primary key value
D. Index name

**Correct answer: A**

---

### 77. What does latency mean?

A. How long a message takes to go to another machine and come back
B. How much disk space an index uses
C. How many rows a table has
D. How many keys are in a B-tree page

**Correct answer: A**

---

### 78. A ping time of 24 ms means what?

A. The round trip took about 24 milliseconds
B. The server has 24 rows
C. The database has 24 indexes
D. The network has 24 shards

**Correct answer: A**

---

### 79. What is bandwidth?

A. How much data can be transferred per second
B. How long a query waits in a lock
C. How many indexes a table has
D. How many nodes are down

**Correct answer: A**

---

### 80. How are latency and bandwidth different?

A. Latency is delay; bandwidth is transfer capacity per second
B. They mean exactly the same thing
C. Bandwidth is delay; latency is disk space
D. Both are SQL Server constraints

**Correct answer: A**

---

### 81. What does the truck full of hard drives example illustrate?

A. High bandwidth but very high latency
B. Low bandwidth and low latency
C. Index seek behavior
D. Clustered index design

**Correct answer: A**

---

### 82. What is packet loss?

A. Network packets can be lost and may need retransmission
B. SQL rows are deleted automatically
C. Index pages are compressed
D. Tables are replicated synchronously

**Correct answer: A**

---

### 83. What is congestion?

A. Too much traffic on a network path causing slowdown
B. Too many columns in a table
C. Too few primary keys
D. Too many aliases in a query

**Correct answer: A**

---

### 84. What is serialization?

A. Converting objects into bytes before sending
B. Creating indexes on all columns
C. Sorting SQL rows by date
D. Splitting data across shards

**Correct answer: A**

---

### 85. What is deserialization?

A. Converting received bytes back into objects
B. Deleting serialized rows
C. Removing indexes
D. Choosing a leader

**Correct answer: A**

---

### 86. Which cost does serialization/deserialization add?

A. CPU time
B. No cost at all
C. Only disk size
D. Only SQL syntax length

**Correct answer: A**

---

### 87. In a network failure, what may the sender see?

A. A timeout
B. A guaranteed explanation
C. The exact broken cable
D. The receiver’s memory

**Correct answer: A**

---

### 88. Which is a possible reason a message does not arrive?

A. Receiver crashed
B. The table has a primary key
C. The query has `ORDER BY`
D. The index is covering

**Correct answer: A**

---

### 89. What is big data according to the lecture?

A. A system of data processing where the amount of data could not fit into a single node
B. Any table with more than ten rows
C. Any database with text columns
D. Any system with a website

**Correct answer: A**

---

### 90. Which limitation can make one node insufficient?

A. Not enough disk
B. Too many SQL aliases
C. Too few table names
D. Too many comments

**Correct answer: A**

---

### 91. In the lecture example, what requires a distributed data processing system?

A. 500 TB logs with a server that has 1 TB disk
B. 10 rows in one local table
C. One small CSV file
D. One query using `TOP 10`

**Correct answer: A**

---

### 92. What is one motivation for distributed systems?

A. Capacity constraints
B. Removing all indexes
C. Avoiding all SQL queries
D. Making failures impossible

**Correct answer: A**

---

### 93. What is vertical scaling?

A. Making one machine stronger
B. Adding more machines
C. Splitting data by user ID
D. Copying data to replicas

**Correct answer: A**

---

### 94. What is horizontal scaling?

A. Adding more machines
B. Making one machine stronger
C. Deleting old data
D. Creating one clustered index

**Correct answer: A**

---

### 95. Why is horizontal scaling often necessary?

A. One server cannot grow forever
B. SQL Server cannot use indexes
C. Networks have no latency
D. One server never fails

**Correct answer: A**

---

### 96. What is availability?

A. The system continues to work when some parts fail
B. Every row has a primary key
C. All indexes are clustered
D. All queries use `SELECT *`

**Correct answer: A**

---

### 97. What happens if a single-server system fails?

A. The whole service may become unavailable
B. Availability always increases
C. The database becomes distributed automatically
D. All indexes become covering indexes

**Correct answer: A**

---

### 98. What is one reason for replication?

A. Availability
B. Making all writes disappear
C. Preventing all reads
D. Removing all storage

**Correct answer: A**

---

### 99. What is geo-distribution?

A. Placing nodes in different geographic locations
B. Creating indexes by geography only
C. Sorting rows by country
D. Removing regional users

**Correct answer: A**

---

### 100. Why can geo-distribution reduce latency?

A. Users can be closer to servers
B. Indexes become smaller automatically
C. SQL queries become shorter
D. Tables disappear

**Correct answer: A**

---

### 101. Which is a benefit of geo-distribution?

A. Service can survive regional failures
B. All consistency problems disappear
C. No network communication is needed
D. One node stores all data only

**Correct answer: A**

---

### 102. Why does geo-distribution make consistency harder?

A. Data changes must be propagated between distant locations
B. Servers cannot store data
C. SQL Server cannot compare strings
D. Indexes cannot be used

**Correct answer: A**

---

### 103. What is redundancy?

A. Storing or running extra copies so failure does not destroy the system
B. Removing all backup copies
C. Storing one copy only
D. Creating invalid foreign keys

**Correct answer: A**

---

### 104. What question does redundancy create?

A. How do we keep all copies correct?
B. How do we delete all rows?
C. How do we avoid using networks?
D. How do we remove all users?

**Correct answer: A**

---

### 105. What is the central problem of distributed data?

A. A write on one node may not be immediately visible on another node
B. Tables cannot have rows
C. Indexes cannot be sorted
D. SQL cannot filter rows

**Correct answer: A**

---

### 106. What does CAP theorem discuss?

A. Tradeoffs in distributed data systems during network partitions
B. How to create clustered indexes
C. How to write `SELECT TOP 10`
D. How to format SQL code

**Correct answer: A**

---

### 107. What does C mean in CAP?

A. Consistency
B. Capacity
C. Compression
D. Caching only

**Correct answer: A**

---

### 108. What does A mean in CAP?

A. Availability
B. Atomicity
C. Authentication
D. Aggregation

**Correct answer: A**

---

### 109. What does P mean in CAP?

A. Partition tolerance
B. Primary key
C. Packet speed
D. Page size

**Correct answer: A**

---

### 110. What does consistency mean in CAP?

A. Every read receives the latest write or an error
B. Every request always succeeds with any data
C. Every database has one table
D. Every index is clustered

**Correct answer: A**

---

### 111. What does availability mean in CAP?

A. Every request receives a response
B. Every read receives the latest write only
C. Every table has a clustered index
D. Every network packet is encrypted

**Correct answer: A**

---

### 112. What does partition tolerance mean?

A. The system continues operating despite communication failure between nodes
B. The table is divided into columns
C. The query uses `PARTITION BY` only
D. The database has no failures

**Correct answer: A**

---

### 113. What is the real CAP choice during a network partition?

A. Consistency versus availability
B. SQL versus NoSQL only
C. Indexes versus tables
D. Memory versus CPU only

**Correct answer: A**

---

### 114. In the registration example, what must not happen?

A. The same stranger must not be registered twice
B. People must never use phones
C. No one can register any stranger ever
D. Everyone must have the same name

**Correct answer: A**

---

### 115. In the registration example, what do the phones represent?

A. Network communication between nodes
B. SQL indexes
C. Clustered tables
D. Backup files

**Correct answer: A**

---

### 116. If phones work, what can Alice do before registering John?

A. Check with Bob and Carol
B. Ignore all other lists
C. Delete her list
D. Create a B-tree

**Correct answer: A**

---

### 117. If Alice refuses to register John during phone failure, what is preserved?

A. Consistency
B. Availability
C. Low latency
D. Bandwidth

**Correct answer: A**

---

### 118. If Alice refuses registration during partition, what is reduced?

A. Availability
B. Consistency
C. Partition tolerance
D. Data correctness

**Correct answer: A**

---

### 119. Alice refusing registration during partition is closer to what behavior?

A. CP
B. AP
C. CA during partition
D. No CAP behavior

**Correct answer: A**

---

### 120. If Alice registers John without contacting others, what is preserved?

A. Availability
B. Strong consistency
C. Synchronous replication
D. Clustered indexing

**Correct answer: A**

---

### 121. If Alice and Bob both register John during a partition, what may happen?

A. Duplicate registration
B. Guaranteed consistency
C. No response to users
D. Index seek

**Correct answer: A**

---

### 122. Alice registering during partition is closer to what behavior?

A. AP
B. CP
C. Single-node behavior
D. Index behavior

**Correct answer: A**

---

### 123. Traditional single-node RDBMS usually prioritizes what?

A. Consistency
B. Network partition tolerance inside one node
C. Eventual inconsistency
D. Random writes

**Correct answer: A**

---

### 124. Why is CAP not the main issue on one database node?

A. There is no distributed network partition inside the single database node
B. SQL Server has no consistency
C. One node cannot store data
D. Indexes remove CAP theorem

**Correct answer: A**

---

### 125. When do CAP tradeoffs appear for relational databases?

A. When they are distributed through replication
B. When a table has a primary key
C. When `SELECT *` is used
D. When an index is created

**Correct answer: A**

---

### 126. In synchronous RDBMS replication, what may happen if a required replica is unreachable?

A. The write may be rejected or delayed
B. The write always succeeds instantly
C. The table becomes a heap
D. The index is deleted

**Correct answer: A**

---

### 127. Cassandra is designed mainly for what?

A. High availability and horizontal scaling
B. Single-node only execution
C. No replication
D. No partition tolerance

**Correct answer: A**

---

### 128. Cassandra is often described as what style?

A. AP-style
B. Single-node-only
C. Index-only
D. NoSQL without replication

**Correct answer: A**

---

### 129. What may Cassandra allow?

A. Temporary inconsistency
B. No writes during any failure
C. No replication
D. Only single-node storage

**Correct answer: A**

---

### 130. Which mechanism can Cassandra use to repair differences?

A. Read repair
B. Clustered index seek
C. `SHOWPLAN_TEXT`
D. `CROSS JOIN`

**Correct answer: A**

---

### 131. What is Redis often used as?

A. In-memory cache or fast key-value store
B. Only a relational table engine
C. Only a B-tree visualization tool
D. Only a blockchain consensus engine

**Correct answer: A**

---

### 132. In a simple Redis primary-replica setup, which node accepts writes?

A. Primary
B. Replica only
C. All nodes independently always
D. No node

**Correct answer: A**

---

### 133. Why can recent writes be lost in Redis async replication?

A. Primary may fail before replicas receive the write
B. Redis cannot store keys
C. Replicas always write first
D. SQL Server deletes them

**Correct answer: A**

---

### 134. What does asynchronous replication mean?

A. Main confirms before followers receive the update
B. Main waits for all followers before confirming
C. No data is copied
D. All nodes share memory

**Correct answer: A**

---

### 135. What do blockchain nodes maintain?

A. Copies of a ledger
B. Only SQL Server indexes
C. Only local cache entries
D. Only table statistics

**Correct answer: A**

---

### 136. What do blockchains use to agree on valid blocks?

A. Consensus rules
B. Nonclustered indexes
C. Table scans
D. `SHOWPLAN_XML`

**Correct answer: A**

---

### 137. Why is blockchain not simply “always available” for fast final writes?

A. Consensus and finality take time
B. It has no nodes
C. It cannot store transactions
D. It does not tolerate partitions

**Correct answer: A**

---

### 138. During a blockchain partition, what may temporarily happen?

A. Groups of nodes may see different chain versions
B. All nodes share memory instantly
C. No node can store data
D. Indexes become clustered

**Correct answer: A**

---

### 139. What is replication?

A. Storing copies of the same data on multiple nodes
B. Splitting different data across nodes only
C. Removing all data copies
D. Creating a SQL alias

**Correct answer: A**

---

### 140. Which is a reason to replicate data?

A. Fault tolerance
B. Making one copy only
C. Increasing write conflicts intentionally
D. Removing all read capacity

**Correct answer: A**

---

### 141. What is main-follower replication also called?

A. Primary-replica
B. Heap scan
C. Table partition only
D. B-tree lookup

**Correct answer: A**

---

### 142. In main-follower replication, which node accepts writes?

A. Main node
B. Follower only
C. Every follower independently
D. No node

**Correct answer: A**

---

### 143. In main-follower replication, what do followers do?

A. Copy data from the main node
B. Replace the main for every write
C. Delete all writes
D. Create indexes only

**Correct answer: A**

---

### 144. What can followers often serve?

A. Read queries
B. Independent conflicting writes
C. Only backups, never reads
D. Only network pings

**Correct answer: A**

---

### 145. What is synchronous replication?

A. Main waits for follower confirmation before confirming write
B. Main confirms immediately before replication
C. No replicas exist
D. Followers accept all writes independently

**Correct answer: A**

---

### 146. What is an advantage of synchronous replication?

A. Stronger consistency
B. Faster writes always
C. No dependency on followers
D. No network communication

**Correct answer: A**

---

### 147. What is a disadvantage of synchronous replication?

A. Slower writes and lower availability if follower is unreachable
B. No consistency
C. No data safety
D. No replication

**Correct answer: A**

---

### 148. What is asynchronous replication?

A. Main confirms write before followers receive it
B. Main waits for all followers first
C. Followers cannot receive data
D. All nodes share disk

**Correct answer: A**

---

### 149. What is an advantage of asynchronous replication?

A. Faster writes and better availability
B. Strongest immediate consistency always
C. No stale reads ever
D. No data loss risk

**Correct answer: A**

---

### 150. What is a disadvantage of asynchronous replication?

A. Followers can be stale
B. Writes must always wait for all followers
C. It cannot scale reads
D. It prevents replication lag

**Correct answer: A**

---

### 151. What is a read-only follower?

A. A replica that can serve reads but cannot accept writes
B. A main database that cannot read
C. A shard router
D. A B-tree leaf page

**Correct answer: A**

---

### 152. Why are read-only followers useful?

A. They improve read scalability
B. They make all writes faster infinitely
C. They remove all consistency problems
D. They delete the main node

**Correct answer: A**

---

### 153. Which type of application often benefits from read replicas?

A. Applications with many more reads than writes
B. Applications with no reads
C. Applications with no data
D. Applications with only network partitions

**Correct answer: A**

---

### 154. What is replication lag?

A. Delay between a write on main and the same data appearing on follower
B. Delay between typing and saving a SQL file
C. Difference between clustered and nonclustered indexes
D. Number of keys in a B-tree page

**Correct answer: A**

---

### 155. What can happen during replication lag?

A. A follower may return old data
B. A follower always has the latest data
C. The main cannot accept writes
D. Indexes disappear

**Correct answer: A**

---

### 156. For critical reads immediately after writes, where may the application need to read from?

A. Main node
B. Stale follower
C. Random shard
D. Network router only

**Correct answer: A**

---

### 157. What is sharding?

A. Splitting data across different nodes
B. Copying the same data to every node
C. Creating one index
D. Running `ping` repeatedly

**Correct answer: A**

---

### 158. What does each shard store?

A. Only part of the data
B. A full copy of all data always
C. Only execution plans
D. Only network logs

**Correct answer: A**

---

### 159. Replication copies what?

A. Same data to many nodes
B. Different data to each node only
C. Only indexes
D. Only query text

**Correct answer: A**

---

### 160. Sharding places what on different nodes?

A. Different data
B. Same full copy always
C. Only table statistics
D. Only SQL aliases

**Correct answer: A**

---

### 161. Why is sharding useful?

A. One node may not store or process all data
B. It removes all joins automatically
C. It prevents all network failures
D. It makes all data consistent instantly

**Correct answer: A**

---

### 162. Which is a benefit of sharding?

A. More storage capacity
B. No complexity
C. No routing needed
D. No failures possible

**Correct answer: A**

---

### 163. What does a shard router decide?

A. Which shard should receive the request
B. Which index should be deleted
C. Which table should be renamed
D. Which SQL keyword to use

**Correct answer: A**

---

### 164. What is a sharding key?

A. Value used to decide where data goes
B. A password for a shard
C. A clustered index leaf page
D. A network packet header only

**Correct answer: A**

---

### 165. Which can be a sharding key?

A. `UserId`
B. SQL comment
C. Query whitespace
D. Keyboard layout

**Correct answer: A**

---

### 166. In `shard = UserId % number_of_shards`, if `UserId = 105` and shards = 4, what is the result?

A. 1
B. 4
C. 105
D. 0.4

**Correct answer: A**

---

### 167. Why is choosing a good sharding key important?

A. A bad key creates imbalance
B. It removes all data
C. It disables replication
D. It prevents storage

**Correct answer: A**

---

### 168. What is a hot shard?

A. A shard receiving too much traffic
B. A shard stored in RAM only
C. A shard with no data
D. A shard with no network

**Correct answer: A**

---

### 169. What can cause a hot shard?

A. Sharding by country when 90% of users are from one country
B. Using too many aliases
C. Creating one execution plan
D. Using a covering index

**Correct answer: A**

---

### 170. What should good sharding spread?

A. Data and traffic
B. SQL comments only
C. One user to all shards always
D. Only table names

**Correct answer: A**

---

### 171. What is partitioning?

A. Dividing data into parts
B. Copying all data to every node only
C. Creating only primary keys
D. Running `ping`

**Correct answer: A**

---

### 172. What is logical table partitioning?

A. Dividing a large table into smaller parts inside one database system
B. Sending every query to all continents
C. Copying data to all followers
D. Choosing a main node

**Correct answer: A**

---

### 173. What can date partitioning help with?

A. Faster queries on specific ranges
B. Removing all indexes
C. Preventing every failure
D. Replacing SQL Server

**Correct answer: A**

---

### 174. What is distributed partitioning similar to?

A. Sharding
B. Clustered indexing
C. `SHOWPLAN_TEXT`
D. Table scanning

**Correct answer: A**

---

### 175. What is the useful distinction between partitioning and sharding?

A. Partitioning is general division; sharding is distributed partitioning across nodes
B. They are completely unrelated
C. Sharding always means one node only
D. Partitioning always means replication

**Correct answer: A**

---

### 176. Large systems often use which combination?

A. Replication plus sharding
B. No replication and no sharding
C. Only table scans
D. Only one server forever

**Correct answer: A**

---

### 177. What does replication plus sharding provide?

A. Capacity from sharding and availability/read scalability from replication
B. No complexity
C. No need for routing
D. No need for failover

**Correct answer: A**

---

### 178. What complexity appears with replication plus sharding?

A. The system must know which shard owns data and which nodes are healthy
B. SQL Server stops using tables
C. All data becomes local memory
D. Queries no longer need planning

**Correct answer: A**

---

### 179. What is consensus?

A. Several nodes agreeing on one decision
B. One node reading an index
C. One query scanning a table
D. One user opening a website

**Correct answer: A**

---

### 180. Which decision may require consensus?

A. Which node is the main
B. Which font is used in SQL editor
C. Which color the server case is
D. Which table name is longest

**Correct answer: A**

---

### 181. Why is consensus difficult?

A. Messages can be delayed, lost, and nodes can crash
B. SQL Server has no tables
C. Indexes cannot store values
D. Networks are always perfect

**Correct answer: A**

---

### 182. What happens if nodes disagree about who is main?

A. Two nodes may accept writes at the same time
B. Reads become impossible forever
C. All indexes become faster
D. Network latency becomes zero

**Correct answer: A**

---

### 183. What is split-brain?

A. A system accidentally has two active main nodes
B. A B-tree has two leaf pages
C. A query uses two indexes
D. A table has two columns

**Correct answer: A**

---

### 184. What can split-brain cause?

A. Conflicting data
B. Guaranteed consistency
C. Faster consensus
D. No writes

**Correct answer: A**

---

### 185. What do consensus algorithms help prevent?

A. Split-brain
B. Table creation
C. Index creation
D. Simple SELECT queries

**Correct answer: A**

---

### 186. What is majority quorum?

A. Majority of nodes required for a decision
B. All rows in a table
C. All indexes in a database
D. All SQL commands in a script

**Correct answer: A**

---

### 187. What is the majority formula from the lecture?

A. `floor(N / 2) + 1`
B. `N * 2`
C. `N - 2`
D. `N / 10`

**Correct answer: A**

---

### 188. What is the majority in a 3-node cluster?

A. 2
B. 1
C. 3.5
D. 0

**Correct answer: A**

---

### 189. What is the majority in a 5-node cluster?

A. 3
B. 2
C. 5.5
D. 1

**Correct answer: A**

---

### 190. Why do majority quorums help?

A. Two different majorities must overlap
B. They remove all network failures
C. They make every node independent
D. They eliminate storage

**Correct answer: A**

---

### 191. In a 3-node cluster, if Node A is alone after partition, can it make majority decisions?

A. No
B. Yes, always
C. Only if it has an index
D. Only if it is a follower

**Correct answer: A**

---

### 192. What tradeoff does consensus create?

A. Safety improves, but availability can decrease
B. Availability always increases without cost
C. Consistency disappears
D. Failures become impossible

**Correct answer: A**

---

### 193. What is a consensus log?

A. An ordered list of operations agreed by nodes
B. A list of SQL Server indexes only
C. A table scan report
D. A network ping output

**Correct answer: A**

---

### 194. What must correct nodes do with the consensus log?

A. Apply the same operations in the same order
B. Apply random operations
C. Ignore committed entries
D. Delete all entries

**Correct answer: A**

---

### 195. What is state machine replication?

A. Nodes applying the same log to end in the same state
B. Tables scanning all rows
C. Indexes storing row locators
D. Networks losing packets

**Correct answer: A**

---

### 196. Which consensus algorithm is often easiest for students to understand?

A. Raft
B. `SHOWPLAN_XML`
C. B-tree
D. `PING`

**Correct answer: A**

---

### 197. Which idea belongs to Raft?

A. Leader
B. Clustered index leaf page
C. Table scan
D. Low-selectivity column only

**Correct answer: A**

---

### 198. When is a Raft log entry committed?

A. When a majority confirms it
B. When only one isolated node writes it
C. When a table scan finishes
D. When `ping` returns 24 ms

**Correct answer: A**

---

### 199. What is the difference between replication and consensus?

A. Replication copies data; consensus agrees on what data or decision is official
B. They mean exactly the same thing
C. Consensus copies data only
D. Replication elects leaders safely by itself always

**Correct answer: A**

---

### 200. What is the purpose of consensus in RDBMS failover?

A. To safely decide which follower becomes the new main
B. To speed up every SELECT query
C. To create covering indexes
D. To remove replication lag completely

**Correct answer: A**


