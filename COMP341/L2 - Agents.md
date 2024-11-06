We want to make **rational** agents, which acts to maximize its utility.
**Agent:** An autonomous entity that exists in some kind of *environment* and that *perceives* and *acts*.
## How do we formulate an AI problem?
- Performance/Utility
- Environment
- Actions
- Sensors

### Search Problem
• A **state space** - The set of all possible states that are possible in your given world
• A s**et of actions** available in each state
• A **transition model** - Outputs the next state when a specific action is taken at current state
• An **action cost** - Incurred when moving from one state to another after applying an action
• A **start state** - The state in which an agent exists initially
• A **goal test** - A function that takes a state as input, and determines whether it is a goal state

- **Simple Reflex Agents:** React to the current percept with a direct action, without considering the future.
- **Model-Based Reflex Agents:** Consider the current state and the internal model of the world to choose an action, allowing for a more informed decision than simple reflex agents.
- **Goal-Based Agents:** Make decisions based on the likelihood of actions bringing them closer to achieving predefined goals, considering future outcomes.
- **Utility-Based Agents:** Optimize their actions to maximize a utility function, evaluating the desirability of different states or outcomes for more nuanced decision-making.

## Simple Reflex
![[Pasted image 20240315205042.png]]
```python
if dirty:
	suck()
else:
	move()
```

They do not consider the aftermath of their actions, they just reflex.

## Model Based Reflex Agent
Model-Based Reflex Agents improve upon simple reflex agents by maintaining some form of internal state that depends on the percept history, allowing them to make better-informed decisions. This internal state is a model of the world, which, combined with the current percept, can help the agent determine the impact of its actions. This model includes knowledge about how the world works (the "laws" of the environment) and the current state of the world.

The structure of a Model-Based Reflex Agent can be described as follows:

1. **Update State:** Based on the current state, action taken, and current percept, update the internal model/state of the world.
2. **Rule Match:** Use the internal state and current percept to decide the action by matching against a set of rules.
3. **Action:** Execute the chosen action.

**Pacman:** is a model-based reflex agent. (in the Projects)


**Evaluation Function:** Gets a state and returns a number, indicating the "goodness" of a state.

## Goal Based Agent

Goal-Based Agents operate by considering the future outcomes of their actions and how these actions will help them achieve specific goals. Unlike Simple Reflex Agents that react to the current situation without regard for the future, Goal-Based Agents have a set of desirable states they aim to reach. The decision-making process involves deliberation on which action, among many, would bring the agent closer to its goal(s).
### Characteristics:
- **Goal Information:** The agent has knowledge of one or more goals that describe desirable situations.
- **Predictive Capability:** The agent can predict the outcome of its actions.
- **Decision Making:** Decisions are made based on the likelihood of actions leading to goal achievement.
### Example:
Consider a robotic vacuum cleaner designed as a Goal-Based Agent. Instead of merely reacting to dirt detected under it (Simple Reflex) or following a set of rules to keep the internal model of the world updated (Model-Based Reflex), it also has a goal, such as "clean the entire house". The robot will evaluate which action (moving to different rooms, cleaning, recharging its battery, etc.) at any given time will maximize its chances of achieving this goal.

## Utility Based Agent
Utility-Based Agents take the concept of Goal-Based Agents further by quantifying how desirable each outcome is. Goals are a binary concept (either achieved or not), but utilities allow for a more nuanced evaluation of the state of the world. Utility is a measure of happiness or satisfaction; it's a way to express the preferences of the agent over different states.
### Characteristics:
- **Utility Function:** A utility function assigns a numerical value to each state, representing the degree of happiness or preference for that state.
- **Optimization:** The agent selects actions to maximize its utility, aiming for the highest level of satisfaction according to its preferences.
### Example:
A Utility-Based robotic vacuum cleaner might not only have the goal to clean the entire house but will also evaluate each potential action based on the utility. For example, it might assign higher utility to cleaning areas that are frequently used and lower utility to areas that are seldom dirty or used. Thus, the robot might prioritize cleaning the living room over a spare bedroom, or it might decide to recharge its battery at a strategic time that maximizes its overall utility, considering the balance between cleaning effectiveness and energy efficiency.