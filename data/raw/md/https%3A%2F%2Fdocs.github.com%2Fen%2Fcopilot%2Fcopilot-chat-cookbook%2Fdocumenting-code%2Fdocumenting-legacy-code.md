  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Copilot Chat Cookbook](https://docs.github.com/en/copilot/copilot-chat-cookbook "Copilot Chat Cookbook")/
  * [Documenting code](https://docs.github.com/en/copilot/copilot-chat-cookbook/documenting-code "Documenting code")/
  * [Document legacy code](https://docs.github.com/en/copilot/copilot-chat-cookbook/documenting-code/documenting-legacy-code "Document legacy code")


# Documenting legacy code
Copilot Chat can help with documenting legacy code.
## In this article
  * [Example scenario](https://docs.github.com/en/copilot/copilot-chat-cookbook/documenting-code/documenting-legacy-code#example-scenario)
  * [Example prompt](https://docs.github.com/en/copilot/copilot-chat-cookbook/documenting-code/documenting-legacy-code#example-prompt)
  * [Example response](https://docs.github.com/en/copilot/copilot-chat-cookbook/documenting-code/documenting-legacy-code#example-response)
  * [Further reading](https://docs.github.com/en/copilot/copilot-chat-cookbook/documenting-code/documenting-legacy-code#further-reading)


Working with legacy code can be challenging for developers, especially when the code is complex or not well-documented. In such cases, it can be helpful to use Copilot Chat to explain unclear or complex code to other developers or to document it for future reference.
## [Example scenario](https://docs.github.com/en/copilot/copilot-chat-cookbook/documenting-code/documenting-legacy-code#example-scenario)
The block of COBOL below connects to a database and inserts a record. The code lacks documentation, which makes it difficult to understand what it does and how it works.
```
IDENTIFICATION DIVISION.
PROGRAM-ID. INSERT-RECORD.

ENVIRONMENT DIVISION.

DATA DIVISION.
WORKING-STORAGE SECTION.
01  WS-STATUS-FLAGS.
    05 WS-DB-STATUS     PIC X(2).
       88 WS-SUCCESS    VALUE "00".
    05 WS-SQLCODE       PIC S9(9) COMP.
    05 WS-ERROR-MSG     PIC X(50).

LINKAGE SECTION.
01  LS-PARAMETERS.
    05 LS-PERSON-RECORD.
       10 PERSON-ID     PIC 9(6).
       10 PERSON-NAME   PIC X(50).
       10 PERSON-AGE    PIC 9(3).
    05 LS-RESULT        PIC X.
       88 SUCCESS       VALUE 'T'.
       88 FAILED        VALUE 'F'.

PROCEDURE DIVISION USING LS-PARAMETERS.
    PERFORM INSERT-AND-VALIDATE
    GOBACK
    .

INSERT-AND-VALIDATE.
    EXEC SQL
        INSERT INTO persons (id, name, age)
        VALUES (:PERSON-ID, :PERSON-NAME, :PERSON-AGE)
    END-EXEC

    IF SQLCODE = 0
        EXEC SQL COMMIT END-EXEC
        SET SUCCESS TO TRUE
    ELSE
        EXEC SQL ROLLBACK END-EXEC
        SET FAILED TO TRUE
        STRING "DB Error: " SQLCODE
            DELIMITED BY SIZE
            INTO WS-ERROR-MSG
        DISPLAY WS-ERROR-MSG
    END-IF
    .

```

## [Example prompt](https://docs.github.com/en/copilot/copilot-chat-cookbook/documenting-code/documenting-legacy-code#example-prompt)
We can use a simple prompt to ask Copilot Chat to document the code.
`Document this code`
If you want the documentation generated in another format like Markdown, you can specify the desired output format in the prompt. For example: `Document this code in Markdown`.
## [Example response](https://docs.github.com/en/copilot/copilot-chat-cookbook/documenting-code/documenting-legacy-code#example-response)
The following response is an example. Copilot Chat responses are non-deterministic, so you may get a different response from the one shown here.
Copilot will provide a text overview of the code block, and an updated version with comments explaining the logic and purpose of each section.
For example:
```
*****************************************************************
* Program: INSERT-RECORD
* Purpose: Inserts a person record into the database with
*          transaction management and error handling
*****************************************************************
 IDENTIFICATION DIVISION.
 PROGRAM-ID. INSERT-RECORD.

 ENVIRONMENT DIVISION.

 DATA DIVISION.
 WORKING-STORAGE SECTION.
* Status flags and error handling variables
 01  WS-STATUS-FLAGS.
     05 WS-DB-STATUS     PIC X(2).              *> Database status
        88 WS-SUCCESS    VALUE "00".            *> Success flag
     05 WS-SQLCODE       PIC S9(9) COMP.        *> SQL return code
     05 WS-ERROR-MSG     PIC X(50).             *> Error message

 LINKAGE SECTION.
* Input/Output parameters
 01  LS-PARAMETERS.
     05 LS-PERSON-RECORD.
        10 PERSON-ID     PIC 9(6).              *> Person ID
        10 PERSON-NAME   PIC X(50).             *> Person name
        10 PERSON-AGE    PIC 9(3).              *> Person age
     05 LS-RESULT        PIC X.                 *> Operation result
        88 SUCCESS       VALUE 'T'.             *> Success flag
        88 FAILED        VALUE 'F'.             *> Failure flag

 PROCEDURE DIVISION USING LS-PARAMETERS.
     PERFORM INSERT-AND-VALIDATE
     GOBACK
     .

*****************************************************************
* Handles database insertion with transaction management
*****************************************************************
 INSERT-AND-VALIDATE.
     EXEC SQL
         INSERT INTO persons (id, name, age)
         VALUES (:PERSON-ID, :PERSON-NAME, :PERSON-AGE)
     END-EXEC

     IF SQLCODE = 0
         EXEC SQL COMMIT END-EXEC                *> Commit if successful
         SET SUCCESS TO TRUE
     ELSE
         EXEC SQL ROLLBACK END-EXEC              *> Rollback if failed
         SET FAILED TO TRUE
         STRING "DB Error: " SQLCODE
             DELIMITED BY SIZE
             INTO WS-ERROR-MSG
         DISPLAY WS-ERROR-MSG
     END-IF
     .

```

## [Further reading](https://docs.github.com/en/copilot/copilot-chat-cookbook/documenting-code/documenting-legacy-code#further-reading)
  * [Prompt engineering for Copilot Chat](https://docs.github.com/en/copilot/using-github-copilot/prompt-engineering-for-github-copilot)
  * [Best practices for using GitHub Copilot](https://docs.github.com/en/copilot/using-github-copilot/best-practices-for-using-github-copilot)


