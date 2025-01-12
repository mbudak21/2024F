# Local Search
- Hill climbing
- Simulated Annealing
- Genetic Algorithms
- Particle Swarm Optimization


# Constraint Satisfaction Problems
Unlike search problems, CSPs are a type of identification problem, problems in which we must simply identify whether a state is a goal state or not, with no regard to how we arrive at that goal. CSPs are defined by three factors:

1) **Variables:** CSPs possess a set of N variables X1, ..., XN that can each take on a single value from some defined set of values
2) **Domain:** A set {x1, ..., xd } representing all possible values that a CSP variable can take on.
3) **Constraint:** Constraints define restrictions on the values of variables, potentially with regard to other variables.



# Search Formulation For CSPs
1) Initial state: {}
2) Successor(): consistent with constraints
3) Goal Test()
4) Failure
# Backtracking Search
Work on 1 variable at a time.

### Minimum Remaining Values (MRV)
Choose the variable with the fewest legal left values in its domain.
If red is choosen as a neighbor, the other cell has blue and green in domain.

The cell with least elements in its domain is chosen.

### Degree Heuristic (DH)
Tie breaker among MRV variables
Choose the variable with most constraints on remaining variables
### Least Constraining Value (LCV)
Given a choice of variable, choose the least constraining value
I.e., the one that rules out the fewest values in the remaining variables


## Filtering

### Forward Checking (naive method)
If a variable is assigned, check the domains of other variables and decrease them according to the constraints.

### Arc Consistency
1) Imagine every undirected edge in the graph as two directed edges.
2) For every edge, check the following: ex: A->B
   For every domain value in A, if a value is picked, will B still have options?
   If there would be no options for B, remove that domain value from A.

3) Since A is updated, re-add all the edges that go to A, eg: X->A


# Local Search
A different CSP solving algorithm, works with iterative improvement.
Start with some random assignment to values then iteratively select a random conflicted variable and reassing its value to the on that violtes the fewest constraints until no more constraint violations exist (known as min-conflicts heuristic)

Very time and space efficent, but incomplete and inoptimal.

Disregard the path, just focus on getting the goal state.
- Solution is the goal state itself.
- Search for a solution when the path doesn't matter
- Get to a `better` state (best if possible)

## Hill Climbing
- Not complete
- Not optimal
- $O(d)$ time complexity, d: longest path to solution (can be infinite!)
- Constant space complexity
- too greedy

```
Start from a node
Look at the best valued neighbor
Choose it
Repeat untill neighborVal < currentVal
```


## Annealing Search
Decrease random moves over time, effectively becomeing complete and optimal as the randomness is decreased slowly.