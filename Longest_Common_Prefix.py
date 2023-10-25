class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 0) {
            return "";  // If the input array is empty, there is no common prefix.
        }
        boolean place = true;
        String pre = "";  // Initialize an empty string to store the common prefix.
        int index = 0;  // Initialize an index to keep track of the character position.

        while (place) {
            if (index >= strs[0].length()) {
                return pre;  // If the index is out of bounds of the first string, return the common prefix found so far.
            }
            char curr = strs[0].charAt(index);  // Get the character at the current index of the first string.
            
            for (int i = 1; i < strs.length; i++) {
                if (index >= strs[i].length() || strs[i].charAt(index) != curr) {
                    return pre;  // If the index is out of bounds of the current string or the character doesn't match, return the common prefix found so far.
                }
            }
            
            pre = pre + curr;  // Append the current character to the common prefix.
            index++;
        }
        
        return pre;  // Return the common prefix found.
    }
}
