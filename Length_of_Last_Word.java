class Solution {
    public int lengthOfLastWord(String s) {
        String[] arr = s.split(" ");  // Split the input string by spaces and store the words in an array.
        return arr[arr.length - 1].length();  // Return the length of the last word in the array.
    }
}
