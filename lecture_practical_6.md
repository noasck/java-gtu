# 1. Copy table creation script:
``` sql
SET ANSI_NULLS ON;
SET QUOTED_IDENTIFIER ON;
SET ANSI_PADDING ON;
SET ANSI_WARNINGS ON;
SET ARITHABORT ON;
SET CONCAT_NULL_YIELDS_NULL ON;
SET NUMERIC_ROUNDABORT OFF;
GO

IF SCHEMA_ID('Training') IS NULL
	EXEC('CREATE SCHEMA Training');
GO

IF OBJECT_ID('Training.CustomerOrders', 'U') IS NOT NULL
	DROP TABLE Training.CustomerOrders;
GO

CREATE TABLE Training.CustomerOrders
(
	OrderID INT IDENTITY(1,1) NOT NULL,
	OrderGuid UNIQUEIDENTIFIER NOT NULL CONSTRAINT DF_CustomerOrders_OrderGuid DEFAULT NEWID(),

	ExternalOrderNumber BIGINT NOT NULL,

	CustomerID INT NOT NULL,
	CustomerName NVARCHAR(100) NOT NULL,
	CustomerEmail VARCHAR(150) NOT NULL,
	CustomerSegment NVARCHAR(30) NOT NULL,

	CountryCode CHAR(2) NOT NULL,
	Region NVARCHAR(50) NOT NULL,
	City NVARCHAR(80) NOT NULL,

	ProductSKU VARCHAR(40) NOT NULL,
	ProductName NVARCHAR(120) NOT NULL,
	ProductCategory NVARCHAR(60) NOT NULL,
	ProductDescription NVARCHAR(MAX) NULL,

	OrderStatus NVARCHAR(30) NOT NULL,
	PaymentMethod NVARCHAR(30) NOT NULL,

	OrderDate DATE NOT NULL,
	OrderTime TIME(0) NOT NULL,
	CreatedAt DATETIME2(0) NOT NULL,
	ProcessedAt DATETIME2(0) NULL,
	DeliveredAt DATETIME2(0) NULL,

	Quantity SMALLINT NOT NULL,
	UnitPrice DECIMAL(10,2) NOT NULL,
	DiscountPercent DECIMAL(5,2) NOT NULL,
	TaxRate DECIMAL(5,2) NOT NULL,
	ShippingCost MONEY NOT NULL,

	OrderTotal AS
	(
		CONVERT
		(
			DECIMAL(12,2),
			ROUND
			(
				(
					CONVERT(DECIMAL(19,4), Quantity)
					* UnitPrice
					* (1 - DiscountPercent / 100.00)
					* (1 + TaxRate / 100.00)
				)
				+ CONVERT(DECIMAL(19,4), ShippingCost),
				2
			)
		)
	) PERSISTED,

	IsPriority BIT NOT NULL,
	IsGift BIT NOT NULL,
	SatisfactionScore TINYINT NULL,
	DeliveryDays SMALLINT NULL,

	CustomerNotes NVARCHAR(500) NULL,
	MetadataJson NVARCHAR(MAX) NOT NULL,
	InvoiceXml XML NULL,

	FraudRiskScore FLOAT NOT NULL,
	RowHash VARBINARY(32) NOT NULL,
	RowVersion ROWVERSION NOT NULL,

	CONSTRAINT PK_CustomerOrders PRIMARY KEY CLUSTERED (OrderID),

	CONSTRAINT UQ_CustomerOrders_ExternalOrderNumber UNIQUE (ExternalOrderNumber),

	CONSTRAINT CK_CustomerOrders_OrderStatus CHECK
	(
		OrderStatus IN
		(
			N'Pending',
			N'Paid',
			N'Processing',
			N'Shipped',
			N'Delivered',
			N'Cancelled',
			N'Returned',
			N'Refunded'
		)
	),

	CONSTRAINT CK_CustomerOrders_CustomerSegment CHECK
	(
		CustomerSegment IN
		(
			N'Retail',
			N'SMB',
			N'Enterprise',
			N'Education',
			N'Government'
		)
	),

	CONSTRAINT CK_CustomerOrders_Quantity CHECK (Quantity > 0),
	CONSTRAINT CK_CustomerOrders_UnitPrice CHECK (UnitPrice >= 0),
	CONSTRAINT CK_CustomerOrders_DiscountPercent CHECK (DiscountPercent BETWEEN 0 AND 100),
	CONSTRAINT CK_CustomerOrders_TaxRate CHECK (TaxRate BETWEEN 0 AND 30),
	CONSTRAINT CK_CustomerOrders_ShippingCost CHECK (ShippingCost >= 0),

	CONSTRAINT CK_CustomerOrders_SatisfactionScore CHECK
	(
		SatisfactionScore IS NULL OR SatisfactionScore BETWEEN 1 AND 5
	),

	CONSTRAINT CK_CustomerOrders_MetadataJson CHECK (ISJSON(MetadataJson) = 1)
);
GO

;WITH Numbers AS
(
	SELECT TOP (150)
		ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS n
	FROM sys.all_objects a
	CROSS JOIN sys.all_objects b
),
Prepared AS
(
	SELECT
		n,

		CustomerID = 1000 + (n % 45),

		CustomerName =
			CASE n % 12
				WHEN 0 THEN N'Nino Beridze'
				WHEN 1 THEN N'Giorgi Kapanadze'
				WHEN 2 THEN N'Mariam Gelashvili'
				WHEN 3 THEN N'Luka Maisuradze'
				WHEN 4 THEN N'Ana Khutsishvili'
				WHEN 5 THEN N'Davit Abashidze'
				WHEN 6 THEN N'Tamar Dolidze'
				WHEN 7 THEN N'Sandro Japaridze'
				WHEN 8 THEN N'Elene Tsereteli'
				WHEN 9 THEN N'Irakli Nozadze'
				WHEN 10 THEN N'Salome Vashakidze'
				ELSE N'Nikoloz Shengelia'
			END,

		CustomerSegment =
			CASE n % 5
				WHEN 0 THEN N'Retail'
				WHEN 1 THEN N'SMB'
				WHEN 2 THEN N'Enterprise'
				WHEN 3 THEN N'Education'
				ELSE N'Government'
			END,

		CountryCode =
			CASE n % 8
				WHEN 0 THEN 'GE'
				WHEN 1 THEN 'US'
				WHEN 2 THEN 'DE'
				WHEN 3 THEN 'FR'
				WHEN 4 THEN 'TR'
				WHEN 5 THEN 'PL'
				WHEN 6 THEN 'IT'
				ELSE 'ES'
			END,

		Region =
			CASE n % 10
				WHEN 0 THEN N'Tbilisi'
				WHEN 1 THEN N'Adjara'
				WHEN 2 THEN N'Imereti'
				WHEN 3 THEN N'Kakheti'
				WHEN 4 THEN N'Berlin'
				WHEN 5 THEN N'California'
				WHEN 6 THEN N'Istanbul'
				WHEN 7 THEN N'Warsaw'
				WHEN 8 THEN N'Lombardy'
				ELSE N'Madrid'
			END,

		City =
			CASE n % 10
				WHEN 0 THEN N'Tbilisi'
				WHEN 1 THEN N'Batumi'
				WHEN 2 THEN N'Kutaisi'
				WHEN 3 THEN N'Telavi'
				WHEN 4 THEN N'Berlin'
				WHEN 5 THEN N'San Francisco'
				WHEN 6 THEN N'Istanbul'
				WHEN 7 THEN N'Warsaw'
				WHEN 8 THEN N'Milan'
				ELSE N'Madrid'
			END,

		ProductCategory =
			CASE n % 9
				WHEN 0 THEN N'Laptops'
				WHEN 1 THEN N'Smartphones'
				WHEN 2 THEN N'Networking'
				WHEN 3 THEN N'Office Equipment'
				WHEN 4 THEN N'Software'
				WHEN 5 THEN N'Cloud Services'
				WHEN 6 THEN N'Security'
				WHEN 7 THEN N'Accessories'
				ELSE N'Database Services'
			END,

		ProductName =
			CASE n % 12
				WHEN 0 THEN N'ProBook 15 Business Laptop'
				WHEN 1 THEN N'Galaxy Pro Smartphone'
				WHEN 2 THEN N'Enterprise WiFi Router'
				WHEN 3 THEN N'Laser Office Printer'
				WHEN 4 THEN N'SQL Server Backup License'
				WHEN 5 THEN N'Cloud Storage Subscription'
				WHEN 6 THEN N'Endpoint Security Suite'
				WHEN 7 THEN N'USB-C Docking Station'
				WHEN 8 THEN N'Database Monitoring Package'
				WHEN 9 THEN N'Full-Text Search Add-on'
				WHEN 10 THEN N'Analytics Dashboard License'
				ELSE N'Premium Support Contract'
			END,

		OrderStatus =
			CASE n % 8
				WHEN 0 THEN N'Pending'
				WHEN 1 THEN N'Paid'
				WHEN 2 THEN N'Processing'
				WHEN 3 THEN N'Shipped'
				WHEN 4 THEN N'Delivered'
				WHEN 5 THEN N'Cancelled'
				WHEN 6 THEN N'Returned'
				ELSE N'Refunded'
			END,

		PaymentMethod =
			CASE n % 6
				WHEN 0 THEN N'Credit Card'
				WHEN 1 THEN N'Bank Transfer'
				WHEN 2 THEN N'PayPal'
				WHEN 3 THEN N'Cash'
				WHEN 4 THEN N'Invoice'
				ELSE N'Crypto'
			END,

		OrderDate = CONVERT(DATE, DATEADD(DAY, -n, GETDATE())),
		OrderTime = TIMEFROMPARTS((n * 7) % 24, (n * 13) % 60, 0, 0, 0),
		CreatedAt = DATEADD(MINUTE, -(n * 37), CONVERT(DATETIME2(0), SYSUTCDATETIME())),

		Quantity = CONVERT(SMALLINT, 1 + (n % 8)),

		UnitPrice =
			CONVERT
			(
				DECIMAL(10,2),
				19.99 + ((n % 25) * 13.75) + ((n % 7) * 2.40)
			),

		DiscountPercent =
			CONVERT
			(
				DECIMAL(5,2),
				CASE
					WHEN n % 17 = 0 THEN 25.00
					WHEN n % 11 = 0 THEN 15.00
					WHEN n % 5 = 0 THEN 10.00
					WHEN n % 3 = 0 THEN 5.00
					ELSE 0.00
				END
			),

		TaxRate =
			CONVERT
			(
				DECIMAL(5,2),
				CASE n % 5
					WHEN 0 THEN 18.00
					WHEN 1 THEN 20.00
					WHEN 2 THEN 19.00
					WHEN 3 THEN 21.00
					ELSE 0.00
				END
			),

		ShippingCost =
			CONVERT
			(
				MONEY,
				CASE
					WHEN n % 13 = 0 THEN 0.00
					WHEN n % 4 = 0 THEN 14.90
					WHEN n % 3 = 0 THEN 9.90
					ELSE 5.90
				END
			),

		IsPriority = CONVERT(BIT, CASE WHEN n % 11 = 0 THEN 1 ELSE 0 END),
		IsGift = CONVERT(BIT, CASE WHEN n % 14 = 0 THEN 1 ELSE 0 END),

		SatisfactionScore =
			CASE
				WHEN n % 13 = 0 THEN NULL
				WHEN n % 8 IN (0, 1) THEN 5
				WHEN n % 8 IN (2, 3) THEN 4
				WHEN n % 8 IN (4, 5) THEN 3
				WHEN n % 8 = 6 THEN 2
				ELSE 1
			END,

		DeliveryDays =
			CASE
				WHEN n % 8 IN (0, 1, 2, 5, 7) THEN NULL
				ELSE CONVERT(SMALLINT, 1 + (n % 12))
			END,

		FraudRiskScore =
			CONVERT(FLOAT, ROUND(((n % 97) * 0.87) / 10.0, 2))
	FROM Numbers
)
INSERT INTO Training.CustomerOrders
(
	OrderGuid,
	ExternalOrderNumber,
	CustomerID,
	CustomerName,
	CustomerEmail,
	CustomerSegment,
	CountryCode,
	Region,
	City,
	ProductSKU,
	ProductName,
	ProductCategory,
	ProductDescription,
	OrderStatus,
	PaymentMethod,
	OrderDate,
	OrderTime,
	CreatedAt,
	ProcessedAt,
	DeliveredAt,
	Quantity,
	UnitPrice,
	DiscountPercent,
	TaxRate,
	ShippingCost,
	IsPriority,
	IsGift,
	SatisfactionScore,
	DeliveryDays,
	CustomerNotes,
	MetadataJson,
	InvoiceXml,
	FraudRiskScore,
	RowHash
)
SELECT
	NEWID(),
	9000000000 + n,
	CustomerID,
	CustomerName,

	LOWER
	(
		REPLACE
		(
			CONVERT(VARCHAR(100), CustomerName),
			' ',
			'.'
		)
	)
	+ CONVERT(VARCHAR(10), n)
	+ '@example.com',

	CustomerSegment,
	CountryCode,
	Region,
	City,

	'SKU-' + RIGHT('00000' + CONVERT(VARCHAR(10), 10000 + n), 5),

	ProductName,
	ProductCategory,

	CASE n % 10
		WHEN 0 THEN N'High performance business laptop with encrypted storage, extended warranty, and enterprise deployment support.'
		WHEN 1 THEN N'Premium smartphone with OLED display, biometric security, fast charging, and mobile device management support.'
		WHEN 2 THEN N'Enterprise networking router for secure office connectivity, VPN access, monitoring, and traffic control.'
		WHEN 3 THEN N'Office printer with duplex printing, network scanning, document workflow support, and low maintenance cost.'
		WHEN 4 THEN N'SQL Server backup license for automated recovery, compliance reporting, and disaster recovery planning.'
		WHEN 5 THEN N'Cloud storage subscription with scalable capacity, audit logs, secure access, and team collaboration.'
		WHEN 6 THEN N'Endpoint security suite with malware protection, threat monitoring, device control, and reporting.'
		WHEN 7 THEN N'USB-C docking station with HDMI, Ethernet, power delivery, and multi-monitor support.'
		WHEN 8 THEN N'Database monitoring package with performance alerts, query analysis, index recommendations, and dashboards.'
		ELSE N'Full-text search add-on for fast document search, ranking, linguistic search, and content discovery.'
	END,

	OrderStatus,
	PaymentMethod,
	OrderDate,
	OrderTime,
	CreatedAt,

	CASE
		WHEN OrderStatus IN (N'Pending', N'Cancelled') THEN NULL
		ELSE DATEADD(MINUTE, 20 + (n % 180), CreatedAt)
	END,

	CASE
		WHEN OrderStatus IN (N'Delivered', N'Returned') THEN DATEADD(DAY, ISNULL(DeliveryDays, 5), CreatedAt)
		ELSE NULL
	END,

	Quantity,
	UnitPrice,
	DiscountPercent,
	TaxRate,
	ShippingCost,
	IsPriority,
	IsGift,
	SatisfactionScore,
	DeliveryDays,

	CASE
		WHEN n % 15 = 0 THEN NULL
		WHEN n % 10 = 0 THEN N'Customer requested urgent delivery and invoice copy.'
		WHEN n % 10 = 1 THEN N'Repeat customer, prefers email communication.'
		WHEN n % 10 = 2 THEN N'Potential bulk purchase opportunity for next quarter.'
		WHEN n % 10 = 3 THEN N'Delivery address confirmed by phone.'
		WHEN n % 10 = 4 THEN N'Customer asked about warranty extension.'
		WHEN n % 10 = 5 THEN N'Order was reviewed by finance department.'
		WHEN n % 10 = 6 THEN N'Customer reported slow previous delivery.'
		WHEN n % 10 = 7 THEN N'Gift packaging requested.'
		WHEN n % 10 = 8 THEN N'Customer searched for database performance optimization.'
		ELSE N'No special requirements.'
	END,

	CONCAT
	(
		'{',
			'"source":"',
			CASE n % 5
				WHEN 0 THEN 'web'
				WHEN 1 THEN 'mobile'
				WHEN 2 THEN 'partner'
				WHEN 3 THEN 'call_center'
				ELSE 'store'
			END,
			'",',
			'"campaign":"',
			CASE n % 4
				WHEN 0 THEN 'spring_sale'
				WHEN 1 THEN 'student_discount'
				WHEN 2 THEN 'enterprise_plan'
				ELSE 'organic'
			END,
			'",',
			'"priority":',
			CASE WHEN IsPriority = 1 THEN 'true' ELSE 'false' END,
			',',
			'"riskScore":',
			CONVERT(VARCHAR(30), FraudRiskScore),
		'}'
	),

	CAST
	(
		CONCAT
		(
			'<invoice>',
				'<number>', 9000000000 + n, '</number>',
				'<customerId>', CustomerID, '</customerId>',
				'<status>', OrderStatus, '</status>',
				'<payment>', PaymentMethod, '</payment>',
			'</invoice>'
		)
		AS XML
	),

	FraudRiskScore,

	HASHBYTES
	(
		'SHA2_256',
		CONCAT
		(
			9000000000 + n,
			CustomerID,
			CustomerName,
			ProductName,
			OrderStatus,
			Quantity,
			UnitPrice
		)
	)
FROM Prepared;
GO

CREATE INDEX IX_CustomerOrders_OrderDate
ON Training.CustomerOrders (OrderDate);
GO

CREATE INDEX IX_CustomerOrders_Status_Date
ON Training.CustomerOrders (OrderStatus, OrderDate)
INCLUDE (CustomerSegment, CountryCode, OrderTotal);
GO

CREATE INDEX IX_CustomerOrders_Category_Total
ON Training.CustomerOrders (ProductCategory, OrderTotal DESC);
GO

CREATE INDEX IX_CustomerOrders_Customer
ON Training.CustomerOrders (CustomerID, CreatedAt DESC);
GO

CREATE INDEX IX_CustomerOrders_City
ON Training.CustomerOrders (City);
GO

SELECT COUNT(*) AS InsertedRows
FROM Training.CustomerOrders;
GO

SELECT TOP (10)
	OrderID,
	CustomerName,
	CustomerSegment,
	CountryCode,
	City,
	ProductCategory,
	ProductName,
	OrderStatus,
	OrderDate,
	Quantity,
	UnitPrice,
	DiscountPercent,
	TaxRate,
	ShippingCost,
	OrderTotal,
	SatisfactionScore,
	CustomerNotes
FROM Training.CustomerOrders
ORDER BY OrderID;
GO
```


