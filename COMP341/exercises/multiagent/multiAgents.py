# multiAgents.py
# --------------
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

# NAME: Mehmet Murat Budak
# ID: 0078940

from util import manhattanDistance
from game import Directions
import random, util

from game import Agent
from pacman import GameState

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """


    def getAction(self, gameState: GameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState: GameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newCapsules = successorGameState.getCapsules()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]



        # Idea: Penalize for ghost distance and reward for capsule distance while the timer is 0, do the reverse while the timer is not 0.

        value = 0

        # Ghosts
        # NOTE: The below logic fails when there are multiple ghosts and one of them is scared.
        ghostScore = 0
        for ghost in newGhostStates:
            ghostPos = ghost.getPosition()
            distance = manhattanDistance(newPos, ghostPos)
            if ghost.scaredTimer == 0: # Not scared, run away
                if distance < 2:
                    return float("-inf")
                else:
                    ghostScore -= 2 / distance # The higher the distance, the better
            elif ghost.scaredTimer > 0: # Scared
                if distance < 2:
                    ghostScore += 500
                else:
                    ghostScore -= distance

        # Food: Reward mildly for proximity, reward greatly for eating
        foodScore = 0
        foodList = newFood.asList()
        if foodList:
            closestFoodDistance = min(manhattanDistance(newPos, food) for food in foodList)
            foodEaten = len(currentGameState.getFood().asList()) - len(foodList)
            foodScore = -closestFoodDistance * 0.5 + foodEaten * 100
        else:
            pass

        # Capsules
        capsuleScore = 0
        capsuleList = newCapsules       
        if capsuleList:
            closestCapsuleDistance = min(manhattanDistance(newPos, capsule) for capsule in newCapsules)
        else:
            closestCapsuleDistance = 0
        capsuleConsumed = len(currentGameState.getCapsules()) - len(capsuleList)
        if capsuleConsumed:
            print("Capsule Consumed!!!")
        capsuleScore = -closestCapsuleDistance * 0.5 + capsuleConsumed * 100

        # Stop penalty
        stopPenalty = 0
        if action == Directions.STOP:
            stopPenalty = -10

        # Game Score
        gameScore = successorGameState.getScore()

        value += ghostScore + foodScore + capsuleScore + stopPenalty + gameScore
        print("Pos", newPos, "Ghost Pos", [ghost.getPosition() for ghost in newGhostStates])
        print("Ghost Score: ", ghostScore)
        # print("Food Score: ", foodScore)
        # print("Capsule Score: ", capsuleScore)
        # print("Stop Penalty: ", stopPenalty)
        # print("Game Score: ", gameScore)
        # print("Total Value: ", value)
        print("")

        return value
    


def scoreEvaluationFunction(currentGameState: GameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState: GameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"


        def minimax(agent: int, depth: int, gameState: GameState, evaluationFunction: callable):
            if gameState.isWin() or gameState.isLose() or depth == 0: # Base Case
                return evaluationFunction(gameState)
            
            if agent == 0:  # Pacman's turn, Maximizer
                return max(minimax(1, depth, gameState.generateSuccessor(agent, action), evaluationFunction)
                        for action in gameState.getLegalActions(agent))
            
            else:  # Ghosts' turn, Minimizer
                nextAgent = agent + 1  # Next agent
                if nextAgent == gameState.getNumAgents():
                    nextAgent = 0  # Cycle back to Pacman
                    depth -= 1  # Decrement depth every full cycle
                return min(minimax(nextAgent, depth, gameState.generateSuccessor(agent, action), evaluationFunction)
                        for action in gameState.getLegalActions(agent))
                
        # Initiate the minimax search
        actions = gameState.getLegalActions(0)  # Pacman's legal actions
        scores = [minimax(1, self.depth, gameState.generateSuccessor(0, action), self.evaluationFunction) for action in actions]
        bestScore = max(scores)
        bestIndices = [index for index, score in enumerate(scores) if score == bestScore]
        chosenIndex = bestIndices[0]  # Pick randomly among the best

        return actions[chosenIndex]


class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState: GameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        # def maxValue(state: GameState, depth: int, alpha: float, beta: float): # Pacman
        #     value = float("-inf")
        #     if state.isWin() or state.isLose() or depth == 0:
        #         return self.evaluationFunction(state)
        #     for action in state.getLegalActions(0):
        #         value = max(value, minValue(state.generateSuccessor(0, action), depth, alpha, beta))
        #         if value > beta:
        #             return value
        #         alpha = max(alpha, value)
        #     return value
        # def minValue(state: GameState, depth: int, alpha: float, beta: float): # All ghosts
        #     # I suppose it isn't really possible to use alpha-beta pruning among ghosts becase all of them are minimizer nodes.
        #     # So the only pruning will be done at pacman's level. I think.
        #     value = float("+inf")
        #     if state.isWin() or state.isLose() or depth == 0:
        #         return self.evaluationFunction(state)
        #     nextAgent = 1
        #     if nextAgent == state.getNumAgents(): # Cycle back to Pacman
        #         nextAgent = 0
        #         depth -= 1
        #     for action in state.getLegalActions(nextAgent):
        #         if nextAgent == state.getNumAgents() - 1:
        #             value = min(value, maxValue(state.generateSuccessor(nextAgent, action), depth, alpha, beta))
        #         else:
        #             value = min(value, minValue(state.generateSuccessor(nextAgent, action), depth, alpha, beta))
        #         if value < alpha:
        #             return value
        #         beta = min(beta, value)
        #     return value
        
    
        # def minimax(agent: int, depth: int, gameState: GameState, alpha: float, beta: float):
        #     if gameState.isWin() or gameState.isLose() or depth == 0: # Base Case
        #         return self.evaluationFunction(gameState)
            
        #     if agent == 0:  # Pacman, Maximizer
        #         v = float("-inf")
        #         nextAgent = agent + 1
        #         for action in gameState.getLegalActions(agent):
        #             state = gameState.generateSuccessor(agent, action)
        #             v = max(v, minimax(nextAgent, depth, state, alpha, beta))
        #             alpha = max(alpha, v)
        #             if beta <= alpha:  # Prune if v is greater than or equal to beta
        #                 return v
        #         return v

        #     else:  # All Ghosts, Minimizers
        #         v = float("+inf")
        #         nextAgent = agent + 1  # Next agent
        #         if nextAgent == gameState.getNumAgents():
        #             nextAgent = 0  # Cycle back to Pacman
        #             depth -= 1  # Decrement depth every full cycle

        #         for action in gameState.getLegalActions(agent):
        #             state = gameState.generateSuccessor(agent, action)
        #             v = min(v, minimax(nextAgent, depth, state, alpha, beta))
        #             beta = min(beta, v)
        #             if beta <= alpha:  # Prune if v is less than or equal to alpha
        #                 return v
        #         return v
                
        # # Initiate the minimax search
        # actions = gameState.getLegalActions(0)  # Pacman's legal actions
        # scores = [minimax(1, self.depth, gameState.generateSuccessor(0, action), float("-inf"), float("+inf")) for action in actions]
        # bestScore = max(scores)
        # bestIndices = [index for index, score in enumerate(scores) if score == bestScore]
        # chosenIndex = bestIndices[0]  # Pick randomly among the best

        # return actions[chosenIndex]

        def minimax(gameState: GameState, agent: int, depth: int, alpha: float, beta: float):
            # print("Call: ", callNum, "Agent: ", agent, "Depth: ", depth, "Alpha: ", alpha, "Beta: ", beta)
            if depth == 0 or gameState.isLose() or gameState.isWin():
                return [self.evaluationFunction(gameState), ""]
            
            agentCount = gameState.getNumAgents()
            nextAgent = (agent + 1)%agentCount
            
            if agent == 0:
                maxEval = float("-inf")
                bestAction = ""
                for action in gameState.getLegalActions(0):
                    state = gameState.generateSuccessor(0, action)
                    value = minimax(state, nextAgent, depth, alpha, beta)[0]
                    
                    if value >= maxEval:
                        maxEval = value
                        bestAction = action
                    alpha = max(alpha, value)
                    if beta < alpha:
                        break
                return [maxEval, bestAction]

            
            else:
                if nextAgent == 0: # Decrement before pacmans move
                    depth -= 1

                minEval = float("+inf")
                for action in gameState.getLegalActions(agent):
                    state = gameState.generateSuccessor(agent, action)
                    value = minimax(state, nextAgent, depth, alpha, beta)[0]
                    minEval = min(minEval, value)
                    beta = min(beta, value)
                    if beta < alpha:
                        break
                return [minEval, ""]
        
        # Initiate the minimax search        
        return minimax(gameState, 0, self.depth, float("-inf"), float("+inf"))[1]


class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState: GameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"
        def minimax(gameState: GameState, agent: int, depth: int):
            # print("Call: ", callNum, "Agent: ", agent, "Depth: ", depth)
            if depth == 0 or gameState.isLose() or gameState.isWin():
                return [self.evaluationFunction(gameState), ""]
            
            agentCount = gameState.getNumAgents()
            nextAgent = (agent + 1)%agentCount
            
            if agent == 0:
                maxEval = float("-inf")
                bestAction = ""
                for action in gameState.getLegalActions(0):
                    state = gameState.generateSuccessor(0, action)
                    value = minimax(state, nextAgent, depth)[0]
                    
                    if value >= maxEval:
                        maxEval = value
                        bestAction = action

                return [maxEval, bestAction]

            
            else:
                if nextAgent == 0: # Decrement before pacman's move
                    depth -= 1

                avgEval = 0
                actions = gameState.getLegalActions(agent)
                for action in actions:
                    state = gameState.generateSuccessor(agent, action)
                    avgEval += minimax(state, nextAgent, depth)[0]
                    
                avgEval /= len(actions)
                return [avgEval, ""]
        
        # Initiate the minimax search        
        return minimax(gameState, 0, self.depth)[1]

def betterEvaluationFunction(currentGameState: GameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: score + closest food distance + food pellet count + closest capsule distance + capsule count + closest ghost penalty + active ghost count + stuck penalty + random
    """
    "*** YOUR CODE HERE ***"

    def manhattanDistance(pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    pos = currentGameState.getPacmanPosition()
    food = currentGameState.getFood()
    capsules = currentGameState.getCapsules()
    ghostStates = currentGameState.getGhostStates()

    score = currentGameState.getScore()

    # Food related
    foodCount = len(food.asList())
    score -= foodCount * 3
    try:
        closestFoodDistance = min([manhattanDistance(pos, food) for food in food.asList()])
        score += 1 / closestFoodDistance  # Reward for closer food
    except ValueError:
        pass

    # Capsule related
    capsuleCount = len(capsules)
    score -= capsuleCount * 5
    try:
        closestCapsuleDistance = min([manhattanDistance(pos, capsule) for capsule in capsules])
        score += 2 / closestCapsuleDistance  # Reward for closer capsule
    except ValueError:
        pass

    # Ghost related
    try:
        closestGhostDistance = min([manhattanDistance(pos, ghost.getPosition()) for ghost in ghostStates if ghost.scaredTimer == 0])  # Distance to closest active ghost
        score -= 1 / closestGhostDistance # Penalize closer ghosts 
    except ValueError:
        pass # No active ghosts
    except ZeroDivisionError:
        return float("-inf")
    
      
    activeGhostCount = len([ghost for ghost in ghostStates if ghost.scaredTimer == 0])  # Number of active ghosts
    score -= activeGhostCount * 2  # Penalize for each active ghost (adjust weight)


    # If there are 3 adjacent walls, pacman is stuck
    stuck = 0
    if currentGameState.hasWall(pos[0] + 1, pos[1]):
        stuck += 1
    if currentGameState.hasWall(pos[0] - 1, pos[1]):
        stuck += 1
    if currentGameState.hasWall(pos[0], pos[1] + 1):
        stuck += 1
    if currentGameState.hasWall(pos[0], pos[1] - 1):
        stuck += 1

    if stuck >= 3:
        #print("STUCK")
        return float("-inf")
    
    score += random.random() * 0.1  # Randomness to break ties

    return score

# Abbreviation
better = betterEvaluationFunction
