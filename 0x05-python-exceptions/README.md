## Python Exceptions
***
###		Introduction
An exception in Python is an incident that happens while executing a program that causes the regular course of the program's commands to be disrupted. When a Python code comes across a condition it can't handle, it raises an exception. An object in Python that describes an error is called an exception.

Python has two options when it encounters an error:
- Handle immediately
- Stop and quit
***
####	Try and Except Statement - Catching Exceptions
The `try` and `except` are two catching expressions <br/>
The try clause contains the code that can raise an exception, while the except clause contains the code lines that handle the exception <br/>


** How to Raise an Exception**
If we wish to use raise to generate an exception when a given condition happens, we may do so as follows:
```
	num = [3, 4, 5, 7]  
	if len(num) > 3:  
	    raise Exception( f"Length of the given list must be less than or equal to 3 \
			    but is {len(num)}" ) 
```
***
### 	conclusion
-  We can throw an exception at any line of code using the raise keyword.
- The try clause's exception(s) are detected and handled using the except function.
- If no exceptions are thrown in the try code block, we can write code to be executed in the else code block.

