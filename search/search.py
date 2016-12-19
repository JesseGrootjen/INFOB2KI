# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
import searchAgents


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """
    i = 0


    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def graphSearch(problem, fringe, heuristic=None):
    """
    graphSearch takes either a stack, queue or priorityqueue and the given problem to work out the graph.
    """
    visited = []												#List of visited nodes
    actionList = []                                             #List of actions

    if isinstance(fringe, util.Stack) or isinstance(fringe, util.Queue):    #If the fringe is of the type Stack or Queue
        fringe.push((problem.getStartState(), actionList))		#Push the start state on the fringe, together with the actionlist that you
                                                          		#need to get to that state.
    elif isinstance(fringe, util.PriorityQueue):                #If the fringe is of the type PriorityQueue
        fringe.push((problem.getStartState(), actionList), heuristic(problem.getStartState(), problem)) #Pushes also the start state and action list on the fringe.  But since this is
                                                                                                        #a priority queue it needs to be sorted on the costs.  This will be the costs
                                                                                                        #of the heuristic (in the ucs it is the nullHeuristic).


    while fringe:												#While there is a fringe
        node, actions = fringe.pop()							#Pops the top from a stack, first in the line from a queue and so on.

        if problem.isGoalState(node):							#Simple check if the node is the goal, then return the path excluding
                                     							#the start state
            return actions

        if node not in visited:									#If a node isn't yes visited
            visited.append(node)								#Add it to the visisted list
            
            for successor in problem.getSuccessors(node):		#Get the successors from a node
                coordinate, direction, cost = successor         #From a successor get coordinate, the direction it needs to move and
                                                                #the cost (which is 0 when using a Stack or Queue).
                if coordinate not in visited:                   #Dont add the stuff to the fringe if it is already visited
                                                                #(extra calculations)
                    newActions = actions + [direction]          #The new actions are the old ones adding the direction it is moving
                                                                #to
                    if isinstance(fringe, util.Stack) or isinstance(fringe, util.Queue):
                        fringe.push((coordinate, newActions))   #Add the coordinate and actions to the fringe
                    elif isinstance(fringe, util.PriorityQueue):
                        newCost = problem.getCostOfActions(newActions) + \
                       heuristic(coordinate, problem)           
                        #print "Heuristic: ", heuristic(coordinate, problem)
                        fringe.push((coordinate, newActions), newCost) #Add the coordinate actions and costs to the fringe

    util.raiseNotDefined()										        #Util raiseNotDefined when there is no path (asked but was
                          										        #out of scope for this exercise).
def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.
    """
    return graphSearch(problem, util.Stack())							#Return the answere from the graphSearch, given the stack and problem as
                                             							#argument
def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    return graphSearch(problem, util.Queue())                           #Return the answere from the graphSearch
def uniformCostSearch(problem):
    """
    Search the node of least total cost first.
    
    Using a priority queue in this case to get a handle on the costs. The same function can be used a the A*, though in this case a nullHeuristic needs to be used to define the costs since it is tivial. Each step costs the same.
    """
    return aStarSearch(problem)                                         #Return the answere from the
                                                                        #graphSearch
def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.
    
    Using a priority queue in this case as fringe, to be able to het a handle on the cost.
    """
    return graphSearch(problem, util.PriorityQueue(), heuristic)        #Return the answere from the graphSearch


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
