"""
-> An exception is a runtime error which can be handled by programmer.
-> It means, if the programmer can guess an error in the program and he can do something to eliminate the harm caused by that error, then it is called an 'exception'.
-> All exceptions are represented as classes in Python.
-> The exceptions which are already available in python are called 'built-in' exceptions.
-> The base class for all built-in exceptions is 'BaseException' class.
-> Like the exceptions which are already available in python language, a programmer can also create his own exceptions called 'user-defined' exceptions.
-> When programmer wants to create his own exception class, he should derive his class from Exception class and not from 'BaseException' class.

Exception hierarchy:

                                                    BaseException
                                                        |
                                                    Exception
                                                        |
                                            StandardError       Warning
                                                |                   |
                                        ArithmeticError        DeprecationWarning
                                            +                       +
                                        AssertionError         RuntimeWarning
                                            +                       +
                                        SyntaxError            ImportWarning
                                            +
                                        TypeError
                                            +
                                        EOFError
                                            +
                                        RuntimeError
                                            +
                                        ImportError
                                            +
                                        NameError


-> Purpose of Exception handling:
            -> It makes the program robust i.e strong.
            -> A robust program doesnot terminate in the middle.
            -> When there is an error in program, it wil display an appropriate message to the user and continue execution.
            -> When the errors can be handled, they are called exceptions.
-> Steps to handle exceptions:
step1:  Programmer should observe the statements in his program where there may be a possibility of exceptions. Such statements should be written inside a 'try' block.
        try:
            statements
        Greateness of try block is that even if some exception arises inside it, program will not be terminated.
step2: Programmer should write 'except' block where he should display the exception details to the user. This helps the user to understand that there is some error in program.
        except exceptionname:
            statements
step3: Lastly, Programmer should perform clean up actions like closing the files and terminating any other processes which are running. It should write code in 'finally' block.
        finally:
            statements
"""