# Lecture 9: Advanced SQL Querying, Filtering, Aggregation, and Data Retrieval

## Duration

**Lecture:** 1 h
**Workgroup:** 2 hours

## Main Goal

Students learn how to retrieve, filter, sort, group, and analyze production-like data using advanced SQL Server query techniques.


# 1. Basic Structure of a SELECT Query

Before advanced filtering, students must understand the general SQL query structure.

```sql
SELECT column1, column2, column3
FROM schema_name.table_name
WHERE condition
ORDER BY column_name;
```

Example:

```sql
SELECT
	OrderID,
	CustomerName,
	ProductName,
	OrderStatus,
	OrderTotal
FROM Training.CustomerOrders
WHERE OrderStatus = N'Delivered'
ORDER BY OrderTotal DESC;
```

This query returns delivered orders, sorted from the largest order total to the smallest.

---

# 2. The `IN` Operator

## Purpose

`IN` is used when a column should match **one value from a list**.

Instead of writing many `OR` conditions:

```sql
WHERE OrderStatus = N'Delivered'
   OR OrderStatus = N'Shipped'
   OR OrderStatus = N'Processing'
```

we can write:

```sql
WHERE OrderStatus IN (N'Delivered', N'Shipped', N'Processing')
```

---

## Syntax

```sql
SELECT columns
FROM table_name
WHERE column_name IN (value1, value2, value3);
```

