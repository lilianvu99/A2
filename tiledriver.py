'''
driver for graph search problem

'''
from explored import Explored
"""
Single Programmer Affidavit
I the undersigned promise that the attached assignment is my own work. While I was free to discuss ideas with others, the work contained is my own. I recognize that should this not be the case, I will be subject to penalties as outlined in the course syllabus.


Lilian Vu 821477716 9/29/2020
________________________________________
Programmer (print & sign your name, then date it)
"""
from statistics import (mean, stdev)  # Only available in Python 3.4 and newer

from npuzzle import NPuzzle
from basicsearch_lib02.tileboard import TileBoard
from basicsearch_lib02.timer import Timer
from searchstrategies import (BreadthFirst, DepthFirst, Manhattan)
from problemsearch import graph_search
import collections
from basicsearch_lib02.searchrep import Node, Problem


def driver() :
    iterations = 31
    numTiles = 8
    outputNode = []
    outputLength = []
    outputElap = []
    nodeDefault = 0

    #iterate 31 times
    for index in range(1, iterations+1):
        print(index)
        nPuzzle = NPuzzle(numTiles, None, g=BreadthFirst.g, h=BreadthFirst.h) #creating an instance of the NPuzzle
        tileBoard = nPuzzle.board #creating instance of TileBoard
        problem = Problem(tileBoard, goals=(1, 2, 3, 4, 5, 7, 8, None)) #creating instance of Problem
        print(tileBoard)

        root = Node(problem, tileBoard) #creating parent node
        queue = []
        queue.append(root)
        childNode = root.child_node([0, 0])

        explored = Explored()
        node = queue.pop(0)

    #BFS
        print("Bread First Search")
        if (problem.goal_test(tileBoard.state_tuple())): #if initial state is already the goal state
            nodeDefault = len(node.path())

        problem.f = BreadthFirst.h(childNode) + BreadthFirst.g(root, [1, 0], childNode) #updating problem with BFS h and g
        outputBF = graph_search(problem) #put updated problem to actually search

    #split the tuple output into appropriate variables
        lengthBF = len(outputBF[0])
        nodeBF = outputBF[1]
        elapBF = outputBF[2]

        print("--------------------------------------------------------------------------------------")
    #DFS
        print("Death First Search")
        problem.f = DepthFirst.h(childNode) + DepthFirst.g(root, [1, 0], childNode)
        outputDF = graph_search(problem)

    #split the tuple output into appropriate variables
        lengthDF = len(outputDF[0])
        nodeDF = outputDF[1]
        elapDF = outputDF[2]
        print("--------------------------------------------------------------------------------------")

    #Manhattan
        print("Manhattan")
        problem.f = DepthFirst.h(childNode) + DepthFirst.g(root, [1, 0], childNode)
        outputMan = graph_search(problem)
    #split the tuple output into appropriate variables
        lengthMan = len(outputMan[0])
        nodeMan = outputMan[1]
        elapMan = outputMan[2]
        print("--------------------------------------------------------------------------------------")

    #appends the sum of the node, path, and elapse time for every iteration into a List
        sumNode = nodeDefault + nodeDF + nodeBF + nodeMan
        outputNode.append(sumNode)
        sumLength = lengthBF + lengthMan + lengthDF
        outputLength.append(sumLength)
        sumElap = elapBF + elapDF + elapMan
        outputElap.append(sumElap)

    #calculate mean and standard deviation of output
    meanLength = mean(outputLength)
    sdLength = stdev(outputLength)
    meanNode = mean(outputNode)
    sdNode = stdev(outputNode)
    meanTime = mean(outputElap)
    sdTime = stdev(outputElap)

    #print table
    print("\t\t\t Length of Plan \t Number of Nodes \t Elapsed Time(s)")
    print("----------------------------------------------------------------------")
    print("Mean: " + "\t\t\t" + str(meanLength) + "\t\t\t\t\t" + str(meanNode) +"\t\t\t\t\t" + str(meanTime))
    print("STD: " + "\t\t" + str(sdLength) + "\t\t\t\t\t" + str(sdNode) + "\t\t\t\t\t" + str(sdTime))

driver()
# To do:  Run driver() if this is the entry module
