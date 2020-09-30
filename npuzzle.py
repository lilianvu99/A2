
"""Partially completed class to represent the problem, derived from a generic Problem representation in basicsearch_lib02.searchrep.
Complete the skeleton code that is provided for you.  When you create a problem to be searched,
you should create an instance of this class which will contain an instance of TileBoard.
The parent class, Problem, accepts two keyword arguments that you will need to use (do not forget to call super):  g and h.
g is a cost function and h is a heuristic function.  See descriptions in modules searchstrategies specified below.
You can pass a function handle by using the name of the function, e.g. g=BreadthFist.g.  """

from basicsearch_lib02.tileboard import TileBoard
from basicsearch_lib02.searchrep import Problem


class NPuzzle(Problem):
    """
    NPuzzle - Problem representation for an N-tile puzzle
    Provides implementations for Problem actions specific to N tile puzzles.
    """
    def __init__(self, n, force_state=None, **kwargs):

        self.board = TileBoard(n,force_state=force_state)

        super().__init__(self.board, goals=self.board.goals, **kwargs)


        # Note on **kwargs:
        # **kwargs is Python construct that captures any remaining arguments 
        # into a dictionary.  The dictionary can be accessed like any other 
        # dictionary, e.g. kwargs[“keyname”], or passed to another function 
        # as if each entry was a keyword argument:
        #    e.g. foobar(arg1, arg2, …, argn, **kwargs).

    def actions(self, state):
        "actions(state) - find a set of actions applicable to specified state"
        return state.get_actions()
    
    def result(self, state, action):
        "result(state, action)- apply action to state and return new state"
        move = state.move(action)
        return move

    def goal_test(self, state):
        "goal_test(state) - Is state a goal?"
        return state.state_tuple() in self.goals



    
        