---

## Example 1: Find orders with selected statuses

```sql
SELECT
	OrderID,
	CustomerName,
	ProductName,
	OrderStatus,
	OrderDate,
	OrderTotal
FROM Training.CustomerOrders
WHERE OrderStatus IN (N'Delivered', N'Shipped', N'Processing')
ORDER BY OrderDate DESC;
```

---

## Example 2: Find orders from selected countries

```sql
SELECT
	OrderID,
	CustomerName,
	CountryCode,
	City,
	ProductName,
	OrderTotal
FROM Training.CustomerOrders
WHERE CountryCode IN ('GE', 'DE', 'US')
ORDER BY CountryCode, City;
```

---

## Example 3: Find orders for selected product categories

```sql
SELECT
	OrderID,
	ProductCategory,
	ProductName,
	Quantity,
	UnitPrice,
	OrderTotal
FROM Training.CustomerOrders
WHERE ProductCategory IN (N'Laptops', N'Smartphones', N'Database Services')
ORDER BY ProductCategory, OrderTotal DESC;
```

---

## Example 4: `IN` with a subquery

Find all orders whose `CustomerID` belongs to customers who have made large orders above 1000.

```sql
SELECT
	OrderID,
	CustomerID,
	CustomerName,
	ProductName,
	OrderTotal
FROM Training.CustomerOrders
WHERE CustomerID IN
(
	SELECT DISTINCT CustomerID
	FROM Training.CustomerOrders
	WHERE OrderTotal > 1000
)
ORDER BY CustomerID, OrderTotal DESC;
```

This is useful when we first identify a group of customers and then retrieve all related records.

---

## Example 5: `NOT IN`

Find orders that are **not** cancelled, returned, or refunded.

```sql
SELECT
	OrderID,
	CustomerName,
	OrderStatus,
	ProductName,
	OrderTotal
FROM Training.CustomerOrders
WHERE OrderStatus NOT IN (N'Cancelled', N'Returned', N'Refunded')
ORDER BY OrderDate DESC;
```

---

## Common Mistake with `NOT IN` and `NULL`

If the list contains `NULL`, `NOT IN` may return unexpected results.

Bad example:

```sql
SELECT *
FROM Training.CustomerOrders
WHERE SatisfactionScore NOT IN (1, 2, NULL);
```

Better:

```sql
SELECT *
FROM Training.CustomerOrders
WHERE SatisfactionScore NOT IN (1, 2)
   OR SatisfactionScore IS NULL;
```

---

# 3. The `BETWEEN` Operator

## Purpose

`BETWEEN` checks whether a value is inside a range.

It is inclusive, meaning it includes both boundary values.

```sql
BETWEEN 100 AND 500
```

means:

```sql
>= 100 AND <= 500
```

---

## Syntax

```sql
SELECT columns
FROM table_name
WHERE column_name BETWEEN start_value AND end_value;
```

---

## Example 1: Orders with total between 100 and 500

```sql
SELECT
	OrderID,
	CustomerName,
	ProductName,
	OrderTotal
FROM Training.CustomerOrders
WHERE OrderTotal BETWEEN 100 AND 500
ORDER BY OrderTotal;
```

---

## Example 2: Orders in a date range

```sql
SELECT
	OrderID,
	CustomerName,
	ProductName,
	OrderDate,
	OrderTotal
FROM Training.CustomerOrders
WHERE OrderDate BETWEEN DATEADD(DAY, -60, CONVERT(DATE, GETDATE()))
                    AND CONVERT(DATE, GETDATE())
ORDER BY OrderDate DESC;
```

This finds orders from the last 60 days.

---

## Example 3: Orders with quantity between 3 and 6

```sql
SELECT
	OrderID,
	ProductName,
	Quantity,
	UnitPrice,
	OrderTotal
FROM Training.CustomerOrders
WHERE Quantity BETWEEN 3 AND 6
ORDER BY Quantity, OrderTotal DESC;
```

---

## Example 4: Discounts between 10% and 25%

```sql
SELECT
	OrderID,
	CustomerName,
	ProductName,
	DiscountPercent,
	OrderTotal
FROM Training.CustomerOrders
WHERE DiscountPercent BETWEEN 10 AND 25
ORDER BY DiscountPercent DESC;
```

---

## Example 5: `NOT BETWEEN`

Find orders that are outside the normal mid-range price.

```sql
SELECT
	OrderID,
	ProductName,
	OrderTotal
FROM Training.CustomerOrders
WHERE OrderTotal NOT BETWEEN 100 AND 1000
ORDER BY OrderTotal DESC;
```

---

## Important Note About Dates

For `DATE`, `BETWEEN` is usually safe.

For `DATETIME` or `DATETIME2`, be careful because time is included.

Example:

```sql
WHERE CreatedAt BETWEEN '2026-01-01' AND '2026-01-31'
```

This includes only:

```sql
2026-01-31 00:00:00
```

Better:

```sql
WHERE CreatedAt >= '2026-01-01'
  AND CreatedAt <  '2026-02-01'
```

Example on our table:

```sql
SELECT
	OrderID,
	CustomerName,
	CreatedAt,
	OrderTotal
FROM Training.CustomerOrders
WHERE CreatedAt >= DATEADD(DAY, -30, SYSUTCDATETIME())
  AND CreatedAt <  SYSUTCDATETIME()
ORDER BY CreatedAt DESC;
```

---

# 4. The `LIKE` Operator

## Purpose

`LIKE` is used for pattern matching in text columns.

It is commonly used for searching names, product names, descriptions, notes, cities, and emails.

---

## Wildcards

| Pattern  | Meaning                       |
| -------- | ----------------------------- |
| `%`      | Any number of characters      |
| `_`      | Exactly one character         |
| `[abc]`  | One character from the list   |
| `[a-z]`  | One character from a range    |
| `[^abc]` | One character not in the list |

---

## Example 1: Product names containing “SQL”

```sql
SELECT
	OrderID,
	ProductName,
	ProductCategory,
	OrderTotal
FROM Training.CustomerOrders
WHERE ProductName LIKE N'%SQL%'
ORDER BY ProductName;
```

---

## Example 2: Customers whose name starts with “Nino”

```sql
SELECT
	OrderID,
	CustomerName,
	CustomerEmail,
	City,
	OrderTotal
FROM Training.CustomerOrders
WHERE CustomerName LIKE N'Nino%'
ORDER BY CustomerName;
```

---

## Example 3: Emails ending with example.com

```sql
SELECT
	OrderID,
	CustomerName,
	CustomerEmail
FROM Training.CustomerOrders
WHERE CustomerEmail LIKE '%@example.com'
ORDER BY CustomerEmail;
```

---

## Example 4: Product descriptions containing “security”

```sql
SELECT
	OrderID,
	ProductName,
	ProductDescription
FROM Training.CustomerOrders
WHERE ProductDescription LIKE N'%security%'
ORDER BY OrderID;
```

---

## Example 5: Customer notes containing “delivery”

```sql
SELECT
	OrderID,
	CustomerName,
	CustomerNotes
FROM Training.CustomerOrders
WHERE CustomerNotes LIKE N'%delivery%'
ORDER BY OrderID;
```

---

## Example 6: Single-character wildcard `_`

Find country codes that start with `G` and have exactly one more character.

```sql
SELECT
	OrderID,
	CountryCode,
	City,
	CustomerName
FROM Training.CustomerOrders
WHERE CountryCode LIKE 'G_';
```

This can match:

```text
GE
```

---

## Example 7: Character range

Find customers whose names start with A, B, C, or D.

```sql
SELECT
	OrderID,
	CustomerName,
	CustomerEmail
FROM Training.CustomerOrders
WHERE CustomerName LIKE N'[A-D]%'
ORDER BY CustomerName;
```

---

