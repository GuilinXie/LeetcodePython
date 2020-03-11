# LeetCode-Solution

### Array

| ID   | Title                                                        | Solution                                                     | Difficulty | C    |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ | ---------- | ---- |
| 54   | [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/Arrary/54_SpiralMatrix.py) | Medium     | 1    |
| 59   | [Spiral Matrix 2](https://leetcode.com/problems/spiral-matrix-ii/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/Arrary/59_SpiralMatrix2.py) | Medium     | 1    |
|      |      quick sort/quicksort/quick_sort  |   [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/Arrary/quicksort_list.py) |            |      |
| 215   | [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/Arrary/215_Kth_Largest_Element_in_an_Array.py) | Medium     | 1    |
| 4   | [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/Arrary/4_Median_of_Two_Sorted_Arrays.py) | Medium     | 1    |
| 295   | [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/Arrary/295_Find_Median_from_Data_Stream.py) | Hard     | 1, heap    |
| 1375   | [Blub Switcher 3](https://leetcode.com/problems/bulb-switcher-iii/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/Arrary/1375_Bulb_Switcher_3.py) | Medium     | 1, keep a record of history, and update for every new data|

### LinkedList

| ID   | Title                                                        | Solution                                                     | Difficulty | C    | Knowledge                                      |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ | ---------- | ---- | ---------------------------------------------- |
| 138  | [Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/LinkedList/138_CopyListWithRandomPointer.py) | Medium     | 1    | LinkedList,Hashmap                             |
| 141  | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/LinkedList/141_linked_list_cycle.py) | Easy       | 1    |                                                |
| 142  | [Linked List Cycle 2](https://leetcode.com/problems/linked-list-cycle-ii/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/LinkedList/142_linked_list_cycle_2.py) | Medium     | 1    | slow & fast should move together in while loop |
| 146  | [LRU Cache](https://leetcode.com/problems/lru-cache/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/LinkedList/146_LRU_Cache.py) | Medium     | 1    | Double LinkedList, hashtable->dict |
| 2  | [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/LinkedList/2_Add_Two_Numbers.py) | Medium     | 1    | carry, digit = divmod(num,10)|

### DFS

| ID   | Title | Solution | Difficulty | Locked |
| ---- | ----- | -------- | ---------- | ------ |
|  200    |   [Number of Island](https://leetcode.com/problems/number-of-islands/)    |   [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/DFS/200_Number_of_Islands.py)       |     Medium       |    dfs func does not return     |
|    695  |  [Max Area of Island](https://leetcode.com/problems/max-area-of-island/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/DFS/695_Max_Area_of_Island.py)  | Medium | dfs func returns sum |
|      | Max Island    |[Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/DFS/maxIsland.py)|       |    Amazon Phone Interview, similar to 695   |
|    1192  |  [Critical Connections in a Network](https://leetcode.com/problems/critical-connections-in-a-network/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/DFS/1192_CriticalConnectionInANetwork.py)| Hard |  |
|    1376  |  [Time Needed to Inform All Employees](https://leetcode.com/problems/time-needed-to-inform-all-employees/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/DFS/1376_Time_Needed_to_Inform_All_Employees.py)| Medium | weighted tree ,find a path sum|
|    1376 - keep path  |  [Time Needed to Inform All Employees](https://leetcode.com/problems/time-needed-to-inform-all-employees/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/DFS/1376_path_Time_Needed_to_Inform_All_Employees.py)| Medium |get the path from 1376|
|    104  |  [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/DFS/104_Maximum_Depth_of_Binary_Tree.py)| Easy |  |
|    111  |  [Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/DFS/111_Minimum_Depth_of_Binary_Tree.py)| Easy | root->leaf,need to care about leaf condition |



### BFS

| ID   | Title                                                 | Solution                                                     | Difficulty | Locked          |
| ---- | ----------------------------------------------------- | ------------------------------------------------------------ | ---------- | --------------- |
| 542  | [01 Matrix](https://leetcode.com/problems/01-matrix/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/BFS/542_01Matrix.py) | Medium     | BFS,deque,yield |
| 994  | [Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/BFS/994_Rotting_Oranges.py) | Easy     | BFS,deque, check edges with all 0's |
|    207  |  [Course Schedule](https://leetcode.com/problems/course-schedule/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/BFS/207_Course_Schedule.py)| Medium |dfs,bfs(topological sort)  |
|    210  |  [Course Schedule 2](https://leetcode.com/problems/course-schedule/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/BFS/210_Course_Schedule_2.py)| Medium |bfs(topological sort)  |
| 1131 |                                                       |                                                              |            |                 |
|      |                                                       |                                                              |            |                 |


### String

| ID   | Title                                                        | Solution                                                     | Difficulty | C    | Knowledge |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ | ---------- | ---- | --------- |
| 12   | [Integer to Roman](https://leetcode.com/problems/integer-to-roman/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/String/12_IntegerToRoman.py) | Medium     | 1    |           |
| 13   | [Roman to Integer](https://leetcode.com/problems/roman-to-integer/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/String/13_RomanToInteger.py) | Easy       | 1    |           |
| 5    | [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/String/5_LongestPalindromicSubstring.py) | Medium     | 1    | DP        |

### Stack

| ID   | Title | Solution | Difficulty | Locked |
| ---- | ----- | -------- | ---------- | ------ |
|      |       |          |            |        |
|      |       |          |            |        |
|      |       |          |            |        |

### Hashset

| ID   | Title | Solution | Difficulty | Locked |
| ---- | ----- | -------- | ---------- | ------ |
|      |       |          |            |        |
|      |       |          |            |        |
|      |       |          |            |        |

### HashMap

| ID   | Title | Solution | Difficulty | Locked |
| ---- | ----- | -------- | ---------- | ------ |
|      |       |          |            |        |
|      |       |          |            |        |
|      |       |          |            |        |

### SlidingWindow

| ID   | Title                                                        | Solution                                                     | Difficulty | C    |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ | ---------- | ---- |
| 76   | [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/SlidingWindow/76_MinimumWindowSubstring.py) | Hard       | 1    |
| 1234 | [Replace the Substring for Balanced String](https://leetcode.com/problems/replace-the-substring-for-balanced-string/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/SlidingWindow/1234_ReplaceTheSubstringForBalancedString.py) | Medium     | 1    |
| 3 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | [Python] (https://github.com/GuilinXie/LeetcodePython/blob/master/Python/SlidingWindow/3_Longest_Substring_Without_Repeating_Characters.py)| Medium| 1    |


### Bitwise

| ID   | Title | Solution | Difficulty | Locked |
| ---- | ----- | -------- | ---------- | ------ |
|      |       |          |            |        |
|      |       |          |            |        |
|      |       |          |            |        |

### Hash

| ID   | Title | Solution | Difficulty | Locked |
| ---- | ----- | -------- | ---------- | ------ |
|      |       |          |            |        |
|      |       |          |            |        |
|      |       |          |            |        |

### Tree

| ID   | Title | Solution | Difficulty | Locked |
| ---- | ----- | -------- | ---------- | ------ |
|      |       |          |            |        |
|      |       |          |            |        |
|      |       |          |            |        |

### Trie

| ID   | Title                                                        | Solution                                                     | Difficulty | C    | Knowledge |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ | ---------- | ---- | --------- |
|      | Build and Search Trie Using dict()                           | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/Trie/BuildTrie.py) |            |      |           |
| 1233 | [Remove Sub Folders From The Filesystem](https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/Trie/1233_RemoveSubFoldersFromTheFilesystem.py) | Medium     |      |           |
|      |                                                              |                                                              |            |      |           |

### Binary Search

| ID   | Title                                                        | Solution                                                     | Difficulty | C    | Knowledge |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ | ---------- | ---- | --------- |
| 74   | [Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/BinarySearch/74_SearchA2DMatrix.py) | Medium     | 1    |           |
| 240  | [Search a 2D Matrix 2](https://leetcode.com/problems/search-a-2d-matrix-ii/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/BinarySearch/240_SearchA2DMatrix2.py) | Medium     | 1    |           |
|      |                                                              |                                                              |            |      |           |

### Sort

| ID   | Title | Solution | Difficulty | Locked |
| ---- | ----- | -------- | ---------- | ------ |
|      |       |          |            |        |
|      |       |          |            |        |
|      |       |          |            |        |


### Greedy

| ID   | Title | Solution | Difficulty | Locked |
| ---- | ----- | -------- | ---------- | ------ |
|      |       |          |            |        |
|      |       |          |            |        |
|      |       |          |            |        |

### Union Find

| ID   | Title | Solution | Difficulty | Locked |
| ---- | ----- | -------- | ---------- | ------ |
|      |       |          |            |        |
|      |       |          |            |        |
|      |       |          |            |        |

### Graph

| ID   | Title                                                        | Solution                                                     | Difficulty | C    | Knowledge                                           |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ | ---------- | ---- | --------------------------------------------------- |
| 1192 | [Critical Connection in a Network](https://leetcode.com/problems/critical-connections-in-a-network/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/DFS/1192_CriticalConnectionInANetwork.py) | Hard       | 1    | Bridge, Articulation Point (Tarjan Algorithm - DFS) |
|      |                                                              |                                                              |            |      |                                                     |
|      |                                                              |                                                              |            |      |                                                     |

### Dynamic Programming

| ID   | Title                                                        | Solution                                                     | Difficulty | C/Locked |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ | ---------- | -------- |
| 5    | [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/String/5_LongestPalindromicSubstring.py) | Medium     | 1        |
| 72   | [Edit Distance](https://leetcode.com/problems/edit-distance/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/DanamicProgramming/72_edit_distance.py) | Hard       | 1        |
|      |                                                              |                                                              |            |          |

### Heap

| ID   | Title | Solution | Difficulty | Locked |
| ---- | ----- | -------- | ---------- | ------ |
|      |       |          |            |        |
|      |       |          |            |        |
|      |       |          |            |        |

### ListIntersection

| ID   | Title                                                        | Solution                                                     | Difficulty | C    | Knowledge               |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ | ---------- | ---- | ----------------------- |
| 1229 | [Meeting Scheduler](https://leetcode.com/problems/meeting-scheduler/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/ListIntersection/1229_MeetingScheduler.py) | Medium     | 1    | List Slots Intersection |
|      |                                                              |                                                              |            |      |                         |
|      |                                                              |                                                              |            |      |                         |

### Others

| ID   | Title                                                        | Solution                                                     | Difficulty | C    | Knowledge                                                  |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ | ---------- | ---- | ---------------------------------------------------------- |
| 1    | [Walk through dir](http://nooverfit.com/wp/15%E4%B8%AA%E9%87%8D%E8%A6%81python%E9%9D%A2%E8%AF%95%E9%A2%98-%E6%B5%8B%E6%B5%8B%E4%BD%A0%E9%80%82%E4%B8%8D%E9%80%82%E5%90%88%E5%81%9Apython%EF%BC%9F/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/Others/1_walk_through_dir.py) |            | 1    | os.getcwd(), os.listdir(), os.path.join(), os.path.isdir() |
|      |                                                              |                                                              |            |      |                                                            |
|      |                                                              |                                                              |            |      |                                                            |

 

