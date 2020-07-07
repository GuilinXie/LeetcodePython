# LeetCode-Solution

### Array

| ID   | Title                                                        | Solution                                                     | Difficulty | Knowledge   |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ | ---------- | ---- |
| 54   | [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/Arrary/54_SpiralMatrix.py) | Medium     |    |
| 59   | [Spiral Matrix 2](https://leetcode.com/problems/spiral-matrix-ii/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/Arrary/59_SpiralMatrix2.py) | Medium     |     |
|      |      quick sort/quicksort/quick_sort  |   [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/Arrary/quicksort_list.py) |            |      |
| 215   | [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/Arrary/215_Kth_Largest_Element_in_an_Array.py) | Medium     |    |
| 4   | [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/Arrary/4_Median_of_Two_Sorted_Arrays.py) | Medium     |    |
| 295   | [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/Arrary/295_Find_Median_from_Data_Stream.py) | Hard     |  heap    |
| 1375   | [Blub Switcher 3](https://leetcode.com/problems/bulb-switcher-iii/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/Arrary/1375_Bulb_Switcher_3.py) | Medium     |  keep a record of history, and update for every new data|
| 1099   | [Two Sum Less Than K](https://leetcode.com/problems/two-sum-less-than-k/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/Arrary/1099_Two_Sum_Less_Than_K.py) | Medium     | sort -> two points|
| 42   | [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/Arrary/42_Trapping_Rain_Water.py) | Hard     | Different Methods|
| 348   | [Design Tic Tac Toe](https://leetcode.com/problems/design-tic-tac-toe/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/Arrary/348_Design_Tic_Tac_Toe.py) | Medium     | Store data in a tricky way|
| 1380   | [Lucky Number in a Matrix](https://leetcode.com/problems/design-tic-tac-toe/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/Arrary/1380_Lucky_Numbers_in_a_Matrix.py) | Easy     | list(list) fetch row[i], col[j], max(list), list.index(max(list))|
| 121   | [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/Arrary/121_Best_Time_to_Buy_and_Sell_Stock.py) | Easy     | different ways|
| 122   | [Best Time to Buy and Sell Stock 2](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/Arrary/122_Best_Time_to_Buy_and_Sell_Stock_2.py) | Easy | tricky thinking point|
| 238   | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/Arrary/238_Product_of_Array_Except_Self.py) | Medium | use intermediate list to keep final result to save space|
| 1390   | [Four Divisors](https://leetcode.com/problems/four-divisors/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/Arrary/1390_Four_Divisors.py) | Medium | Find divisors for a num, caution for end(i*i=n) cases|
| 204   | [Count Primes](https://leetcode.com/problems/count-primes/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/Arrary/204_Count_Primes.py) | Easy | from find divisors to mark, o(n^2) -> o(n^1.5) -> o(n*log*logn), learn from hints|
| 1362   | [Closest Divisors](https://leetcode.com/problems/closest-divisors/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/Arrary/1362_Closest_Divisors.py) | Medium | check divisors from end to 1|
|560 | [Subarray_Sum_Equals_K](https://leetcode.com/problems/subarray-sum-equals-k/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/Arrary/560_Subarray_Sum_Equals_K.py) | Medium | bf:TLE, cache subSum similar to twoSum|
|36 | [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/Arrary/36_Valid_Sudoku.py) | Medium | check block starti * 3 & startj * 3|
|37 | [Sudoku Solver](https://leetcode.com/problems/sudoku-solver/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/Arrary/37_Sudoku_Solver.py) | Hard | isValid, then place, then backtrack, note that solve needs to return True at the end |
|283 | [Move Zeroes](https://leetcode.com/problems/move-zeroes/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/Arrary/283_Move_Zeros.py) | Easy | two pointers |
|1423 | [Maximum Points You Can Obtain from Cards](https://leetcode.com/contest/weekly-contest-186/problems/maximum-points-you-can-obtain-from-cards/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/Arrary/1423_Maximum_Points_You_Can_Obtain_from_Cards.py) | Medium | left obtaining + right obtaining, if want to obtain in the middle of left, then must obtail all ones left than that |
|498 | [Diagonal_Traverse](https://leetcode.com/problems/diagonal-traverse/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/Arrary/498_Diagonal_Traverse.py) | Medium | Diagnal, row+col is the same |
|1424 | [Diagonal Traverse 2](https://leetcode.com/contest/weekly-contest-186/problems/diagonal-traverse-ii/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/Arrary/1424_Diagonal_Traverse_2.py) | Medium | similar to 498 |



### LinkedList
| ID   | Title                                                        | Solution                                                     | Difficulty | Knowledge |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ | ---------- | ---------------------------------------------- |
| 138  | [Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/LinkedList/138_CopyListWithRandomPointer.py) | Medium     | LinkedList,Hashmap |
| 141  | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/LinkedList/141_linked_list_cycle.py) | Easy|   |
| 142  | [Linked List Cycle 2](https://leetcode.com/problems/linked-list-cycle-ii/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/LinkedList/142_linked_list_cycle_2.py) | Medium | slow & fast should move together in while loop |
| 146  | [LRU Cache](https://leetcode.com/problems/lru-cache/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/LinkedList/146_LRU_Cache.py) | Medium | Double LinkedList, hashtable->dict |
| 2  | [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/LinkedList/2_Add_Two_Numbers.py) | Medium | carry, digit = divmod(num,10)|
| 206  | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/LinkedList/206_Reverse_Linked_List.py) | Easy | 2 ways to reverse in-place|
| 876  | [Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/LinkedList/876_Middle_of_the_Linked_list.py) | Easy | slow & fast two points|

### DFS
| ID   | Title | Solution | Difficulty | Knowledge |
| ---- | ----- | -------- | ---------- | ------ |
|  200    |   [Number of Island](https://leetcode.com/problems/number-of-islands/)    |   [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/DFS/200_Number_of_Islands.py)       |     Medium       |    dfs func does not return     |
|    695  |  [Max Area of Island](https://leetcode.com/problems/max-area-of-island/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/DFS/695_Max_Area_of_Island.py)  | Medium | dfs func returns sum |
|      | Max Island    |[Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/DFS/maxIsland.py)|       |    Amazon Phone Interview, similar to 695   |
|    1192  |  [Critical Connections in a Network](https://leetcode.com/problems/critical-connections-in-a-network/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/DFS/1192_CriticalConnectionInANetwork.py)| Hard |  |
|    1376  |  [Time Needed to Inform All Employees](https://leetcode.com/problems/time-needed-to-inform-all-employees/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/DFS/1376_Time_Needed_to_Inform_All_Employees.py)| Medium | weighted tree ,find a path sum|
|     |  [Time Needed to Inform All Employees](https://leetcode.com/problems/time-needed-to-inform-all-employees/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/DFS/1376_path_Time_Needed_to_Inform_All_Employees.py)| Medium |get all the paths from 1376|
|    1391 |  [Check if There is a Valid Path in a Grid](https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/DFS/1391_Check_if_There_is_a_Valid_Path_in_a_Grid.py)| Medium |check i,j edge & whether visited & extra direction conditions, dfs check these before going into next dfs(new_i, new_j)|
|    93 |  [Restore IP Address](https://leetcode.com/problems/restore-ip-addresses/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/DFS/93_Restore_IP_Address.py)| Medium |dfs, backtrack, check dfs conditions before going into the next dfs|
| 139   | [Word Break](https://leetcode.com/problems/word-break/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/String/139_Word_Break.py) | Medium | dfs+recursive|
|    140  |  [Word Break2](https://leetcode.com/problems/word-break-ii/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/BFS/140_Word_Break_2.py)| Hard |dfs+recursive+cache(local variable), bfs(store ending index for the word)  | 
|    46  |  [Permutations](https://leetcode.com/problems/permutations/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/DFS/46_Permutations.py)| Medium |dfs  + backtracking, from itertools import permutations, O(n * n!) time | 
|  39|[Combination Sum](https://leetcode.com/problems/combination-sum/)|[Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/DFS/39_Combination_Sum.py)| Medium |dfs, backtracking, from itertools import combinations | 


### BFS
| ID   | Title                                                 | Solution                                                     | Difficulty | Knowledge |
| ---- | ----------------------------------------------------- | ------------------------------------------------------------ | ---------- | --------------- |
| 542  | [01 Matrix](https://leetcode.com/problems/01-matrix/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/BFS/542_01Matrix.py) | Medium     | BFS,deque,yield |
| 994  | [Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/BFS/994_Rotting_Oranges.py) | Easy     | BFS,deque, check edges with all 0's |
|    207  |  [Course Schedule](https://leetcode.com/problems/course-schedule/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/BFS/207_Course_Schedule.py)| Medium |dfs,bfs(topological sort)  |
|    210  |  [Course Schedule 2](https://leetcode.com/problems/course-schedule-ii/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/BFS/210_Course%20Schedule_2.py)| Medium |bfs(topological sort)  |
|    127  |  [Word Ladder](https://leetcode.com/problems/word-ladder/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/BFS/127_Word_Ladder.py)| Medium | bfs, construct_dict for neighbors | 
|    126  |  [Word Ladder 2](https://leetcode.com/problems/word-ladder-ii/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/BFS/126_Word_Ladder_2.py)| Hard |bfs, store all shortest path, need to store current path_length, and the first time shortest_path | 
|    1311  |  [Get Watched Videos by Your Friends](https://leetcode.com/problems/get-watched-videos-by-your-friends/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/BFS/1311_Get_Watched_Videos_by_Your_Friends.py)| Medium ||


### String
| ID   | Title                                                        | Solution                                                     | Difficulty | Knowledge |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ | ---------- | --------- |
| 12   | [Integer to Roman](https://leetcode.com/problems/integer-to-roman/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/String/12_IntegerToRoman.py) | Medium     |           |
| 13   | [Roman to Integer](https://leetcode.com/problems/roman-to-integer/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/String/13_RomanToInteger.py) | Easy       |           |
| 819   | [Most_Common_Word](https://leetcode.com/problems/most-common-word/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/String/819_Most_Common_Word.py) | Easy | string separate by different punctuations, get max from Counter, stopwords|
| 1360   | [Number of Days Between Two Dates](https://leetcode.com/problems/number-of-days-between-two-dates/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/String/1360_Number_of_Days_Between_Two_Dates.py) | Easy | leapyear, different days in months|
| 28   | [Implement strStr()](https://leetcode.com/problems/implement-strstr/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/String/28_Implement_strStr.py) | Easy | Naive or KMP, tricky to understand getNext for KMP|
| 1392   | [Longest Happy Prefix](https://leetcode.com/problems/longest-happy-prefix/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/String/1392_Longest_Happy_Prefix.py) | Hard | Naive, use KMP getNext idea to solve|
| 125   | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/String/125_Valid_Palindrome.py) | Easy | str.isalnum() [a-zA-Z0-9] return True|


### Tree
| ID   | Title | Solution | Difficulty | Knowledge |
| ---- | ----- | -------- | ---------- | ------ |
|    104  |  [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/DFS/104_Maximum_Depth_of_Binary_Tree.py)| Easy |  |
|    111  |  [Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/DFS/111_Minimum_Depth_of_Binary_Tree.py)| Easy | root->leaf,need to care about leaf condition |
|    110  |  [Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/Tree/110_Balanced_Binary_Tree.py)| Easy | check if balanced|
|    1328 |  [Balance a Binary Search Tree](https://leetcode.com/problems/balance-a-binary-search-tree/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/Tree/1382_Balance_a_Binary_Search_Tree.py)| Medium | inorder traversal, convert to BST 108 |
|    98 |  [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/Tree/98_Validate_Binary_Search_Tree.py)| Medium | keep boundary, or find left_max && right_min |
|    236 |  [Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/Tree/236_Lowest_Common_Ancestor_of_a_Binary_Tree.py)| Medium | path, multiple path |
|    572 |  [Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/Tree/572_Subtree_of_Another_Tree.py)| Easy | subtree, same tree |
|    106 |  [Construct Binary Tree from Inorder and Postorder](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/Tree/106_Construct_Binary_Tree_from_Inorder_and_Postorder_Traversal.py)| Medium | recursive |
|    112 |  [Path Sum](https://leetcode.com/problems/path-sum/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/Tree/112_Path_Sum.py)| Easy | dfs recursive, dfs iterate stack, bfs iterate queue, stack(list.pop()), queue(list.pop(0)) |
|    113 |  [Path Sum 2](https://leetcode.com/problems/path-sum-ii/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/Tree/113_Path_Sum_2.py)| Medium | Store multiple sum paths |
|    297 |  [Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/Tree/297_Serialize_and_Deserialize_Binary_Tree.py)| Hard | preOrder serialize, then need to use preOrder deserialize |
|    108  |  [Convert Sorted Array to Binary Search Tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/Tree/108_Convert_Sorted_Array_to_Binary_Search_Tree.py)| Easy | |
|    1008  |  [Convert Preorder Array to Binary Search Tree](https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/Tree/1008_Construct_BST_from_Preorder_Traversal.py)| Medium | |

### Trie
| ID   | Title                                                        | Solution                                                     | Difficulty | Knowledge |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ | ---------- | --------- |
|      | Build and Search Trie Using dict()                           | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/Trie/BuildTrie.py) |            |      |
| 1233 | [Remove Sub Folders From The Filesystem](https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/Trie/1233_RemoveSubFoldersFromTheFilesystem.py) | Medium     |  variant of trie, trie stores character, here it can store a word as a node data    |   
| 642 | [Design Search Autocomplete System](https://leetcode.com/problems/design-search-autocomplete-system/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/Trie/642_Design_Search_Autocomplete_System.py) | Hard     | build trie, search trie, add autocomplete recommend words with dfs | 
| 208 | [Implement Trie(Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/Trie/208_Implement_Trie_Prefix_Tree.py) | Medium     | build trie with dict(), search, and search with prefix|
| 79 | [Word Search](https://leetcode.com/problems/word-search) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/DFS/79_Word_Search.py) | Medium     |  DFS, backtracking    | 
| 208 | [Word Search 2](https://leetcode.com/problems/word-search-ii/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/Trie/212_Word_Search_2.py) | Hard | when to return, when not return, backtracking, trie| 


### Binary Search
| ID   | Title                                                        | Solution                                                     | Difficulty| Knowledge |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ | ---------- | --------- |
| 74   | [Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/BinarySearch/74_SearchA2DMatrix.py) | Medium    |           |
| 240  | [Search a 2D Matrix 2](https://leetcode.com/problems/search-a-2d-matrix-ii/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/BinarySearch/240_SearchA2DMatrix2.py) | Medium     |           |


### SlidingWindow
| ID   | Title                                                        | Solution                                                     | Difficulty | Knowledge   |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ | ---------- | ---- |
| 76   | [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/SlidingWindow/76_MinimumWindowSubstring.py) | Hard       |    |
| 1234 | [Replace the Substring for Balanced String](https://leetcode.com/problems/replace-the-substring-for-balanced-string/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/SlidingWindow/1234_ReplaceTheSubstringForBalancedString.py) | Medium     |    |
| 3 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/SlidingWindow/3_Longest_Substring_Without_Repeating_Characters.py)| Medium|    |
| 978 | [Longest Turbulent Subarray](https://leetcode.com/problems/longest-turbulent-subarray/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/SlidingWindow/978_Longest_Turbulent_Subarray.py)| Medium|    |
| 1004 | [Max Consecutive Ones](https://leetcode.com/problems/max-consecutive-ones-iii/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/SlidingWindow/1004_Max_Consecutive_Ones_3.py)| Medium|    |
| 525 | [Contiguous Array](https://leetcode.com/problems/contiguous-array/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/SlidingWindow/525_Contiguous_Array.py)| Medium| similar to [Longest sub-array having sum k](https://www.geeksforgeeks.org/longest-sub-array-sum-k/)|
| 560 | [Subarray Sum Equals K_CountHowManySuchSubarrays](https://leetcode.com/problems/subarray-sum-equals-k/)| [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/SlidingWindow/560_Subarray_Sum_Equals_K_countHowManySuchSubarray.py)| Medium| Also similar to [Longest sub-array having sum k](https://www.geeksforgeeks.org/longest-sub-array-sum-k/)|

### Stack

| ID   | Title | Solution | Difficulty | Knowledge |
| ---- | ----- | -------- | ---------- | ------ |
| 739   | [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/Stack/739_Daily_Temperatures.py) | Medium | last in first out, otherwise store them for next out |
| 155   | [Min Stack](https://leetcode.com/problems/min-stack/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/Stack/155_Min_Stack.py) | Easy | Store a tuple with two values in the stack |

### Graph
| ID   | Title                                                        | Solution                                                     | Difficulty | Knowledge                                           |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ | ---------- | --------------------------------------------------- |
| 1192 | [Critical Connection in a Network](https://leetcode.com/problems/critical-connections-in-a-network/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/DFS/1192_CriticalConnectionInANetwork.py) | Hard       | Bridge, Articulation Point (Tarjan Algorithm - DFS) |


### Dynamic Programming, dp
| ID   | Title                                                        | Solution                                                     | Difficulty | Knowledge |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ | ---------- | -------- |
| 5    | [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/DanamicProgramming/5_LongestPalindromicSubstring.py) | Medium     | dp|
| 72   | [Edit Distance](https://leetcode.com/problems/edit-distance/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/DanamicProgramming/72_edit_distance.py) | Hard       | recursive, dp        |
| 718   | [Maximum Length of Repeated Subarray](https://leetcode.com/problems/maximum-length-of-repeated-subarray/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/DanamicProgramming/718_Maximum_Length_of_Repeated_Subarray.py) | Medium   |   Recursive, dp, same to Longest Common Substring |
| 1143   | [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/DanamicProgramming/1143_Longest_Common_Subsequence.py) | Medium | Recursive, cache, dp, relative order, similar to Longest Common Substring  |
| 53   | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/DanamicProgramming/53_Maximum_Subarray.py) | Easy | Define problems in d p idea  |
|    | [0 1 backpack]() | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/DanamicProgramming/0_1_backpacking.py) |  | recursive, recursive+cache, 01 backpack  |
| 416   | [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/DanamicProgramming/416_Partition_Equal_Subset_Sum.py) | Medium | several number sums to a target, bool return. 0-1 bagProblem, pick or not pick, recursive+cache & dp  |


### Heap
| ID   | Title | Solution | Difficulty | Knowledge |
| ---- | ----- | -------- | ---------- | ------ |
|1383| [Maximum Performance of a Team](https://leetcode.com/problems/maximum-performance-of-a-team/) |  [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/Heap/1383_Maximum_Performance_of_a_Team.py)   |     Hard       |    Priority Queue    |
|1167| [Minimum Cost to Connect Sticks](https://leetcode.com/problems/minimum-cost-to-connect-sticks/) |  [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/Heap/1167_Minimum_Cost_to_Connect_Sticks.py)   |     Medium  |     |
|1102| [Path With Maximum Minimum Value](https://leetcode.com/problems/path-with-maximum-minimum-value/) |  [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/Heap/1102_Path_With_Maximum_Minimum_Value.py) |  Medium  | Max Heap, choose max() to store, priority queue |
|692| [Top K Frequent Words](https://leetcode.com/problems/top-k-frequent-words/) |  [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/Heap/692_Top_K_Frequent_Words.py) |  Medium  | statistics count, sort to get topK, or use heap to get topK|
|621| [Task Scheduler](https://leetcode.com/problems/task-scheduler/) |  [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/Heap/621_Task_Scheduler.py) |  Medium  | max heap - priority queue, top=heappop(hq) first, then modify the top, then heappush it back again. If want to use heappop(), have to use heapify(list) && heappush(new_num), otherwise heapop() will just work as popleft() || pop(0), and won't do its min_heap or max_heap job|


### ListIntersection
| ID   | Title                                                        | Solution                                                     | Difficulty | Knowledge               |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ | ---------- | ----------------------- |
| 1229 | [Meeting Scheduler](https://leetcode.com/problems/meeting-scheduler/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/ListIntersection/1229_MeetingScheduler.py) | Medium | List Slots Intersection |
| 56 | [Merge Intervals](https://leetcode.com/problems/merge-intervals/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/ListIntersection/56_Merge_Intervals.py) | Medium | Intervals update trick |


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


### Bitwise
| ID   | Title | Solution | Difficulty | Knowledge |
| ---- | ----- | -------- | ---------- | ------ |
|      |       |          |            |        |
|      |       |          |            |        |
|      |       |          |            |        |

### Hash
| ID   | Title | Solution | Difficulty | Knowledge |
| ---- | ----- | -------- | ---------- | ------ |
|      |       |          |            |        |
|      |       |          |            |        |
|      |       |          |            |        |


| ID   | Title | Solution | Difficulty | Knowledge |
| ---- | ----- | -------- | ---------- | ------ |
|      |       |          |            |        |
|      |       |          |            |        |
|      |       |          |            |        |


### Greedy
| ID   | Title | Solution | Difficulty | knowledge |
| ---- | ----- | -------- | ---------- | ------ |
|      |       |          |            |        |
|      |       |          |            |        |
|      |       |          |            |        |


### Union Find
| ID   | Title | Solution | Difficulty | knowledge |
| ---- | ----- | -------- | ---------- | ------ |
|      |       |          |            |        |
|      |       |          |            |        |
|      |       |          |            |        |

### Shell
| ID   | Title | Solution | Difficulty | knowledge |
| ---- | ----- | -------- | ---------- | ------ |
| 193   | [Valid Phone Numbers](https://leetcode.com/problems/valid-phone-numbers/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Shell/193_Valid_Phone_Numbers.py) | Easy | awk, regex  |



### Others
| ID   | Title                                                        | Solution                                                     | Difficulty | C    | Knowledge                                                  |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ | ---------- | ---- | ---------------------------------------------------------- |
| 1    | [Walk through dir](http://nooverfit.com/wp/15%E4%B8%AA%E9%87%8D%E8%A6%81python%E9%9D%A2%E8%AF%95%E9%A2%98-%E6%B5%8B%E6%B5%8B%E4%BD%A0%E9%80%82%E4%B8%8D%E9%80%82%E5%90%88%E5%81%9Apython%EF%BC%9F/) | [Python](https://github.com/GuilinXie/LeetcodePython/blob/master/Python/Others/1_walk_through_dir.py) |            | 1    | os.getcwd(), os.listdir(), os.path.join(), os.path.isdir() |