## Example 8: `NOT LIKE`

Find products that are not related to SQL.

```sql
SELECT
	OrderID,
	ProductName,
	ProductCategory
FROM Training.CustomerOrders
WHERE ProductName NOT LIKE N'%SQL%'
ORDER BY ProductName;
```

---

## Production Note

This query can use an index more efficiently:

```sql
WHERE CustomerName LIKE N'Nino%'
```

This query usually cannot use a normal index efficiently:

```sql
WHERE CustomerName LIKE N'%Nino%'
```

Because `%` at the beginning means SQL Server cannot seek directly from the start of the text.

---

# 5. `IS NULL` and `IS NOT NULL`

## Purpose

`NULL` means unknown, missing, or not applicable.

You cannot compare `NULL` using `=`.

Wrong:

```sql
WHERE DeliveredAt = NULL
```

Correct:

```sql
WHERE DeliveredAt IS NULL
```

---

## Example 1: Orders not yet delivered

```sql
SELECT
	OrderID,
	CustomerName,
	OrderStatus,
	DeliveredAt
FROM Training.CustomerOrders
WHERE DeliveredAt IS NULL
ORDER BY OrderDate DESC;
```

---

## Example 2: Orders already delivered or returned

```sql
SELECT
	OrderID,
	CustomerName,
	OrderStatus,
	DeliveredAt
FROM Training.CustomerOrders
WHERE DeliveredAt IS NOT NULL
ORDER BY DeliveredAt DESC;
```

---

## Example 3: Customers with missing satisfaction score

```sql
SELECT
	OrderID,
	CustomerName,
	ProductName,
	SatisfactionScore
FROM Training.CustomerOrders
WHERE SatisfactionScore IS NULL
ORDER BY OrderID;
```

---

## Example 4: Notes are missing

```sql
SELECT
	OrderID,
	CustomerName,
	CustomerNotes
FROM Training.CustomerOrders
WHERE CustomerNotes IS NULL;
```

---

## Example 5: Replace `NULL` with readable text using `ISNULL`

```sql
SELECT
	OrderID,
	CustomerName,
	OrderStatus,
	ISNULL(CustomerNotes, N'No customer note') AS CustomerNoteText
FROM Training.CustomerOrders
ORDER BY OrderID;
```

---

## Example 6: Use `COALESCE`

`COALESCE` returns the first non-null value.

```sql
SELECT
	OrderID,
	CustomerName,
	COALESCE(CustomerNotes, N'No notes available') AS NotesDisplay
FROM Training.CustomerOrders
ORDER BY OrderID;
```

---

## Example 7: Treat missing satisfaction as zero for reporting

```sql
SELECT
	OrderID,
	CustomerName,
	SatisfactionScore,
	ISNULL(SatisfactionScore, 0) AS SatisfactionForReport
FROM Training.CustomerOrders
ORDER BY OrderID;
```

---

# 6. `DISTINCT`

## Purpose

`DISTINCT` removes duplicate rows from the result.

It applies to the entire selected row, not just one column.

---

## Example 1: List all countries

```sql
SELECT DISTINCT
	CountryCode
FROM Training.CustomerOrders
ORDER BY CountryCode;
```

---

## Example 2: List all cities

```sql
SELECT DISTINCT
	City
FROM Training.CustomerOrders
ORDER BY City;
```

---

## Example 3: List all product categories

```sql
SELECT DISTINCT
	ProductCategory
FROM Training.CustomerOrders
ORDER BY ProductCategory;
```

---

## Example 4: Distinct country and city combinations

```sql
SELECT DISTINCT
	CountryCode,
	City
FROM Training.CustomerOrders
ORDER BY CountryCode, City;
```

This returns unique combinations, not unique countries only.

---

## Example 5: Distinct customer segments and payment methods

```sql
SELECT DISTINCT
	CustomerSegment,
	PaymentMethod
FROM Training.CustomerOrders
ORDER BY CustomerSegment, PaymentMethod;
```

---

## Important Difference

This returns distinct countries:

```sql
SELECT DISTINCT CountryCode
FROM Training.CustomerOrders;
```

This returns distinct country-city pairs:

```sql
SELECT DISTINCT CountryCode, City
FROM Training.CustomerOrders;
```

If Georgia appears with Tbilisi, Batumi, Kutaisi, and Telavi, it can appear multiple times in the second query.

---

# 7. `ORDER BY`

## Purpose

`ORDER BY` sorts the result.

Without `ORDER BY`, SQL Server does not guarantee row order.

---

## Syntax

```sql
ORDER BY column_name ASC;
ORDER BY column_name DESC;
```

`ASC` means ascending.
`DESC` means descending.

---

## Example 1: Sort by order total descending

```sql
SELECT
	OrderID,
	CustomerName,
	ProductName,
	OrderTotal
FROM Training.CustomerOrders
ORDER BY OrderTotal DESC;
```

---

## Example 2: Sort by date newest first

```sql
SELECT
	OrderID,
	CustomerName,
	OrderDate,
	OrderTotal
FROM Training.CustomerOrders
ORDER BY OrderDate DESC;
```

---

## Example 3: Sort by category and total

```sql
SELECT
	OrderID,
	ProductCategory,
	ProductName,
	OrderTotal
FROM Training.CustomerOrders
ORDER BY ProductCategory ASC, OrderTotal DESC;
```

This first groups rows by category alphabetically, then sorts each category by largest total.

---

## Example 4: Sort by calculated expression

```sql
SELECT
	OrderID,
	ProductName,
	Quantity,
	UnitPrice,
	Quantity * UnitPrice AS GrossAmount
FROM Training.CustomerOrders
ORDER BY Quantity * UnitPrice DESC;
```

---

## Example 5: Sort by alias

```sql
SELECT
	OrderID,
	ProductName,
	Quantity,
	UnitPrice,
	Quantity * UnitPrice AS GrossAmount
FROM Training.CustomerOrders
ORDER BY GrossAmount DESC;
```

---

## Example 6: Sort with `NULL` values

SQL Server sorts `NULL` values first in ascending order.

```sql
SELECT
	OrderID,
	CustomerName,
	SatisfactionScore
FROM Training.CustomerOrders
ORDER BY SatisfactionScore ASC;
```

To push `NULL` values to the end:

```sql
SELECT
	OrderID,
	CustomerName,
	SatisfactionScore
FROM Training.CustomerOrders
ORDER BY
	CASE WHEN SatisfactionScore IS NULL THEN 1 ELSE 0 END,
	SatisfactionScore ASC;
```

---

## Example 7: `TOP` with `ORDER BY`

Find the 10 most expensive orders.

```sql
SELECT TOP (10)
	OrderID,
	CustomerName,
	ProductName,
	OrderTotal
FROM Training.CustomerOrders
ORDER BY OrderTotal DESC;
```

---

## Example 8: Pagination with `OFFSET` and `FETCH`

```sql
SELECT
	OrderID,
	CustomerName,
	ProductName,
	OrderDate,
	OrderTotal
FROM Training.CustomerOrders
ORDER BY OrderDate DESC
OFFSET 0 ROWS FETCH NEXT 10 ROWS ONLY;
```

Second page:

```sql
SELECT
	OrderID,
	CustomerName,
	ProductName,
	OrderDate,
	OrderTotal
FROM Training.CustomerOrders
ORDER BY OrderDate DESC
OFFSET 10 ROWS FETCH NEXT 10 ROWS ONLY;
```

---

# 8. `ANY` Operator

## Purpose

`ANY` compares a value with a list returned by a subquery.

It means:

```text
true if the comparison is true for at least one value
```

In SQL Server, `SOME` is equivalent to `ANY`.

---

## Syntax

```sql
WHERE value operator ANY (subquery)
```

Examples of operators:

```sql
= ANY
> ANY
< ANY
>= ANY
<= ANY
<> ANY
```

---

## Example 1: Orders greater than any order in a small category

Find orders whose total is greater than at least one order from the `Accessories` category.

```sql
SELECT
	OrderID,
	ProductCategory,
	ProductName,
	OrderTotal
FROM Training.CustomerOrders
WHERE OrderTotal > ANY
(
	SELECT OrderTotal
	FROM Training.CustomerOrders
	WHERE ProductCategory = N'Accessories'
)
ORDER BY OrderTotal DESC;
```

Meaning:

```text
Return orders whose total is greater than at least one Accessories order.
```

This is similar to:

```sql
OrderTotal > minimum accessories order total
```

---

## Example 2: Orders with discount greater than any cancelled order discount

```sql
SELECT
	OrderID,
	OrderStatus,
	ProductName,
	DiscountPercent,
	OrderTotal
FROM Training.CustomerOrders
WHERE DiscountPercent > ANY
(
	SELECT DiscountPercent
	FROM Training.CustomerOrders
	WHERE OrderStatus = N'Cancelled'
)
ORDER BY DiscountPercent DESC;
```

---

## Example 3: Customers with quantity equal to any quantity used in returned orders

```sql
SELECT
	OrderID,
	CustomerName,
	OrderStatus,
	Quantity
FROM Training.CustomerOrders
WHERE Quantity = ANY
(
	SELECT Quantity
	FROM Training.CustomerOrders
	WHERE OrderStatus = N'Returned'
)
ORDER BY Quantity;
```

This is similar to using `IN`.

