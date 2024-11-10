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
from game import Directions
from typing import List

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

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




def tinyMazeSearch(problem: SearchProblem) -> List[Directions]:
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    startState = problem.getStartState()
    
    from util import Stack  
    openSet = Stack()
    closedSet = []

    # Node format: (state, action, cost)

    openSet.push((startState, [], 0))

    while (not openSet.isEmpty()):
        curr_node = openSet.pop()

        if curr_node[0] not in closedSet:
            closedSet.append(curr_node[0])
            if problem.isGoalState(curr_node[0]):
                return curr_node[1] # return the actions
            for child in problem.getSuccessors(curr_node[0]):
                #print(child)
                if child[0] not in closedSet:
                    new_actions = curr_node[1].copy()
                    new_actions.append(child[1])
                    openSet.push((child[0], new_actions, child[2]))

    print("WARNING: Couldn't find a path")
    return []

def breadthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    startState = problem.getStartState()
    
    #Initializing the fringe and closed set
    from util import Queue  
    openSet = Queue()
    closedSet = []

    # Node format: (state, action, cost)

    openSet.push((startState, [], 0))

    while (not openSet.isEmpty()):
        curr_node = openSet.pop()

        if curr_node[0] not in closedSet:
            closedSet.append(curr_node[0])
            if problem.isGoalState(curr_node[0]):
                #print("Goal found")
                return curr_node[1] # return the actions
            for child in problem.getSuccessors(curr_node[0]):
                #print(child)
                if child[0] not in closedSet:
                    new_actions = curr_node[1].copy()
                    new_actions.append(child[1])
                    openSet.push((child[0], new_actions, child[2]))
    print("WARNING: Couldn't find a path")
    return []

def uniformCostSearch(problem: SearchProblem) -> List[Directions]:
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    startState = problem.getStartState()
    
    #Initializing the fringe and closed set
    from util import PriorityQueue
    openSet = PriorityQueue()
    closedSet = []

    # Node format: (state, action, cost)

    openSet.push((startState, [], 0), 0)

    while (not openSet.isEmpty()):
        
        curr_node = openSet.pop()

        if curr_node[0] not in closedSet:
            closedSet.append(curr_node[0])
            if problem.isGoalState(curr_node[0]):
                #print("Goal found")
                return curr_node[1] # return the actions
            for child in problem.getSuccessors(curr_node[0]):
                if child[0] not in closedSet:
                    actions = curr_node[1].copy()
                    actions.append(child[1])
                    item = (child[0],actions, child[2])
                    priority = problem.getCostOfActions(actions)
                    openSet.push(item, priority)
    print("WARNING: Couldn't find a path")
    return []

def nullHeuristic(state, problem=None) -> float:
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic) -> List[Directions]:
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    from util import PriorityQueue
    startState = problem.getStartState()

    # Ensure startState is hashable (convert to tuple if needed)
    startState = tuple(startState) if isinstance(startState, dict) else startState

    openSet = PriorityQueue()
    closedSet = {}

    # Node format: (state, actions, cumulative cost)
    openSet.push((startState, [], 0), 0)

    while not openSet.isEmpty():
        current_node = openSet.pop()
        current_state, actions, current_cost = current_node

        # Ensure current_state is hashable
        current_state = tuple(current_state) if isinstance(current_state, dict) else current_state

        if current_state in closedSet and closedSet[current_state] <= current_cost:
            continue

        # Track the lowest cost for reaching this state
        closedSet[current_state] = current_cost

        if problem.isGoalState(current_state):
            return actions

        for successor, action, step_cost in problem.getSuccessors(current_state):
            # Ensure successor is hashable
            successor = tuple(successor) if isinstance(successor, dict) else successor

            new_actions = actions + [action]
            new_cost = current_cost + step_cost
            priority = new_cost + heuristic(successor, problem)

            # Only push if this path to successor is cheaper
            if successor not in closedSet or closedSet[successor] > new_cost:
                openSet.push((successor, new_actions, new_cost), priority)

    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
