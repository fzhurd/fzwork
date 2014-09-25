/*
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.
*/

public class Solution {
    public String countAndSay(int n) {
        // Start typing your Java solution below
        // DO NOT write main() function
        String result = "1";
        for (int i = 0; i < n-1; i++) {
            result = sayIt(result);
        }
        return result;
    }

    public String sayIt(String s) {
        StringBuilder buf = new StringBuilder();
        int length = s.length();
        for (int i = 0; i < length; i++) {
            int count = 1;
            while (i + 1 < length && s.charAt(i + 1) == s.charAt(i)) {
                i++;
                count++;
            }
            buf.append(String.valueOf(count) + String.valueOf(s.charAt(i)));
        }   
        return buf.toString();
    }
}