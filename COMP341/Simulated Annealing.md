*Idea:* [[Hill Climbing]] is too greedy, never moving downhill is incomplete and unacceptable. 
*Solution:* 
1. Add a temperature parameter `T`, which decreases over time.
2. Select a random neighbor and calculate the change in value.
3. If the change is positive, move to the next state. Else, move with probability T.

**If `T` is decreased "slow enough", then SA is probabilistically complete and globally optimal.**