```sql
WHERE Quantity IN
(
	SELECT Quantity
	FROM Training.CustomerOrders
	WHERE OrderStatus = N'Returned'
)
```

---

## Example 4: `SOME` instead of `ANY`

```sql
SELECT
	OrderID,
	ProductName,
	OrderTotal
FROM Training.CustomerOrders
WHERE OrderTotal > SOME
(
	SELECT OrderTotal
	FROM Training.CustomerOrders
	WHERE CountryCode = 'GE'
)
ORDER BY OrderTotal DESC;
```

`SOME` and `ANY` mean the same thing in SQL Server.

---

# 9. `ALL` Operator

## Purpose

`ALL` compares a value with every value returned by a subquery.

It means:

```text
true only if the comparison is true for all values
```

---

## Syntax

```sql
WHERE value operator ALL (subquery)
```

---

## Example 1: Orders greater than all Accessories orders

```sql
SELECT
	OrderID,
	ProductCategory,
	ProductName,
	OrderTotal
FROM Training.CustomerOrders
WHERE OrderTotal > ALL
(
	SELECT OrderTotal
	FROM Training.CustomerOrders
	WHERE ProductCategory = N'Accessories'
)
ORDER BY OrderTotal DESC;
```

Meaning:

```text
Return orders whose total is greater than every Accessories order.
```

This is similar to:

```sql
OrderTotal > maximum accessories order total
```

---

## Example 2: Products cheaper than all Database Services orders

```sql
SELECT
	OrderID,
	ProductCategory,
	ProductName,
	OrderTotal
FROM Training.CustomerOrders
WHERE OrderTotal < ALL
(
	SELECT OrderTotal
	FROM Training.CustomerOrders
	WHERE ProductCategory = N'Database Services'
)
ORDER BY OrderTotal ASC;
```

---

## Example 3: Orders with tax rate greater than all Retail order tax rates

```sql
SELECT
	OrderID,
	CustomerSegment,
	ProductName,
	TaxRate,
	OrderTotal
FROM Training.CustomerOrders
WHERE TaxRate > ALL
(
	SELECT TaxRate
	FROM Training.CustomerOrders
	WHERE CustomerSegment = N'Retail'
)
ORDER BY TaxRate DESC;
```

---

## Example 4: Compare `ANY` vs `ALL`

```sql
SELECT
	OrderID,
	ProductName,
	OrderTotal
FROM Training.CustomerOrders
WHERE OrderTotal > ANY
(
	SELECT OrderTotal
	FROM Training.CustomerOrders
	WHERE ProductCategory = N'Accessories'
)
ORDER BY OrderTotal DESC;
```

This means greater than at least one Accessories order.

```sql
SELECT
	OrderID,
	ProductName,
	OrderTotal
FROM Training.CustomerOrders
WHERE OrderTotal > ALL
(
	SELECT OrderTotal
	FROM Training.CustomerOrders
	WHERE ProductCategory = N'Accessories'
)
ORDER BY OrderTotal DESC;
```

This means greater than every Accessories order.

`ALL` is stricter than `ANY`.

---

# 10. Aggregate Functions

Aggregate functions calculate a single value from many rows.

Common aggregate functions:

| Function  | Meaning            |
| --------- | ------------------ |
| `COUNT()` | Counts rows        |
| `SUM()`   | Adds values        |
| `AVG()`   | Calculates average |
| `MIN()`   | Finds minimum      |
| `MAX()`   | Finds maximum      |

---

# 10.1 `COUNT`

## Example 1: Count all orders

```sql
SELECT COUNT(*) AS TotalOrders
FROM Training.CustomerOrders;
```

---

## Example 2: Count delivered orders

```sql
SELECT COUNT(*) AS DeliveredOrders
FROM Training.CustomerOrders
WHERE OrderStatus = N'Delivered';
```

---

## Example 3: Count non-null satisfaction scores

```sql
SELECT COUNT(SatisfactionScore) AS OrdersWithSatisfactionScore
FROM Training.CustomerOrders;
```

Important:

```sql
COUNT(*) 
```

counts all rows.

```sql
COUNT(SatisfactionScore)
```

counts only rows where `SatisfactionScore` is not null.

---

## Example 4: Count distinct customers

```sql
SELECT COUNT(DISTINCT CustomerID) AS UniqueCustomers
FROM Training.CustomerOrders;
```

---

# 10.2 `SUM`

## Example 1: Total revenue

```sql
SELECT SUM(OrderTotal) AS TotalRevenue
FROM Training.CustomerOrders;
```

---

## Example 2: Revenue from delivered orders only

```sql
SELECT SUM(OrderTotal) AS DeliveredRevenue
FROM Training.CustomerOrders
WHERE OrderStatus = N'Delivered';
```

---

## Example 3: Total quantity sold

```sql
SELECT SUM(Quantity) AS TotalItemsSold
FROM Training.CustomerOrders;
```

---

## Example 4: Total shipping cost

```sql
SELECT SUM(CONVERT(DECIMAL(12,2), ShippingCost)) AS TotalShippingCost
FROM Training.CustomerOrders;
```

---

# 10.3 `AVG`

## Example 1: Average order total

```sql
SELECT AVG(OrderTotal) AS AverageOrderTotal
FROM Training.CustomerOrders;
```

---

## Example 2: Average satisfaction score

```sql
SELECT AVG(CONVERT(DECIMAL(5,2), SatisfactionScore)) AS AverageSatisfaction
FROM Training.CustomerOrders;
```

`AVG` ignores `NULL` values.

---

## Example 3: Average delivery days

```sql
SELECT AVG(CONVERT(DECIMAL(5,2), DeliveryDays)) AS AverageDeliveryDays
FROM Training.CustomerOrders;
```

---

# 10.4 `MIN`

## Example 1: Lowest order total

```sql
SELECT MIN(OrderTotal) AS LowestOrderTotal
FROM Training.CustomerOrders;
```

---

## Example 2: Earliest order date

```sql
SELECT MIN(OrderDate) AS FirstOrderDate
FROM Training.CustomerOrders;
```

---

## Example 3: Smallest discount

```sql
SELECT MIN(DiscountPercent) AS MinimumDiscount
FROM Training.CustomerOrders;
```

---

# 10.5 `MAX`

## Example 1: Highest order total

```sql
SELECT MAX(OrderTotal) AS HighestOrderTotal
FROM Training.CustomerOrders;
```

---

## Example 2: Latest order date

```sql
SELECT MAX(OrderDate) AS LatestOrderDate
FROM Training.CustomerOrders;
```

---

## Example 3: Maximum fraud risk score

```sql
SELECT MAX(FraudRiskScore) AS HighestFraudRiskScore
FROM Training.CustomerOrders;
```

---

# 10.6 Multiple Aggregates in One Query

```sql
SELECT
	COUNT(*) AS TotalOrders,
	COUNT(DISTINCT CustomerID) AS UniqueCustomers,
	SUM(OrderTotal) AS TotalRevenue,
	AVG(OrderTotal) AS AverageOrderTotal,
	MIN(OrderTotal) AS LowestOrderTotal,
	MAX(OrderTotal) AS HighestOrderTotal
FROM Training.CustomerOrders;
```

---

# 11. `GROUP BY`

## Purpose

`GROUP BY` groups rows that have the same value in one or more columns.

It is usually used with aggregate functions.

---

## Syntax

```sql
SELECT
	GroupColumn,
	AggregateFunction(Column)
FROM table_name
GROUP BY GroupColumn;
```

---

## Example 1: Revenue by order status

```sql
SELECT
	OrderStatus,
	COUNT(*) AS TotalOrders,
	SUM(OrderTotal) AS TotalRevenue
FROM Training.CustomerOrders
GROUP BY OrderStatus
ORDER BY TotalRevenue DESC;
```

---

## Example 2: Revenue by product category

```sql
SELECT
	ProductCategory,
	COUNT(*) AS TotalOrders,
	SUM(OrderTotal) AS TotalRevenue,
	AVG(OrderTotal) AS AverageOrderTotal
FROM Training.CustomerOrders
GROUP BY ProductCategory
ORDER BY TotalRevenue DESC;
```

---

## Example 3: Revenue by country

```sql
SELECT
	CountryCode,
	COUNT(*) AS TotalOrders,
	SUM(OrderTotal) AS TotalRevenue
FROM Training.CustomerOrders
GROUP BY CountryCode
ORDER BY TotalRevenue DESC;
```

---

## Example 4: Orders by customer segment

```sql
SELECT
	CustomerSegment,
	COUNT(*) AS TotalOrders,
	COUNT(DISTINCT CustomerID) AS UniqueCustomers,
	SUM(OrderTotal) AS TotalRevenue
FROM Training.CustomerOrders
GROUP BY CustomerSegment
ORDER BY TotalRevenue DESC;
```

---

## Example 5: Group by multiple columns

Revenue by country and city:

```sql
SELECT
	CountryCode,
	City,
	COUNT(*) AS TotalOrders,
	SUM(OrderTotal) AS TotalRevenue
FROM Training.CustomerOrders
GROUP BY CountryCode, City
ORDER BY CountryCode, TotalRevenue DESC;
```

---

## Example 6: Group by product category and status

