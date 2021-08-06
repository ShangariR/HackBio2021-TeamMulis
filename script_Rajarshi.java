//Write a script that prints name,email,slack username (with @), biostack,twitter handle (with @) and calculate hamming distance between stack username & twitter username in that order.


public class script_Rajarshi
{
 public static void main(String args[]){
 
     String name="Rajarshi Mondal";
     String email="rajarshimondal92@gmail.com";
     String slack_username="@Rajarshi_Mondal";
     String biostack="Genomics";
     String twitter_handle="@Rajarshi568";
     int a,b,min,i;
     char c,d;
     

     // calculating the hamming distance between stack_username and twitter handle

     String string1 = slack_username;
     String string2= twitter_handle;
     int hamming_distance = 0;

     a= string1.length();
     b= string2.length();
     if (a>b)
     min=b;
     else if (b>a)
     min=a;
     else
     min=a;
     for(i=0; i<min;i++)
     {
         c= string1.charAt(i);
         d= string2.charAt(i);
     if (c!=d)
     hamming_distance= hamming_distance + 1;
     }
     System.out.print(name+ ", ");
     System.out.print(email+ ", ");
     System.out.print(slack_username+ ", ");
     System.out.print(biostack+ ", ");
     System.out.print(twitter_handle+ ", ");
     System.out.print(hamming_distance);
     
     
 }
}
