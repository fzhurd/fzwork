/*
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example, 
Given s = "Hello World",
return 5.
*/

public class Solution {
    public int lengthOfLastWord(String s) {
        // Start typing your Java solution below
        // DO NOT write main() function
       String[] splitedStr = s.split("\\s+");
       if (splitedStr.length==0)
       {
           return 0;
       }
       else 
       {
           int len= splitedStr.length;
           int theWordLen = splitedStr[len-1].length();
           return theWordLen;
       }
    }
}