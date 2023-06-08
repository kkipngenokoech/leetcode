# Errors and Exceptions

there are at least two errors

1. syntax errors
2. exceptions

## syntax errors

this is also known as a parsing errors.

## exceptions

these are errors detected during executions.

## Handling exceptions

we do this using `try and exception`

The try statement works as follows:

1. First, the try clause (the statement(s) between the try and except keywords) is executed.
2. If no exception occurs, the except clause is skipped and execution of the try statement is finished.
3. If an exception occurs during execution of the try clause, the rest of the clause is skipped. Then, if its type matches the exception named after the except keyword, the except clause is executed, and then execution continues after the try/except block.
4. If an exception occurs which does not match the exception named in the except clause, it is passed on to outer try statements; if no handler is found, it is an unhandled exception and execution stops.

A try statement may have more than one except clause, to specify handlers for different exceptions. At most one handler will be executed.

Handlers only handle exceptions that occur in the corresponding try clause, not in other handlers of the same try statement. An except clause may name multiple exceptions as a parenthesized tuple

```python
except (RuntimeError, TypeError, NameError):
    pass
```
