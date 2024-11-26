---
Complete?: Yes
Optimal?: Yes, if costs are equal
Time Complexity: O(b^s)
Space Complexity: O(b^m)
---
![[Pasted image 20241113211917.png]]
**Uses FIFO**
Expands the shallowest node first. 
First In First Out stack

Example:
```
Stack:= [Start Node]
Stack = [N1, N2]
Stack = [NN1, NN2, N2]
Stack = [NNN1, NNN2, NN2, N2]
```

