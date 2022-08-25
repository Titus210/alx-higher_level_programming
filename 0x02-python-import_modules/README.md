#               import & modules
***
##  Introduction to modules and imports

- `Modules` are `python.py` files that consist of a python code. Any Python code
can be reffered to as the module
- Modules define functions , classes and variables.
- Modules are accesed using  `import` statement i.e
```
    import math
```
- When Python imports a module called `math` for example, the interpreter will
    search for build-in module called `math`. If the build-in module is noth
    found, the interpreter willsearch for a file called `math.py` in list of
    directories that is received from the `sys.path`.
- If a build-in module is not found we can istall it using the following code
```
    pip install matplotlib
```
***
## About this project
- This project contains the following files :
1. 0-add.py :  program that imports the function def add(a, b): from the file
        add_0.py and prints the result of the addition 1 + 2 = 3
2. 1-calculation.py :  program that imports functions from the file
        calculator_1.py, does some Maths, and prints the result.
3. 2-args.py :  program that prints the number of and the list of its
         arguments.
4. 3-infinite_add.py : program that prints the result of the addition of all
        arguments
5. 4-hidden_discovery.py :  program that prints all the names defined by the
        compiled module hidden_4.pyc 
6. 5-variable_load.py :program that imports the variable a from the file
        variable_load_5.py and prints its value.
7. 100-my_calculator.py :  program that imports all functions from the file
        calculator_1.py and handles basic operations.
8. 101-easy_print.py : program that prints #pythoniscool, followed by a new
        line, in the standard output.
9.  102-magic_calculation.py :  Python function def magic_calculation(a, b)
10. 103-fast_alphabet.py : program that prints the alphabet in uppercase,
        followed by a new line.
***
### Conclusion
- Some modules are pre installed in Python Liblrary while others are installed
  using `pip`