```sql
SELECT
	ProductCategory,
	OrderStatus,
	COUNT(*) AS TotalOrders,
	SUM(OrderTotal) AS TotalRevenue
FROM Training.CustomerOrders
GROUP BY ProductCategory, OrderStatus
ORDER BY ProductCategory, TotalRevenue DESC;
```

---

## Example 7: Group by date

Orders per day:

```sql
SELECT
	OrderDate,
	COUNT(*) AS OrdersPerDay,
	SUM(OrderTotal) AS DailyRevenue
FROM Training.CustomerOrders
GROUP BY OrderDate
ORDER BY OrderDate DESC;
```

---

## Example 8: Group by month

```sql
SELECT
	YEAR(OrderDate) AS OrderYear,
	MONTH(OrderDate) AS OrderMonth,
	COUNT(*) AS TotalOrders,
	SUM(OrderTotal) AS MonthlyRevenue
FROM Training.CustomerOrders
GROUP BY
	YEAR(OrderDate),
	MONTH(OrderDate)
ORDER BY
	OrderYear DESC,
	OrderMonth DESC;
```

---

# 12. `HAVING`

## Purpose

`HAVING` filters grouped results.

`WHERE` filters rows before grouping.
`HAVING` filters groups after grouping.

---

## Example 1: Categories with revenue above 5000

```sql
SELECT
	ProductCategory,
	COUNT(*) AS TotalOrders,
	SUM(OrderTotal) AS TotalRevenue
FROM Training.CustomerOrders
GROUP BY ProductCategory
HAVING SUM(OrderTotal) > 5000
ORDER BY TotalRevenue DESC;
```

---

## Example 2: Countries with more than 10 orders

```sql
SELECT
	CountryCode,
	COUNT(*) AS TotalOrders
FROM Training.CustomerOrders
GROUP BY CountryCode
HAVING COUNT(*) > 10
ORDER BY TotalOrders DESC;
```

---

## Example 3: Customer segments with average order above 500

```sql
SELECT
	CustomerSegment,
	COUNT(*) AS TotalOrders,
	AVG(OrderTotal) AS AverageOrderTotal
FROM Training.CustomerOrders
GROUP BY CustomerSegment
HAVING AVG(OrderTotal) > 500
ORDER BY AverageOrderTotal DESC;
```

---

## Example 4: Product categories with high average discount

```sql
SELECT
	ProductCategory,
	AVG(DiscountPercent) AS AverageDiscount
FROM Training.CustomerOrders
GROUP BY ProductCategory
HAVING AVG(DiscountPercent) >= 5
ORDER BY AverageDiscount DESC;
```

---

# 13. Difference Between `WHERE` and `HAVING`

## `WHERE`

Filters individual rows before grouping.

```sql
SELECT
	ProductCategory,
	COUNT(*) AS DeliveredOrders,
	SUM(OrderTotal) AS DeliveredRevenue
FROM Training.CustomerOrders
WHERE OrderStatus = N'Delivered'
GROUP BY ProductCategory
ORDER BY DeliveredRevenue DESC;
```

Here SQL Server first keeps only delivered rows, then groups them.

---

## `HAVING`

Filters groups after aggregation.

```sql
SELECT
	ProductCategory,
	COUNT(*) AS TotalOrders,
	SUM(OrderTotal) AS TotalRevenue
FROM Training.CustomerOrders
GROUP BY ProductCategory
HAVING SUM(OrderTotal) > 3000
ORDER BY TotalRevenue DESC;
```

Here SQL Server groups all rows first, then keeps only groups whose revenue is above 3000.

---

## Using Both Together

```sql
SELECT
	ProductCategory,
	COUNT(*) AS DeliveredOrders,
	SUM(OrderTotal) AS DeliveredRevenue
FROM Training.CustomerOrders
WHERE OrderStatus = N'Delivered'
GROUP BY ProductCategory
HAVING SUM(OrderTotal) > 1000
ORDER BY DeliveredRevenue DESC;
```

Meaning:

1. Keep only delivered orders.
2. Group them by product category.
3. Keep only categories where delivered revenue is above 1000.

---

## Wrong Example

```sql
SELECT
	ProductCategory,
	SUM(OrderTotal) AS TotalRevenue
FROM Training.CustomerOrders
WHERE SUM(OrderTotal) > 1000
GROUP BY ProductCategory;
```

This is invalid because aggregate functions cannot be used in `WHERE`.

Correct:

```sql
SELECT
	ProductCategory,
	SUM(OrderTotal) AS TotalRevenue
FROM Training.CustomerOrders
GROUP BY ProductCategory
HAVING SUM(OrderTotal) > 1000;
```

---

# 14. Math Functions

SQL Server provides many math functions.

Useful functions:

| Function    | Purpose             |
| ----------- | ------------------- |
| `ROUND()`   | Rounds a number     |
| `CEILING()` | Rounds upward       |
| `FLOOR()`   | Rounds downward     |
| `ABS()`     | Absolute value      |
| `POWER()`   | Power calculation   |
| `SQRT()`    | Square root         |
| `RAND()`    | Random value        |
| `SIGN()`    | Returns -1, 0, or 1 |

---

## Example 1: Round order totals

```sql
SELECT
	OrderID,
	OrderTotal,
	ROUND(OrderTotal, 0) AS RoundedTotal
FROM Training.CustomerOrders
ORDER BY OrderID;
```

---

## Example 2: Round to one decimal place

```sql
SELECT
	OrderID,
	OrderTotal,
	ROUND(OrderTotal, 1) AS RoundedTotalOneDecimal
FROM Training.CustomerOrders
ORDER BY OrderID;
```

---

## Example 3: `CEILING`

```sql
SELECT
	OrderID,
	OrderTotal,
	CEILING(OrderTotal) AS RoundedUp
FROM Training.CustomerOrders
ORDER BY OrderID;
```

---

## Example 4: `FLOOR`

```sql
SELECT
	OrderID,
	OrderTotal,
	FLOOR(OrderTotal) AS RoundedDown
FROM Training.CustomerOrders
ORDER BY OrderID;
```

---

## Example 5: Calculate gross amount before discount and tax

```sql
SELECT
	OrderID,
	ProductName,
	Quantity,
	UnitPrice,
	Quantity * UnitPrice AS GrossAmount,
	DiscountPercent,
	OrderTotal
FROM Training.CustomerOrders
ORDER BY GrossAmount DESC;
```

---

## Example 6: Calculate discount amount

```sql
SELECT
	OrderID,
	ProductName,
	Quantity,
	UnitPrice,
	DiscountPercent,
	ROUND(Quantity * UnitPrice * DiscountPercent / 100.0, 2) AS DiscountAmount
FROM Training.CustomerOrders
ORDER BY DiscountAmount DESC;
```

---

## Example 7: Use `ABS`

Suppose we compare actual delivery days with target delivery days of 5.

```sql
SELECT
	OrderID,
	OrderStatus,
	DeliveryDays,
	ABS(ISNULL(DeliveryDays, 5) - 5) AS DifferenceFromTarget
FROM Training.CustomerOrders
ORDER BY DifferenceFromTarget DESC;
```

---

## Example 8: Use `POWER`

Calculate a simple weighted fraud score.

```sql
SELECT
	OrderID,
	FraudRiskScore,
	POWER(FraudRiskScore, 2) AS RiskScoreSquared
FROM Training.CustomerOrders
ORDER BY RiskScoreSquared DESC;
```

---

## Example 9: Use `SQRT`

```sql
SELECT
	OrderID,
	FraudRiskScore,
	SQRT(FraudRiskScore) AS RiskScoreRoot
FROM Training.CustomerOrders
WHERE FraudRiskScore >= 0
ORDER BY RiskScoreRoot DESC;
```

---

## Example 10: Use math in aggregates

```sql
SELECT
	ProductCategory,
	COUNT(*) AS TotalOrders,
	ROUND(AVG(OrderTotal), 2) AS AverageOrderTotal,
	ROUND(SUM(OrderTotal), 2) AS TotalRevenue
FROM Training.CustomerOrders
GROUP BY ProductCategory
ORDER BY TotalRevenue DESC;
```

---

# 15. String Functions

Useful SQL Server string functions:

| Function              | Purpose                       |
| --------------------- | ----------------------------- |
| `LEN()`               | Length of text                |
| `LEFT()`              | First characters              |
| `RIGHT()`             | Last characters               |
| `SUBSTRING()`         | Part of string                |
| `CHARINDEX()`         | Position of text              |
| `REPLACE()`           | Replace text                  |
| `UPPER()`             | Convert to uppercase          |
| `LOWER()`             | Convert to lowercase          |
| `LTRIM()` / `RTRIM()` | Remove spaces                 |
| `TRIM()`              | Remove spaces from both sides |
| `CONCAT()`            | Join strings                  |

---

## Example 1: Convert names to uppercase

```sql
SELECT
	OrderID,
	CustomerName,
	UPPER(CustomerName) AS CustomerNameUpper
FROM Training.CustomerOrders
ORDER BY CustomerName;
```

---

## Example 2: Convert emails to lowercase

```sql
SELECT
	OrderID,
	CustomerEmail,
	LOWER(CustomerEmail) AS NormalizedEmail
FROM Training.CustomerOrders
ORDER BY CustomerEmail;
```

---

## Example 3: Get first 5 characters of product SKU

