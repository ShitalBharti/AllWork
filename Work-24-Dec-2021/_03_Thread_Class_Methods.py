"""
t.start()           -> Starts the Thread. It must be called at most once per thread object. It arranges for the object's run() method to be invoked in a separate thread of control.
t.join()            -> waits until the thread terminates.
t.join(timeout)     -> waits until the thread terminates or a timeout occurs.
t.is_alive()        -> Returns True if the thread is alive in memory and False otherwise.
                        Thread is alive from the moment of start() method returns until its run() method terminates.
t.setName(name)     -> Gives a name to the Thread.
t.getName()         -> Returns the name of the Thread.
t.name              -> This is a property that represents the thread's name.
t.setDaemon(flag)   -> Makes a thread a daemon thread if the flag is True.
t.isDaemon()        -> Returns True if the thread is a daemon thread, otherwise False.
t.daemon            -> This takes either True or False to set the thread as daemon or not.
"""