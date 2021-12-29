"""
-> It is good idea to store all the error messages raised by a program into a file.
-> The file which stores the messages, especially of errors or exceptions is called as 'log' file and this technique is called 'logging'.
-> When we store the messages into a log file, we can open the file and read it or take a print out of file later.
-> This helps the programmers to understand how many errors are there, the names of those errors and where they are occurring in the program.
-> This information will enable them to pin point the errors and also rectify them easily. So, logging helps in debugging the programs.
-> Python provides a module 'logging' that is useful to create a log file that can store all error messages that may occur while executing a program.

-> Levels of Log Message:
    -> There are two built-in levels of the log message:
        Debug :     These are used to give Detailed information, typically of interest only when diagnosing problems.
        Info :      These are used to Confirm that things are working as expected
        Warning :   These are used an indication that something unexpected happened, or indicative of some problem in the near future
        Error :     This tells that due to a more serious problem, the software has not been able to perform some function
        Critical :  This tells serious error, indicating that the program itself may be unable to continue running
    -> If required, developers have the option to create more levels but these are sufficient enough to handle every possible situation.
    -> Each built-in level has been assigned its numeric value.
                Level                               Numeric Value
                CRITICAL                                50
                ERROR                                   40
                WARNING                                 30
                INFO                                    20
                DEBUG                                   10
                NOTSET                                  0
    -> Logging module is packed with several features. It has several constants, classes, and methods.
    -> The items with all caps are constant, the capitalize items are classes and the items which start with lowercase letters are methods.
    -> There are several logger objects offered by the module itself:
            -> Logger.info(msg) :           This will log a message with level INFO on this logger.
            -> Logger.warning(msg) :        This will log a message with level WARNING on this logger.
            -> Logger.error(msg) :          This will log a message with level ERROR on this logger.
            -> Logger.critical(msg) :       This will log a message with level CRITICAL on this logger.
            -> Logger.log(lvl,msg) :        This will Logs a message with integer level lvl on this logger.
            -> Logger.exception(msg) :      This will log a message with level ERROR on this logger.
            -> Logger.setLevel(lvl) :       This function sets the threshold of this logger to lvl. This means that all the messages below this level will be ignored.
            -> Logger.addFilter(filt) :     This adds a specific filter filt to the to this logger.
            -> Logger.removeFilter(filt) :  This removes a specific filter filt to the to this logger.
            -> Logger.filter(record) :      This method applies the logger’s filter to the record provided and returns
                                            True if record is to be processed. Else, it will return False.
            -> Logger.addHandler(hdlr) :    This adds a specific handler hdlr to the to this logger.
            -> Logger.removeHandler(hdlr) : This removes a specific handler hdlr to the to this logger.
            -> Logger.hasHandlers() :       This checks if the logger has any handler configured or not.
"""
import logging

# STORE messages into mylog.txt file
logging.basicConfig(filename = 'mylog.txt', level = logging.ERROR)

# these messages are stored into file
logging.error("There is an error in program")
logging.critical("There is a problem in the design")

# but these are not stored
logging.warning('The project is going slow')
logging.info('You are a junior programmer')
logging.debug("Line no. 10 contains syntax error")

# program to store the messages released by any exception into a log file
logging.basicConfig(filename = 'mylog.txt', level = logging.ERROR)
try:
    a = int(input("Enter a number1: "))
    b = int(input("Enter a number2: "))
    c = a/b
except Exception as e:
    logging.exception(e)
else:
    print("The result of division: ",c)

"""
From Google:

#Create and configure logger
logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
  
#Creating an object
logger=logging.getLogger()
  
#Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)
  
#Test messages
logger.debug("Harmless debug Message")
logger.info("Just an information")
logger.warning("Its a Warning")
logger.error("Did you try to divide by zero")
logger.critical("Internet is down")

"""