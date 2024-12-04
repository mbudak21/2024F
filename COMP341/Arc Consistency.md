A CSP is arc consistent if:

1. For every arc $(X,Y)$ (meaning, there is a constraint between $X$ and $Y$),
2. For every value $x$ in the domain of $X$, there exists **at least one value** $y$ in the domain of $Y$ such that the constraint between $X$ and $Y$ is satisfied when $X=x$ and $Y=y$.

If any value $x$ in the domain of $X$ doesn’t have a corresponding value in the domain of $Y$ that satisfies the constraint, then $x$ can be removed from $X$’s domain.

### Example Problem:

Variables:
- X: Domain = {1, 2, 3}
- Y: Domain = {2, 3}
- Z: Domain = {1, 3}

Constraints:
1. X ≠ Y
2. Y ≠ Z

Applying Arc Consistency:
1. Arc (X, Y) with constraint X ≠ Y:
    - For X = 1, there is a compatible Y = 2 (since 1 ≠ 2) and Y = 3, so 1 remains in the domain of X.
    - For X = 2, there’s no valid Y value because Y has {2, 3}, and Y = 2 would violate X ≠ Y. So, we remove 2 from the domain of X.
    - For X = 3, there’s a compatible Y = 2 (since 3 ≠ 2), so 3 remains in the domain of X.
    - Result: Domain of X is now {1, 3}.

2. Arc (Y, Z) with constraint Y ≠ Z:
    - For Y = 2, there’s a compatible Z = 1 (since 2 ≠ 1), so 2 remains in the domain of Y.
    - For Y = 3, there’s no valid Z value because Z has {1, 3}, and Z = 3 would violate Y ≠ Z. So, we remove 3 from the domain of Y.
    - Result: Domain of Y is now {2}.

3. Revisiting Arc (X, Y) after changes:
    - Now that Y’s domain has changed, we re-check (X, Y) with the updated domains.
    - For X = 1, there’s a compatible Y = 2, so 1 remains in the domain of X.
    - For X = 3, there’s a compatible Y = 2, so 3 remains in the domain of X.
    - No further changes are needed for the domain of X.

After enforcing arc consistency:
- Domain of X: {1, 3}
- Domain of Y: {2}
- Domain of Z: {1, 3}
