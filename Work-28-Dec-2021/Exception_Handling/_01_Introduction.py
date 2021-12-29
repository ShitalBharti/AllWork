"""
-> Errors in software are called 'bugs' and process of removing them is called 'debugging'.
-> Errors in python programs:
1. Compile-time errors:
            Syntactical errors found in the code, due to which a program fails to compile.
2. Runtime errors:
            When PVM cannot execute the byte code, it flags runtime error.
            For example, insufficient memory to store something or inability of the PVM to execute some statement come under runtime errors.
            Runtime errors are not detected by Python compiler. They are detected by PVM, only at runtime.
3. Logical errors:
            These errors depict flaws in the logic of the program.
            Logical errors are not detected by the Python compiler or PVM.
            Programmer is solely responsible for them.
-> When there is an error in a program, due to its sudden termination, following things can be suspected:
        ->  The important data in files or databases used in program may be lost.
        ->  The software may be corrupted.
        ->  Program abruptly terminates giving error message to the user making the user losing trust in the software.
"""
"""
# 1. program to understand compile-time error:
x = 1
if x==1
    print("Where is colon?")
    
''' output:
    if x==1
          ^
SyntaxError: invalid syntax
'''
"""

""""
# 2. program to understand run-time error:

def concat(a,b):
    print(a+b)

concat('Hai',25)

'''
output:
TypeError: can only concatenate str (not "int") to str
'''
"""

# 3. program to understand logical error:

def increment(sal):
    sal = sal * 15/100
    return sal

sal = increment(5000.00)
print("Incremented salary is",sal)


