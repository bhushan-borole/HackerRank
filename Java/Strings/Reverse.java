import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        StringBuilder sb = new StringBuilder();
        sb.append(A);
        if(A.equals(sb.reverse().toString()))
            System.out.println("Yes");
        else
            System.out.println("No");
        
    }
}


