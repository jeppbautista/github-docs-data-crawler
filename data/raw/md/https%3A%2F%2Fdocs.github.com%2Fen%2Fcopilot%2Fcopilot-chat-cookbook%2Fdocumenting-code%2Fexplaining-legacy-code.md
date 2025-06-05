  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Copilot Chat Cookbook](https://docs.github.com/en/copilot/copilot-chat-cookbook "Copilot Chat Cookbook")/
  * [Documenting code](https://docs.github.com/en/copilot/copilot-chat-cookbook/documenting-code "Documenting code")/
  * [Explain legacy code](https://docs.github.com/en/copilot/copilot-chat-cookbook/documenting-code/explaining-legacy-code "Explain legacy code")


# Explaining legacy code
Copilot Chat can help with explaining unfamiliar code.
## In this article
  * [Example scenario](https://docs.github.com/en/copilot/copilot-chat-cookbook/documenting-code/explaining-legacy-code#example-scenario)
  * [Example prompt](https://docs.github.com/en/copilot/copilot-chat-cookbook/documenting-code/explaining-legacy-code#example-prompt)
  * [Example response](https://docs.github.com/en/copilot/copilot-chat-cookbook/documenting-code/explaining-legacy-code#example-response)
  * [Further reading](https://docs.github.com/en/copilot/copilot-chat-cookbook/documenting-code/explaining-legacy-code#further-reading)


One of the biggest challenges with legacy code is helping developers understand it who aren't familiar with the languages or frameworks. With Copilot Chat, you can explain the background you have and ask for an explanation.
## [Example scenario](https://docs.github.com/en/copilot/copilot-chat-cookbook/documenting-code/explaining-legacy-code#example-scenario)
Consider the following COBOL code. If you're a Python developer (as an example), you might not be familiar with COBOL, so you could ask Copilot Chat to explain the code to you.
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

## [Example prompt](https://docs.github.com/en/copilot/copilot-chat-cookbook/documenting-code/explaining-legacy-code#example-prompt)
You can ask for an explanation of the COBOL code from the point of view of a Python developer.
`I'm a Python developer. Help me better understand this code. Please provide analogies.`
## [Example response](https://docs.github.com/en/copilot/copilot-chat-cookbook/documenting-code/explaining-legacy-code#example-response)
The following response is an example. Copilot Chat responses are non-deterministic, so you may get a different response from the one shown here.
Copilot provides a high-level overview of the code, before walking through the various operations and explaining them in a way that Python developers can understand. It uses analogies to make the explanation more accessible. The response might start with the following:
```
Let me explain this COBOL code using Python analogies:

High-Level Overview
This is similar to a Python function that inserts a person's record into a database with error handling.

```
```
# In Python, the COBOL divisions would be like:

# IDENTIFICATION DIVISION = module/file name
# PROGRAM-ID = function name
def insert_record():
    pass

# DATA DIVISION would be like declaring these variables:
class WorkingStorage:
    db_status = ""  # WS-DB-STATUS
    sqlcode = 0     # WS-SQLCODE
    error_msg = ""  # WS-ERROR-MSG

# LINKAGE SECTION is like function parameters
class PersonRecord:
    def __init__(self, person_id: int, person_name: str, person_age: int):
        self.person_id = person_id    # PERSON-ID
        self.person_name = person_name # PERSON-NAME
        self.person_age = person_age   # PERSON-AGE
        self.success = False          # LS-RESULT

```

## [Further reading](https://docs.github.com/en/copilot/copilot-chat-cookbook/documenting-code/explaining-legacy-code#further-reading)
  * [Prompt engineering for Copilot Chat](https://docs.github.com/en/copilot/using-github-copilot/prompt-engineering-for-github-copilot)
  * [Best practices for using GitHub Copilot](https://docs.github.com/en/copilot/using-github-copilot/best-practices-for-using-github-copilot)