```sql
SELECT
	OrderID,
	ProductSKU,
	LEFT(ProductSKU, 5) AS SkuPrefix
FROM Training.CustomerOrders
ORDER BY ProductSKU;
```

---

## Example 4: Get last 5 characters of product SKU

```sql
SELECT
	OrderID,
	ProductSKU,
	RIGHT(ProductSKU, 5) AS SkuNumber
FROM Training.CustomerOrders
ORDER BY ProductSKU;
```

---

## Example 5: Extract part of a string

```sql
SELECT
	OrderID,
	ProductSKU,
	SUBSTRING(ProductSKU, 5, 5) AS ExtractedSkuNumber
FROM Training.CustomerOrders
ORDER BY ProductSKU;
```

---

## Example 6: Find position of “@” in email

```sql
SELECT
	OrderID,
	CustomerEmail,
	CHARINDEX('@', CustomerEmail) AS AtPosition
FROM Training.CustomerOrders
ORDER BY CustomerEmail;
```

---

## Example 7: Extract email domain

```sql
SELECT
	OrderID,
	CustomerEmail,
	SUBSTRING
	(
		CustomerEmail,
		CHARINDEX('@', CustomerEmail) + 1,
		LEN(CustomerEmail)
	) AS EmailDomain
FROM Training.CustomerOrders
ORDER BY EmailDomain;
```

---

## Example 8: Replace text

```sql
SELECT
	OrderID,
	ProductName,
	REPLACE(ProductName, N'SQL Server', N'Microsoft SQL Server') AS UpdatedProductName
FROM Training.CustomerOrders
WHERE ProductName LIKE N'%SQL Server%';
```

---

## Example 9: Build a readable order label

```sql
SELECT
	OrderID,
	CONCAT
	(
		N'Order #',
		OrderID,
		N' - ',
		CustomerName,
		N' bought ',
		ProductName
	) AS OrderLabel
FROM Training.CustomerOrders
ORDER BY OrderID;
```

---

## Example 10: Length of customer notes

```sql
SELECT
	OrderID,
	CustomerNotes,
	LEN(CustomerNotes) AS NoteLength
FROM Training.CustomerOrders
WHERE CustomerNotes IS NOT NULL
ORDER BY NoteLength DESC;
```

---

# 16. Date and Time Functions

Useful SQL Server date/time functions:

| Function           | Purpose                                       |
| ------------------ | --------------------------------------------- |
| `GETDATE()`        | Current local date and time                   |
| `SYSDATETIME()`    | Current local date/time with higher precision |
| `SYSUTCDATETIME()` | Current UTC date/time                         |
| `DATEADD()`        | Add date/time interval                        |
| `DATEDIFF()`       | Difference between dates                      |
| `YEAR()`           | Extract year                                  |
| `MONTH()`          | Extract month                                 |
| `DAY()`            | Extract day                                   |
| `DATEPART()`       | Extract specific date part                    |
| `DATENAME()`       | Get name of date part                         |
| `EOMONTH()`        | End of month                                  |

---

## Example 1: Current date and time

```sql
SELECT
	GETDATE() AS CurrentLocalDateTime,
	SYSDATETIME() AS CurrentPreciseDateTime,
	SYSUTCDATETIME() AS CurrentUtcDateTime;
```

---

## Example 2: Orders from last 30 days

```sql
SELECT
	OrderID,
	CustomerName,
	OrderDate,
	OrderTotal
FROM Training.CustomerOrders
WHERE OrderDate >= DATEADD(DAY, -30, CONVERT(DATE, GETDATE()))
ORDER BY OrderDate DESC;
```

---

## Example 3: Orders older than 90 days

```sql
SELECT
	OrderID,
	CustomerName,
	OrderDate,
	OrderTotal
FROM Training.CustomerOrders
WHERE OrderDate < DATEADD(DAY, -90, CONVERT(DATE, GETDATE()))
ORDER BY OrderDate;
```

---

## Example 4: Calculate processing time in minutes

```sql
SELECT
	OrderID,
	OrderStatus,
	CreatedAt,
	ProcessedAt,
	DATEDIFF(MINUTE, CreatedAt, ProcessedAt) AS ProcessingMinutes
FROM Training.CustomerOrders
WHERE ProcessedAt IS NOT NULL
ORDER BY ProcessingMinutes DESC;
```

---

## Example 5: Calculate delivery time in days

```sql
SELECT
	OrderID,
	OrderStatus,
	CreatedAt,
	DeliveredAt,
	DATEDIFF(DAY, CreatedAt, DeliveredAt) AS ActualDeliveryDays
FROM Training.CustomerOrders
WHERE DeliveredAt IS NOT NULL
ORDER BY ActualDeliveryDays DESC;
```

---

## Example 6: Extract year and month

```sql
SELECT
	OrderID,
	OrderDate,
	YEAR(OrderDate) AS OrderYear,
	MONTH(OrderDate) AS OrderMonth,
	DAY(OrderDate) AS OrderDay
FROM Training.CustomerOrders
ORDER BY OrderDate DESC;
```

---

## Example 7: Group by weekday

```sql
SELECT
	DATENAME(WEEKDAY, OrderDate) AS WeekdayName,
	COUNT(*) AS TotalOrders,
	SUM(OrderTotal) AS TotalRevenue
FROM Training.CustomerOrders
GROUP BY DATENAME(WEEKDAY, OrderDate)
ORDER BY TotalOrders DESC;
```

---

## Example 8: Group by month end

```sql
SELECT
	EOMONTH(OrderDate) AS MonthEndDate,
	COUNT(*) AS TotalOrders,
	SUM(OrderTotal) AS TotalRevenue
FROM Training.CustomerOrders
GROUP BY EOMONTH(OrderDate)
ORDER BY MonthEndDate DESC;
```

---

## Example 9: Add estimated delivery date

```sql
SELECT
	OrderID,
	OrderDate,
	DeliveryDays,
	DATEADD(DAY, ISNULL(DeliveryDays, 5), OrderDate) AS EstimatedDeliveryDate
FROM Training.CustomerOrders
ORDER BY OrderDate DESC;
```

---

## Example 10: Orders created by hour

```sql
SELECT
	DATEPART(HOUR, CreatedAt) AS CreatedHour,
	COUNT(*) AS TotalOrders
FROM Training.CustomerOrders
GROUP BY DATEPART(HOUR, CreatedAt)
ORDER BY CreatedHour;
```

---

# 17. Search Techniques Using Different Criteria

In real systems, searching often combines several filters.

---

## Example 1: Search by status and country

```sql
SELECT
	OrderID,
	CustomerName,
	CountryCode,
	OrderStatus,
	OrderTotal
FROM Training.CustomerOrders
WHERE CountryCode = 'GE'
  AND OrderStatus = N'Delivered'
ORDER BY OrderTotal DESC;
```

---

## Example 2: Search by category, date, and minimum total

```sql
SELECT
	OrderID,
	ProductCategory,
	ProductName,
	OrderDate,
	OrderTotal
FROM Training.CustomerOrders
WHERE ProductCategory = N'Database Services'
  AND OrderDate >= DATEADD(DAY, -120, CONVERT(DATE, GETDATE()))
  AND OrderTotal >= 500
ORDER BY OrderDate DESC;
```

---

## Example 3: Search by customer segment and payment method

```sql
SELECT
	OrderID,
	CustomerName,
	CustomerSegment,
	PaymentMethod,
	OrderTotal
FROM Training.CustomerOrders
WHERE CustomerSegment = N'Enterprise'
  AND PaymentMethod IN (N'Invoice', N'Bank Transfer')
ORDER BY OrderTotal DESC;
```

---

## Example 4: Search for risky orders

```sql
SELECT
	OrderID,
	CustomerName,
	OrderStatus,
	PaymentMethod,
	FraudRiskScore,
	OrderTotal
FROM Training.CustomerOrders
WHERE FraudRiskScore >= 7.0
   OR IsPriority = 1
ORDER BY FraudRiskScore DESC, OrderTotal DESC;
```

---

## Example 5: Search for high-value pending orders

```sql
SELECT
	OrderID,
	CustomerName,
	ProductName,
	OrderStatus,
	OrderTotal
FROM Training.CustomerOrders
WHERE OrderStatus = N'Pending'
  AND OrderTotal > 500
ORDER BY OrderTotal DESC;
```

---

## Example 6: Search for customer complaints or delivery-related notes

```sql
SELECT
	OrderID,
	CustomerName,
	CustomerNotes,
	OrderStatus
FROM Training.CustomerOrders
WHERE CustomerNotes LIKE N'%delivery%'
   OR CustomerNotes LIKE N'%slow%'
   OR CustomerNotes LIKE N'%urgent%'
ORDER BY OrderID;
```

---

## Example 7: Search with optional missing values

Find orders that have no satisfaction score or have low satisfaction.

```sql
SELECT
	OrderID,
	CustomerName,
	ProductName,
	SatisfactionScore,
	CustomerNotes
FROM Training.CustomerOrders
WHERE SatisfactionScore IS NULL
   OR SatisfactionScore <= 2
ORDER BY SatisfactionScore;
```

---

# 18. Pattern-Based Search with `LIKE`

Since full-text search is excluded, we use `LIKE` for basic text searching.

---

## Example 1: Search product descriptions for “database”

```sql
SELECT
	OrderID,
	ProductName,
	ProductDescription
FROM Training.CustomerOrders
WHERE ProductDescription LIKE N'%database%'
ORDER BY OrderID;
```

