'''
Created on Feb 8, 2018

@author: mroch
'''

#hash table -> state is a key -> search through dictionary
"""Implement class Explored.  
Apart from the zero argument constructor, it has two methods:  exists(state) and add(state).  
Both of these expect state tuples from a TileBoard (see TileBoard.state_tuple()) 
and will use a hash table to determine whether a state has been seen before (exists) and 
to add new states as they are removed from the frontier set (add).   """
class Explored(object):
    "Maintain an explored set.  Assumes that states are hashtable"

    def __init__(self):
        "__init__() - Create an empty explored set"
        self.thisset = set()

    def exists(self, state):
        """
        exists(state) - Has this state already been explored?
        :param state:  Hashable problem state
        :return: True if already seen, False otherwise4
        """
        existing = False
        if state in self.thisset:
            existing = True
        else:
            existing = False
        return existing

    def add(self, state):
        """
        add(state) - Add a given state to the explored set
        :param state:  A problem state that is hashable, e.g. a tuple
        :return: None
        """
        self.thisset.add(state)





