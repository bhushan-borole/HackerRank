// https://www.hackerrank.com/challenges/30-running-time-and-complexity/problem

import java.io.*;
import java.util.*;
import java.math.BigInteger;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for(int i=0; i<n; i++){
            String s = sc.next();
            BigInteger bg = new BigInteger(s);
            if(bg.isProbablePrime(5))
                System.out.println("Prime");
            else
                System.out.println("Not prime");
        }
        
    }
}