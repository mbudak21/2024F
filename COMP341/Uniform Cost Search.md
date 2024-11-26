---
Complete?: Yes
Optimal?: Yes, if costs are positive
Time Complexity: O(b^(C*/epsilon))
Space Complexity: O(b^(C*/epsilon))
---
# Properties
$$f(s) = g(s)+0h(s)$$
If the solution costs $C^*$ and arcs cost at least $\epsilon$, then the effective depth is roughly $C^*/\epsilon$  
![[Pasted image 20241113212409.png]]
**Uses LIFO**
Expands the deepest node first. 
Last In First Out stack

Example:
```
Stack:= [Start Node]
Stack = [N1, N2]
Stack = [N1, NN1, NN2]
Stack = [N1, NN1, NNN1, NNN2]
```

