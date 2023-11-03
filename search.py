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


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    initialNode = problem.getStartState() # get the starting position of the player
    # if that is the goal state desired then we dont need to perform any action
    if problem.isGoalState(initialNode): return []

    # initialy stack and visited array is empty
    st = util.Stack()
    visitedList = []

    # we push the initial node first along with empty action array
    st.push((initialNode, []))

    # while the stack does not get empty, we visit each node and add its adjacent nodes which are not
    # yet visited into the stack
    while not st.isEmpty():
        currNode, actions = st.pop()
        if currNode not in visitedList:
            visitedList.append(currNode) # mark current node as visited
            if problem.isGoalState(currNode):
                return actions
            # loop through all the successors of the current node and add them to the stack by including eac action
            for nextNode, action, cost in problem.getSuccessors(currNode):
                nextAction = actions + [action]
                st.push((nextNode, nextAction))

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    q = util.Queue() # using a FIFO queue
    initialNode = problem.getStartState()
    visitedList = []
    q.push((initialNode, []))
    if problem.isGoalState(initialNode):
        return []
    
    
    while not q.isEmpty():
        initialNode, actions = q.pop() # choosing the shallowest node each time
        if initialNode not in visitedList:
            visitedList.append(initialNode)
            if problem.isGoalState(initialNode):
                return actions
            for nextNode, action, cost in problem.getSuccessors(initialNode):
                nextAction = actions + [action]
                q.push((nextNode, nextAction))


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    startingNode = problem.getStartState()
    if problem.isGoalState(startingNode):
        return []
    visitedList = []
    pq = util.PriorityQueue() # using a priority queue to get us least costly next state from all adjacent states
    pq.push((startingNode, [], 0), 0)
    
    while not pq.isEmpty():
        curr, actions, prevCost = pq.pop()
        if curr not in visitedList:
            visitedList.append(curr)
            if problem.isGoalState(curr):
                return actions
            for nextNode, action, cost in problem.getSuccessors(curr):
                nextDirection = actions + [action]
                priority = prevCost + cost
                pq.push((nextNode, nextDirection, priority), priority)


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    initialNode = problem.getStartState()
    if problem.isGoalState(initialNode): return []
    # main logic idea: a* score = cost of path + heuristic
    # heuristic consists of two things g and h where g tells you the cost from startnode to currnode
    # while h tells you the cost of currnode to goalnode
    visitedList = []
    pq = util.PriorityQueue()
    pq.push((initialNode, [], 0), 0)

    while not pq.isEmpty():
        curr, actions, prevCost = pq.pop()
        if curr not in visitedList:
            visitedList.append(curr)
            if problem.isGoalState(curr):
                return actions
            for nextNode, action, cost in problem.getSuccessors(curr):
                nextDirection = actions + [action]
                newCost = prevCost + cost
                heurCost = newCost + heuristic(nextNode, problem)
                pq.push((nextNode, nextDirection, newCost), heurCost)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
