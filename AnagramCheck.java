import java.util.Scanner;

public class AnagramCheck
{
 public static void main(String args[])
 { 
      
   Scanner sc = new Scanner(System.in);
   System.out.println("enter first string");
   String str1 = sc.nextLine();
   System.out.println("enter second string");
   String str2 = sc.nextLine();
   
   char arr1[] = str1.toCharArray();
   char arr2[] = str2.toCharArray();
   
   java.util.Arrays.sort(arr1);
   java.util.Arrays.sort(arr2);
   
   int small = (arr1.length<arr2.length)?arr1.length:arr2.length;
   System.out.println(small);
   boolean flag = false;
   for(int i=0;i<small;i++)
   {
     if(arr1[i] != arr2[i])
	 {
	   flag = true;
     }
   }
   
   if(flag)
    System.out.println("string not anagram");
   else
    System.out.println("strings  are anagram");
  }
 }
