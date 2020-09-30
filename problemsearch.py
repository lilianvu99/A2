'''
problemsearch - Functions for seaarching.
'''
from npuzzle import NPuzzle


from basicsearch_lib02.searchrep import (Node, print_nodes, Problem)
from basicsearch_lib02.queues import PriorityQueue
from basicsearch_lib02.timer import Timer

from explored import Explored


       
def graph_search(problem, verbose=False, debug=False):
    """graph_search(problem, verbose, debug) - Given a problem representation
    (instance of basicsearch_lib02.representation.Problem or derived class),
    attempt to solve the problem.
    
    If debug is True, debugging information will be displayed.
    
    if verbose is True, the following information will be displayed:
        
        Number of moves to solution
        List of moves and resulting puzzle states
        Example:
        
            Solution in 25 moves        
            Initial state
                  0        1        2    
            0     4        8        7    
            1     5        .        2    
            2     3        6        1    
            Move 1 -  [0, -1]
                  0        1        2    
            0     4        8        7    
            1     .        5        2    
            2     3        6        1    
            Move 2 -  [1, 0]
                  0        1        2    
            0     4        8        7    
            1     3        5        2    
            2     .        6        1    
            
            ... more moves ...
            
                  0        1        2    
            0     1        3        5    
            1     4        2        .    
            2     6        7        8    
            Move 22 -  [-1, 0]
                  0        1        2    
            0     1        3        .    
            1     4        2        5    
            2     6        7        8    
            Move 23 -  [0, -1]
                  0        1        2    
            0     1        .        3    
            1     4        2        5    
            2     6        7        8    
            Move 24 -  [1, 0]
                  0        1        2    
            0     1        2        3    
            1     4        .        5    
            2     6        7        8    
        
        If no solution were found (not possible with the puzzles we
        are using), we would display:
        
            No solution found
    
    Returns a tuple (path, nodes_explored, elapsed_s) where:
    path - list of actions to solve the problem or None if no solution was found
    nodes_explored - Number of nodes explored (dequeued from frontier)
    elapsed_s is the elapsed wall clock time performing the search
    """
    node = Node(problem, problem.initial) #creating a node instance
    queue = PriorityQueue() #creating the queue
    queue.append(node) #adding the initial state to queue

    queueCheck = Explored() #explored set to check the queue
    explored = Explored() #creating empty set of explored

    nodeExplored = 0 #to keep track
    startTimer = Timer() #start the timer
    done = False

    while not done:
        node = queue.pop() #popping current state
        if not explored.exists(node.state.state_tuple()): #if the node that popped off has not been explored
            explored.add(node.state.state_tuple())
            nodeExplored += 1

        if node.state.solved():
            done = True
            elapsedTime = Timer.elapsed_s(startTimer)  # find elapsed time in seconds
            pathFinder = node.path()
            return pathFinder, nodeExplored, elapsedTime #returns a tuple of list of nodes, num of nodes explored, elapsed time
        for child in node.expand(problem): #expanding the problem to find every child node
            s = child.state
            if not explored.exists(s.state_tuple()) and not queueCheck.exists(s.state_tuple()): #if the child is not in the explored and not in the queue
                queue.append(child)
                queueCheck.add(child)
        done = len(queue) == 0 #queue is empty

    print("No Solution Found")
    return (None, 0, 0) #return None if no solution was found
