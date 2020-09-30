"""
searchstrategies

Module to provide implementations of g and h for various search strategies.
In each case, the functions are class methods as we don't need an instance
of the class.  

If you are unfamiliar with Python class methods, Python uses a function
decorator (indicated by an @ to indicate that the next method is a class
method).  Example:

class SomeClass:
    @classmethod
    def foobar(cls, arg1, arg2):
        "foobar(arg1, arg2) - does ..."
        
        code... class variables are accessed as cls.var (if needed)
        return computed value

A caller would import SomeClass and then call, e.g. :  
    SomeClass.foobar("hola","amigos")

Contains g and h functions for:
BreadFirst - breadth first search
DepthFirst - depth first search
Manhattan - city block heuristic search.  To restrict the complexity of
    this, you only need handle heuristics for puzzles with a single solution
    where the blank is in the center, e.g.:
        123
        4 5
        678
    When multiple solutions are allowed, the heuristic becomes a little more
    complex as the city block distance must be estimated to each possible solution
    state. 
"""

import math

from basicsearch_lib02.tileboard import TileBoard
from explored import Explored
from basicsearch_lib02.searchrep import (Node, print_nodes, Problem)

from basicsearch_lib02.queues import PriorityQueue


class BreadthFirst:
    "BreadthFirst - breadth first search"
    @classmethod
    def g(cls, parentnode, action, childnode):
        """"g - cost from initial state to childnode
        constrained such that the last edge of the search space
        moves from parentnode to childnode via the specified action
        """
        return parentnode.depth+1

    @classmethod
    def h(cls, searchnode):
        "h - heuristic value"
        return 0

class DepthFirst:

    @classmethod
    def g(cls, parentnode, action, childnode):
        return 0

    @classmethod
    def h(cls, searchnode):
        return (searchnode.depth+1)*-1

class Manhattan:
    @classmethod
    def g(cls, parentNode, action, childNode):
        return 0

    @classmethod
    def h(cls, searchnode):
        cost = searchnode.get_h()
        return cost
# To complete:
# Write two more classes, DepthFirst and Manhattan
# that support appropriate g/h with the same signatures for the class functions

