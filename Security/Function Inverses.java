// https://www.hackerrank.com/challenges/security-inverse-of-a-function/problem

import java.util.*;


public class Solution {
    static HashMap<Integer, Integer> map = new HashMap<>();
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int i=0;
        for(int i1=0; i1<n; i1++){
            map.put(sc.nextInt(), ++i);
        }
        //System.out.println(map.keySet());
        for(int x : map.values()){
            System.out.println(x);
        }

    }
}