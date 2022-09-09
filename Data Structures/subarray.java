// Program to count the number of subarrays with negative sum (HackerRank problem)
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        
        int n = sc.nextInt();
        
        int[] a = new int[n];
        
        // initialise array
        for(int i=0; i<n;i++) {
            a[i] = sc.nextInt();
        }
        
        int count = 0; //num of negative arrays
      
        for(int j = 0; j<n ; j++){
            int sum = 0; //sum of elements of the arrays
            for(int k=j; k<n ;k++){
                sum = sum + a[k];
                if(sum < 0){
                    count +=1;
                }
            }
        } System.out.println(count);
        
        
    }
}
