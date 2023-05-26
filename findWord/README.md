# Find the needle in the Haystack

28. Find the Index of the First Occurrence in a String
Easy
3.5K
181
Companies
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.


## solution

### find()

the find method in python is used to find the first occurrence of needle in haystack

```python
index = haystack.find(needle, startHaystack, endHaystack)
```

the starting position and ending position of the haystack are optional parameters

1. value: The value to search for within the string.
2. start (optional): The index at which the search starts. If not specified, the search starts from the beginning of the string.
3. end (optional): The index at which the search ends. If not specified, the search goes until the end of the string.

it returns the first occurrence of needle - it's index