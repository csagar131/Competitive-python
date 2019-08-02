import java.lang.*;
import java.util.Scanner;
public class CheckPalindrom
{
	public static void main(String args[])
 	{
	 Scanner sc = new Scanner(System.in);
	 System.out.println("enter string");
	 String str = sc.nextLine();
	 boolean flag = true;
	 System.out.println("your string is ="+str);
	 int len = str.length();
	 System.out.println("len is="+len);
	 char ch[] = str.toCharArray();
	 for(int i=0;i<len;i++)
	   System.out.print(ch[i]+" ");
	 for(int i=0;i<len/2;i++)
	 {
	   if(ch[i] != ch[len-i-1])
	   {
	     flag = false;
	   }
	 }
	 
	 if(flag == false)
	   System.out.println("\nString is not palindrom");
	 else
	   System.out.println("\nString is palindrom");
	}
	
}
