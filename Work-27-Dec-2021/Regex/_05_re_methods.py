"""
Mainly regular expressions are used to perform following important operations:

-> Matching Strings
-> Searching for Strings
-> Finding all Strings
-> Splitting a string into pieces Strings
-> Replacing Strings

re module methods:

match() ->       Searches in the beginning of string and if matching string is found it returns an object that contains the resultant string, otherwise it returns None.
                 We can access string from the returned object using group() method.

search() ->      Searches the string from beginning till the end and returns the first occurrence of matching string, otherwise it returns None.
                 We can access string from the returned object using group() method.

findall() ->     Searches string from beginning till the end and returns all occurrences of matching string in the form of a list object.
                 If the matching strings are not found, it returns an empty list.
                 We can retrieve resultant strings from the list using a for loop.

split() ->       It splits string according to regular expressions and the resultant pieces are returned as a list. If there are no string pieces, then it returns an empty list.
                 We can retrieve resultant string pieces from list using a for loop.

sub() ->         It substitutes new strings in the place of existing strings. After substitution, main string is returned by this method.

"""