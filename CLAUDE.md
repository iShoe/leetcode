# LeetCode Organization Instructions

## Project Structure
This project organizes LeetCode solutions by algorithm/data structure type:

```
leetcode/
├── arrays/
├── binary-search/
├── graphs/
├── matrices/
├── strings/
├── two-pointers/
└── README.md
```

## When organizing new LeetCode solutions:

### 1. File Organization
- New/unorganized Python files will be in the project root
- Move Python files from project root to appropriate category directories
- Categories include: arrays, binary-search, graphs, matrices, strings, two-pointers
- Create new categories if needed for different algorithm types

### 2. File Header Format
Each Python file should have a standardized header with:

```python
"""
LC #{number} - {Problem Title} ({Difficulty})
Tags: {relevant-tags}
Time: O({time-complexity}), Space: O({space-complexity})

{Problem description with examples and constraints}
"""
```

**Example:**
```python
"""
LC #242 - Valid Anagram (Easy)
Tags: hash-table, string, sorting
Time: O(n), Space: O(1)

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Constraints:
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
"""
```

### 3. README.md Updates
- Add new problems to the appropriate section in README.md
- Format: `- [Problem Title](path/to/file.py) - Difficulty`
- Keep sections alphabetically ordered
- If adding a new category, create a new section with `## Category Name`

### 4. Difficulty Levels
Use standard LeetCode difficulty levels:
- Easy
- Medium  
- Hard

### 5. Common Tags
Use relevant LeetCode tags such as:
- array, hash-table, string, math
- two-pointers, sliding-window, binary-search
- tree, graph, dfs, bfs
- dynamic-programming, greedy, backtracking
- bit-manipulation, sorting

### 6. Time/Space Complexity
- Use Big O notation: O(1), O(n), O(log n), O(n²), etc.
- Consider the most efficient solution implemented
- Space complexity should account for auxiliary space, not input space

## Workflow Steps:
1. Look for Python files in project root (unorganized files)
2. Categorize each problem by its primary algorithm/data structure
3. Move files to appropriate directories
4. Update each file header with proper format
5. Update README.md with new entries in correct sections
6. Verify all files are properly organized and documented