""""
*******************  Methods of Array Class ********************
a.append(x)      ->     Adds an element x at the end of existing array.
a.count(x)       ->     Returns the number of occurrences of x in array.
a.extend(x)      ->     Append x at the end of array. x can be another array or an iterable object.
a.fromfile(f,n)  ->     Reads n items (in binary format) from the file object f and appends to the end of the array a. 'f' must be file object. Raises 'EOFError'
                        if fewer than n items are read.
a.fromlist(lst)  ->     Appends item from the lst to end of array. 'lst' can be any list or iterable object.
a.fromstring(s)  ->     Append items from string s to end of array.
a.index(x)       ->     Returns the position number of the first occurrence of x in array. Raises 'ValueError' if not found.
a.insert(i,x)    ->     Inserts x in the position i in array.
a.pop(x)         ->     Removes item x from array a and returns it.
a.pop()          ->     Removes last item from array a.
a.remove(x)      ->     Removes the first occurrence of x in array a. Raises 'ValueError' if not found.
a.reverse(x)     ->     Reverses the order of elements in array a.
a.tofile(f)      ->     Writes all elements to the file f.
a.tolist()       ->     Converts the array 'a' into a list.
a.tostring()     ->     Converts the array 'a' into a string.

*******************  Variables of Array Class ********************
a.typecode       ->     Represents the type code character used to create the array a
a.itemsize       ->     Represents the size of items stored in the array (in bytes)

"""