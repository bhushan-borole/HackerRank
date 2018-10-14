// https://www.hackerrank.com/challenges/java-1d-array/problem

import java.util.*;

public class Solution {

    private static boolean isSolvable(int[] array, int m, int i) {
        
        if (i < 0 || array[i] == 1) {
            return false;
        } else if (i + 1 >= array.length || i + m >= array.length) {
            return true;
        }
        
        array[i] = 1; 

        /* Recursive Cases (Tries +m first to try to finish game quickly) */
        return isSolvable(array, m, i + m) || 
               isSolvable(array, m, i + 1) || 
               isSolvable(array, m, i - 1);
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int q = scan.nextInt();
        while (q-- > 0) {
            int n = scan.nextInt();
            int leap = scan.nextInt();
            
            int[] game = new int[n];
            for (int i = 0; i < n; i++) {
                game[i] = scan.nextInt();
            }

            System.out.println(isSolvable(game, leap, 0) ? "YES" : "NO");
        }
        scan.close();
    }
}