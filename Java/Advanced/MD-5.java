// https://www.hackerrank.com/challenges/java-md5/problem

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        byte[] md5 = org.apache.commons.codec.digest.DigestUtils.md5(s);
        for (byte b : md5)
            System.out.printf("%02x", b);
    }
}