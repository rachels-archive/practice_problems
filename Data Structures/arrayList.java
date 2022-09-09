// HackerRank problem: Java Arraylist
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        
        int n = sc.nextInt();
        
        ArrayList[] arrayLists = new ArrayList[n]; //array of Array Lists
        
        
        for (int i = 0; i < n; i ++){
            
            // initialise array
            arrayLists[i] = new ArrayList();
            
            int d = sc.nextInt();
            
            // initialise array list
            for (int j = 0; j < d; j ++) {
                int val = sc.nextInt();
                arrayLists[i].add(val);
            }
        }
        
        // queries
        int q = sc.nextInt();
        for (int k = 0; k < q; k ++) {
            int row = sc.nextInt();
            int col = sc.nextInt();
            try{
                System.out.println(arrayLists[row-1].get(col-1));
            } catch (Exception e) {
                System.out.println("ERROR!");
            }
        }
    }
}
