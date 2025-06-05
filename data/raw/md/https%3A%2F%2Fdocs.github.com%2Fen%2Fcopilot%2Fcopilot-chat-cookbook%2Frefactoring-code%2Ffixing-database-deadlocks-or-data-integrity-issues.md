  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Copilot Chat Cookbook](https://docs.github.com/en/copilot/copilot-chat-cookbook "Copilot Chat Cookbook")/
  * [Refactoring code](https://docs.github.com/en/copilot/copilot-chat-cookbook/refactoring-code "Refactoring code")/
  * [Fix database deadlocks](https://docs.github.com/en/copilot/copilot-chat-cookbook/refactoring-code/fixing-database-deadlocks-or-data-integrity-issues "Fix database deadlocks")


# Fixing database deadlocks or data integrity issues
Copilot Chat can help you avoid code that causes slow or blocked database operations, or tables with missing or incorrect data.
## In this article
  * [Avoiding simultaneous updates on interdependent rows](https://docs.github.com/en/copilot/copilot-chat-cookbook/refactoring-code/fixing-database-deadlocks-or-data-integrity-issues#avoiding-simultaneous-updates-on-interdependent-rows)
  * [Avoiding non-index searches](https://docs.github.com/en/copilot/copilot-chat-cookbook/refactoring-code/fixing-database-deadlocks-or-data-integrity-issues#avoiding-non-index-searches)
  * [Avoiding long-running transactions](https://docs.github.com/en/copilot/copilot-chat-cookbook/refactoring-code/fixing-database-deadlocks-or-data-integrity-issues#avoiding-long-running-transactions)
  * [Avoiding data integrity issues](https://docs.github.com/en/copilot/copilot-chat-cookbook/refactoring-code/fixing-database-deadlocks-or-data-integrity-issues#avoiding-data-integrity-issues)
  * [Further reading](https://docs.github.com/en/copilot/copilot-chat-cookbook/refactoring-code/fixing-database-deadlocks-or-data-integrity-issues#further-reading)


Complex database operations–particularly those involving transactions–can lead to deadlocks or data inconsistencies that are hard to debug.
Copilot Chat can help by identifying points in a transaction where locking or deadlocks could occur, and can suggest best practices for transaction isolation or deadlock resolution, such as adjusting locking strategies or handling deadlock exceptions gracefully.
The responses shown in this article are examples. Copilot Chat responses are non-deterministic, so you may get different responses from the ones shown here.
## [Avoiding simultaneous updates on interdependent rows](https://docs.github.com/en/copilot/copilot-chat-cookbook/refactoring-code/fixing-database-deadlocks-or-data-integrity-issues#avoiding-simultaneous-updates-on-interdependent-rows)
When two or more transactions attempt to update the same rows in a database table, but in different orders, it can cause a circular wait condition.
### [Example scenario](https://docs.github.com/en/copilot/copilot-chat-cookbook/refactoring-code/fixing-database-deadlocks-or-data-integrity-issues#example-scenario)
The following SQL snippet updates one row of a table, then performs an operation that takes several seconds, then updates another row in the same table. This is problematic because the transaction locks the `id = 1` row for several seconds before the transaction completes, releasing the lock. If another transaction starts during this time that performs a similar operation, but locks the `id = 2` row first, so that it can update the row, and then attempts to lock the `id = 1` row, then both transactions will be left waiting for the other to complete, resulting in deadlock.
```
BEGIN TRANSACTION;
UPDATE my_table SET value = 'Some value' WHERE id = 301;
-- Simulate a process taking 5 seconds:
WAITFOR DELAY '00:00:05';
UPDATE my_table SET value = 'Another value' WHERE id = 127;
COMMIT TRANSACTION;

```

### [Example prompt 1](https://docs.github.com/en/copilot/copilot-chat-cookbook/refactoring-code/fixing-database-deadlocks-or-data-integrity-issues#example-prompt-1)
You can check whether there are any problems with this transaction.
In the editor, select the transaction code, then ask Copilot Chat:
`Is this transaction good?`
### [Example response 1](https://docs.github.com/en/copilot/copilot-chat-cookbook/refactoring-code/fixing-database-deadlocks-or-data-integrity-issues#example-response-1)
Copilot tells you that "the transaction in your SQL code is generally fine," but lists some things you may want to consider: lock duration, error handling, and concurrency. It mentions that "the transaction holds locks for an extended period, potentially leading to blocking or deadlocks." The response also includes revised code that adds error handling.
In this case, you decide not to add error handling. Right now you want to address the potential for deadlocks.
### [Example prompt 2](https://docs.github.com/en/copilot/copilot-chat-cookbook/refactoring-code/fixing-database-deadlocks-or-data-integrity-issues#example-prompt-2)
Enter this follow-up prompt:
`How can I rewrite this code to reduce the chance of deadlock to a minimum while not adversely affecting performance. Tell me anything else I can do to avoid a deadlock. Note: I don't want to add error handling at this time.`
### [Example response 2](https://docs.github.com/en/copilot/copilot-chat-cookbook/refactoring-code/fixing-database-deadlocks-or-data-integrity-issues#example-response-2)
Copilot gives the following advice:
>   * **Order of Access:** Ensure that all transactions access tables and rows in the same order.
>   * **Keep Transactions Short:** Minimize the time a transaction holds locks.
>   * **Use Appropriate Isolation Levels:** Use the lowest isolation level that meets your requirements.
> 

> Here is a revised version of your code:
```
BEGIN TRANSACTION;
-- Update the rows in a consistent order
UPDATE my_table SET value = 'Another value' WHERE id = 127;
UPDATE my_table SET value = 'Some value' WHERE id = 301;
-- Simulate a process taking 5 seconds:
WAITFOR DELAY '00:00:05';
COMMIT TRANSACTION;

```

## [Avoiding non-index searches](https://docs.github.com/en/copilot/copilot-chat-cookbook/refactoring-code/fixing-database-deadlocks-or-data-integrity-issues#avoiding-non-index-searches)
Searching table columns that have not been indexed will typically result in a full table scan. This can be very slow and resource-intensive, increasing the likelihood of performance bottlenecks.
### [Example scenario](https://docs.github.com/en/copilot/copilot-chat-cookbook/refactoring-code/fixing-database-deadlocks-or-data-integrity-issues#example-scenario-1)
The following SQL will result in a full table scan if `some_column` is not indexed:
```
BEGIN TRANSACTION;
SELECT * FROM my_table WHERE some_column = 'some_value';
-- More actions here, then:
COMMIT TRANSACTION;

```

### [Example prompt](https://docs.github.com/en/copilot/copilot-chat-cookbook/refactoring-code/fixing-database-deadlocks-or-data-integrity-issues#example-prompt)
Asking Copilot the following question will usually reveal the potential problem.
`How can I optimize this transaction?`
### [Example response](https://docs.github.com/en/copilot/copilot-chat-cookbook/refactoring-code/fixing-database-deadlocks-or-data-integrity-issues#example-response)
Copilot gives some advice, and mentions that the column should be indexed:
> To optimize the transaction, you should ensure that the transaction is as short as possible to reduce locking and improve performance. Here are a few tips:
>   1. **Minimize the work done in the transaction:** Only include the necessary operations within the transaction.
>   2. **Use appropriate indexes:** Ensure that the columns used in the WHERE clause are indexed.
>   3. **Avoid long-running transactions:** Keep the transaction duration short to avoid locking issues.
> 

The suggested code in the response includes the SQL command for indexing the column:
```
`CREATE INDEX idx_some_column ON my_table(some_column);`

```

## [Avoiding long-running transactions](https://docs.github.com/en/copilot/copilot-chat-cookbook/refactoring-code/fixing-database-deadlocks-or-data-integrity-issues#avoiding-long-running-transactions)
It's important to avoid long-running queries and transactions, where possible, as these can severely degrade performance and cause bottlenecks for other operations. Additionally, they can consume significant memory and log space, making your application more prone to failure in high-load environments.
### [Example scenario](https://docs.github.com/en/copilot/copilot-chat-cookbook/refactoring-code/fixing-database-deadlocks-or-data-integrity-issues#example-scenario-2)
The following SQL creates new rows in `target_table`, containing data from selected fields of rows in `source_table` where various conditions are met. If `source_table` is extremely large this may result in a long-running transaction.
```
BEGIN TRANSACTION;

INSERT INTO target_table (first_name, last_name, email, dept, role, hire_date)
SELECT first_name, last_name, email, department, job_title, start_date
FROM source_table
WHERE (department = 'Engineering' AND (salary > 95000 OR grade > 5))
  OR (department = 'Marketing' AND performance_rating = 'Excellent');

COMMIT;

```

### [Example prompt](https://docs.github.com/en/copilot/copilot-chat-cookbook/refactoring-code/fixing-database-deadlocks-or-data-integrity-issues#example-prompt-3)
You can ask Copilot whether it's possible to avoid long-running transactions.
`source_table is an extremely large table. Without altering the table, how can I ensure this SQL doesn't become a long-running query, that blocks other operations?`
### [Example response](https://docs.github.com/en/copilot/copilot-chat-cookbook/refactoring-code/fixing-database-deadlocks-or-data-integrity-issues#example-response-3)
Copilot suggests the following strategies:
  * **Batch Processing:** Process the data in smaller batches instead of a single large transaction. This can be done using a loop with a limit and offset.
  * **Indexing:** Ensure that the columns used in the `WHERE` clause (`department`, `salary`, `grade`, and `performance_rating`) are indexed to speed up the query.
  * **Locking:** Use row-level locking to avoid locking the entire table.


It supplies the following example of how you can implement batch processing. This SQL processes the data in batches of 1000 rows at a time, reducing the load on the database and preventing long-running transactions.
```
DECLARE @BatchSize INT = 1000;
DECLARE @Offset INT = 0;
DECLARE @RowCount INT;

SET @RowCount = @BatchSize;

WHILE @RowCount = @BatchSize
BEGIN
    BEGIN TRANSACTION;

    INSERT INTO target_table (first_name, last_name, email, dept, role, hire_date)
    SELECT first_name, last_name, email, department, job_title, start_date
    FROM source_table
    WHERE (department = 'Engineering' AND salary > 95000)
       OR (department = 'Engineering' AND years_of_experience > 5)
       OR (department = 'Marketing' AND performance_rating = 'Excellent');
    ORDER BY primary_key_column
    OFFSET @Offset ROWS FETCH NEXT @BatchSize ROWS ONLY;

    SET @RowCount = @@ROWCOUNT;
    SET @Offset = @Offset + @BatchSize;

    COMMIT;
END;

```

Copilot tells you to replace `primary_key_column` in the suggested code with the name of the actual primary key column of `source_table`.
## [Avoiding data integrity issues](https://docs.github.com/en/copilot/copilot-chat-cookbook/refactoring-code/fixing-database-deadlocks-or-data-integrity-issues#avoiding-data-integrity-issues)
It's important that the information in your databases remains accurate, consistent, and complete. Poorly designed queries can result in missing or incorrect data.
### [Example scenario](https://docs.github.com/en/copilot/copilot-chat-cookbook/refactoring-code/fixing-database-deadlocks-or-data-integrity-issues#example-scenario-3)
The following SQL transaction deletes an employee record and creates a deletion log. However, it's possible for the `DELETE` operation to succeed and the `INSERT` operation to fail, in which case there is no log record for the deletion.
```
BEGIN TRANSACTION;

DELETE FROM employees
WHERE employee_id = 101;

INSERT INTO deletion_log (employee_id, deletion_date, reason)
VALUES (101, GETDATE(), 'Voluntary Resignation');

COMMIT TRANSACTION;

```

### [Example prompt](https://docs.github.com/en/copilot/copilot-chat-cookbook/refactoring-code/fixing-database-deadlocks-or-data-integrity-issues#example-prompt-4)
`How can I ensure that the DELETE and INSERT operations are only performed if both succeed?`
Copilot tells you that you achieve this by using a transaction with error handling. It gives the following example using SQL Server's `TRY...CATCH` construct:
```
BEGIN TRY
    BEGIN TRANSACTION;

    DELETE FROM employees
    WHERE employee_id = 101;

    INSERT INTO deletion_log (employee_id, deletion_date, reason)
    VALUES (101, GETDATE(), 'Voluntary Resignation');

    COMMIT TRANSACTION;
END TRY
BEGIN CATCH
    ROLLBACK TRANSACTION;
    -- Handle the error, e.g., log it or re-throw
    DECLARE @ErrorMessage NVARCHAR(4000);
    DECLARE @ErrorSeverity INT;
    DECLARE @ErrorState INT;

    SELECT
        @ErrorMessage = ERROR_MESSAGE(),
        @ErrorSeverity = ERROR_SEVERITY(),
        @ErrorState = ERROR_STATE();

    RAISERROR (@ErrorMessage, @ErrorSeverity, @ErrorState);
END CATCH;

```

The suggested code ensures that if either the `DELETE` or `INSERT` operation fails, the transaction is rolled back and no changes are made to the database.
## [Further reading](https://docs.github.com/en/copilot/copilot-chat-cookbook/refactoring-code/fixing-database-deadlocks-or-data-integrity-issues#further-reading)
  * [Prompt engineering for Copilot Chat](https://docs.github.com/en/copilot/using-github-copilot/prompt-engineering-for-github-copilot)
  * [Best practices for using GitHub Copilot](https://docs.github.com/en/copilot/using-github-copilot/best-practices-for-using-github-copilot)


