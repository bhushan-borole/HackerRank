// https://www.hackerrank.com/challenges/sha-256/problem

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        String sha256hex = org.apache.commons.codec.digest.DigestUtils.sha256Hex(s);
        System.out.println(sha256hex);
    }
}