---

## Example 2: Search descriptions for “monitoring” or “performance”

```sql
SELECT
	OrderID,
	ProductName,
	ProductDescription
FROM Training.CustomerOrders
WHERE ProductDescription LIKE N'%monitoring%'
   OR ProductDescription LIKE N'%performance%'
ORDER BY ProductName;
```

---

## Example 3: Search notes for “invoice”

```sql
SELECT
	OrderID,
	CustomerName,
	CustomerNotes
FROM Training.CustomerOrders
WHERE CustomerNotes LIKE N'%invoice%'
ORDER BY OrderID;
```

---

## Example 4: Search names beginning with “Sa”

```sql
SELECT
	OrderID,
	CustomerName,
	CustomerEmail
FROM Training.CustomerOrders
WHERE CustomerName LIKE N'Sa%'
ORDER BY CustomerName;
```

---

## Example 5: Search products ending with “License”

```sql
SELECT
	OrderID,
	ProductName,
	ProductCategory
FROM Training.CustomerOrders
WHERE ProductName LIKE N'%License'
ORDER BY ProductName;
```

---

## Example 6: Search emails containing customer number pattern

```sql
SELECT
	OrderID,
	CustomerName,
	CustomerEmail
FROM Training.CustomerOrders
WHERE CustomerEmail LIKE '%10@example.com'
ORDER BY CustomerEmail;
```

---

## Example 7: Search by SKU pattern

```sql
SELECT
	OrderID,
	ProductSKU,
	ProductName
FROM Training.CustomerOrders
WHERE ProductSKU LIKE 'SKU-100%'
ORDER BY ProductSKU;
```

---

# 19. Combined Production-Style Examples

These examples are closer to real business reports.

---

## Example 1: Sales dashboard by category

```sql
SELECT
	ProductCategory,
	COUNT(*) AS TotalOrders,
	SUM(Quantity) AS TotalItemsSold,
	ROUND(SUM(OrderTotal), 2) AS TotalRevenue,
	ROUND(AVG(OrderTotal), 2) AS AverageOrderValue,
	MIN(OrderTotal) AS SmallestOrder,
	MAX(OrderTotal) AS LargestOrder
FROM Training.CustomerOrders
GROUP BY ProductCategory
ORDER BY TotalRevenue DESC;
```

---

## Example 2: High-value customers

```sql
SELECT
	CustomerID,
	CustomerName,
	COUNT(*) AS TotalOrders,
	SUM(OrderTotal) AS TotalSpent,
	AVG(OrderTotal) AS AverageOrderValue
FROM Training.CustomerOrders
GROUP BY CustomerID, CustomerName
HAVING SUM(OrderTotal) > 1500
ORDER BY TotalSpent DESC;
```

---

## Example 3: Operational report for delayed deliveries

```sql
SELECT
	OrderID,
	CustomerName,
	ProductName,
	OrderStatus,
	CreatedAt,
	DeliveredAt,
	DATEDIFF(DAY, CreatedAt, DeliveredAt) AS ActualDeliveryDays,
	DeliveryDays
FROM Training.CustomerOrders
WHERE DeliveredAt IS NOT NULL
  AND DATEDIFF(DAY, CreatedAt, DeliveredAt) > 7
ORDER BY ActualDeliveryDays DESC;
```

---

## Example 4: Risk and revenue report

```sql
SELECT
	OrderStatus,
	COUNT(*) AS TotalOrders,
	SUM(OrderTotal) AS TotalRevenue,
	AVG(FraudRiskScore) AS AverageRisk,
	MAX(FraudRiskScore) AS MaximumRisk
FROM Training.CustomerOrders
GROUP BY OrderStatus
HAVING AVG(FraudRiskScore) > 3
ORDER BY AverageRisk DESC;
```

---

## Example 5: Product search and revenue report

```sql
SELECT
	ProductCategory,
	ProductName,
	COUNT(*) AS TotalOrders,
	SUM(OrderTotal) AS TotalRevenue
FROM Training.CustomerOrders
WHERE ProductName LIKE N'%SQL%'
   OR ProductDescription LIKE N'%database%'
GROUP BY ProductCategory, ProductName
ORDER BY TotalRevenue DESC;
```

---

## Example 6: Customer support report

```sql
SELECT
	CustomerSegment,
	COUNT(*) AS TotalOrders,
	COUNT(CustomerNotes) AS OrdersWithNotes,
	COUNT(SatisfactionScore) AS OrdersWithScore,
	AVG(CONVERT(DECIMAL(5,2), SatisfactionScore)) AS AverageSatisfaction
FROM Training.CustomerOrders
GROUP BY CustomerSegment
ORDER BY AverageSatisfaction DESC;
```

# 21. Workgroup Tasks

## Task 1: Filtering

Write a query that returns orders:

* from `GE`, `US`, or `DE`
* with status `Delivered` or `Shipped`
* with order total between 200 and 1000
* sorted by order total descending

Expected solution:

```sql
SELECT
	OrderID,
	CustomerName,
	CountryCode,
	OrderStatus,
	OrderTotal
FROM Training.CustomerOrders
WHERE CountryCode IN ('GE', 'US', 'DE')
  AND OrderStatus IN (N'Delivered', N'Shipped')
  AND OrderTotal BETWEEN 200 AND 1000
ORDER BY OrderTotal DESC;
```

---

## Task 2: Pattern Search

Find all orders where:

* product name contains `SQL`
* or product description contains `database`

```sql
SELECT
	OrderID,
	ProductName,
	ProductDescription,
	OrderTotal
FROM Training.CustomerOrders
WHERE ProductName LIKE N'%SQL%'
   OR ProductDescription LIKE N'%database%'
ORDER BY OrderTotal DESC;
```

---

## Task 3: NULL Handling

Find all orders:

* without a delivery date
* without a satisfaction score

```sql
SELECT
	OrderID,
	CustomerName,
	OrderStatus,
	DeliveredAt,
	SatisfactionScore
FROM Training.CustomerOrders
WHERE DeliveredAt IS NULL
  AND SatisfactionScore IS NULL
ORDER BY OrderID;
```

---

## Task 4: Aggregation

Show revenue by product category.

```sql
SELECT
	ProductCategory,
	COUNT(*) AS TotalOrders,
	SUM(OrderTotal) AS TotalRevenue,
	AVG(OrderTotal) AS AverageOrderTotal
FROM Training.CustomerOrders
GROUP BY ProductCategory
ORDER BY TotalRevenue DESC;
```

---

## Task 5: HAVING

Show only product categories where total revenue is greater than 4000.

```sql
SELECT
	ProductCategory,
	COUNT(*) AS TotalOrders,
	SUM(OrderTotal) AS TotalRevenue
FROM Training.CustomerOrders
GROUP BY ProductCategory
HAVING SUM(OrderTotal) > 4000
ORDER BY TotalRevenue DESC;
```

---

## Task 6: Date Functions

Show orders from the last 45 days.

```sql
SELECT
	OrderID,
	CustomerName,
	OrderDate,
	OrderTotal
FROM Training.CustomerOrders
WHERE OrderDate >= DATEADD(DAY, -45, CONVERT(DATE, GETDATE()))
ORDER BY OrderDate DESC;
```

---

## Task 7: String Functions

Extract the email domain from `CustomerEmail`.

```sql
SELECT
	OrderID,
	CustomerEmail,
	SUBSTRING
	(
		CustomerEmail,
		CHARINDEX('@', CustomerEmail) + 1,
		LEN(CustomerEmail)
	) AS EmailDomain
FROM Training.CustomerOrders
ORDER BY EmailDomain;
```

---

## Task 8: `ANY`

Find orders whose total is greater than at least one order from `Accessories`.

```sql
SELECT
	OrderID,
	ProductName,
	ProductCategory,
	OrderTotal
FROM Training.CustomerOrders
WHERE OrderTotal > ANY
(
	SELECT OrderTotal
	FROM Training.CustomerOrders
	WHERE ProductCategory = N'Accessories'
)
ORDER BY OrderTotal DESC;
```

---

## Task 9: `ALL`

Find orders whose total is greater than all orders from `Accessories`.

```sql
SELECT
	OrderID,
	ProductName,
	ProductCategory,
	OrderTotal
FROM Training.CustomerOrders
WHERE OrderTotal > ALL
(
	SELECT OrderTotal
	FROM Training.CustomerOrders
	WHERE ProductCategory = N'Accessories'
)
ORDER BY OrderTotal DESC;
```

---

## Task 10: Final Combined Report

Create a report by country and customer segment showing:

* number of orders
* number of unique customers
* total revenue
* average order total
* maximum order total
* only groups with more than 3 orders
* sorted by total revenue descending

```sql
SELECT
	CountryCode,
	CustomerSegment,
	COUNT(*) AS TotalOrders,
	COUNT(DISTINCT CustomerID) AS UniqueCustomers,
	SUM(OrderTotal) AS TotalRevenue,
	AVG(OrderTotal) AS AverageOrderTotal,
	MAX(OrderTotal) AS MaximumOrderTotal
FROM Training.CustomerOrders
GROUP BY CountryCode, CustomerSegment
HAVING COUNT(*) > 3
ORDER BY TotalRevenue DESC;
```

