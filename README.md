# Dsa_Test
## DSA Test Question
# Section 1:
# Question1: Find the missing Number
# Approach: To find the missing number from 1 to n:
•	Calculate the total sum on number from 1 to n using the formula n*(n+1)/2.
•	Compute the sum of given array.
•	Subtract the total sum -actual sum to find the missing number.
# Question2: Longest substring without Repeating characters
# Approach: 
•	Is using the sliding windows where 2 pointers left and right.
•	Create a set to store the character we seen.
•	If we encounter the same character then we move the left pointer to remove the windows until the charcter is removed.
•	Then print the maximum length of windows where every character is unique.
# Section 2:
# Question 3: Detect and Remove loop in linked list
# Approach: we use Floyd’s Cycle Detection Algorithm.
We move two pointer name as slow and fast at a time the slow move one step while fast move 2 step at a time
If a loop exists, the two pointers meet inside the loop
After finding the loop starting node we remove loop by the next pointer of the last node =None

# Question 4: Reverse a Linked List in Groups of K
# To reverse a linked list in groups of size k:
•	We iterate through the list and reverse nodes in groups of k.
•	After reversing a group, we recursively reverse the remaining nodes.
•	If the number of remaining nodes is less than k, we keep them as they are.
# Section 3
# Question 5: Lowest Common Ancestor (LCA)
# Approach:
•	Start from the root and recursively check for the two nodes in the left and right subtrees.
•	If both nodes are found in different subtrees, the current root is the LCA.
•	If one node is found, return it; if neither is found, return None.
# Question 6: Serialize and Deserialize a Binary Tree (Not solved)

# Section 4:
# 7. Shortest Path in an Unweighted Graph (BFS)
# Approach:
•	Initialize a dictionary distances to store the shortest distance from the start node to every other node, initially set to infinity.
•	Use a queue to explore the graph level by level.
•	For each node, update the distance of its unvisited neighbors and add them to the queue.
# 8. Detect Cycle in a Directed Graph (DFS)
•	Use a visited dictionary to track the state of each node (0 = not visited, 1 = visiting, 2 = fully processed).
•	If a node is encountered that is currently in the "visiting" state, a cycle is detected.
•	Recursively traverse all neighbors and check for cycles.

# Section 5: Not Solved
# Bonus Section:
# Question 12.Dijkstra's Algorithm
# Approach:
1.	Initialize distances: Start by setting the distance to the source node as 0, and all other nodes as infinity.
2.	Create a list of unvisited nodes: These will be nodes that haven’t been fully processed.
3.	Iterate through unvisited nodes: Continuously pick the node with the smallest known distance, update the distances of its neighboring nodes, and mark it as visited.
4.	Update distances: For each neighbor of the current node, calculate the new potential distance. If it’s shorter than the current stored distance, update it.
5.	Repeat until all nodes are visited.




