---
Complete?: Only if cycles are prevented
Optimal?: No!
Time Complexity: b^m
Space Complexity: O(bm)
---
![[Pasted image 20241113211845.png]]
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

