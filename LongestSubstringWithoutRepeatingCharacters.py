class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Create a set to store unique characters in the current substring
        charSet = set()
        
        l = 0  # Initialize the left pointer of the substring
        res = 0  # Initialize the result (length of the longest substring)
        
        for r in range(len(s)):  # Iterate through the characters of the string
            while s[r] in charSet:
                # If the character at the right pointer already exists in the substring, 
                # remove the leftmost character from the substring and move the left pointer
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])  # Add the character at the right pointer to the substring
            res = max(res, r - l + 1)  # Update the result with the maximum substring length
        
        return res  # Return the length of the longest substring without repeating characters
