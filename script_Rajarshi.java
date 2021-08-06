//Write a script that prints name,email,slack username (with @), biostack,twitter handle (with @) and calculate hamming distance between stack username & twitter username in that order.
#!/opt/java/jdk-11/bin/java --source 11
 
public class script_Rajarshi
{
 public static void main(String args[]){
 
     String name="Rajarshi Mondal";
     String email="rajarshimondal92@gmail.com";
     String slack_username="@Rajarshi_Mondal";
     String biostack="Genomics, Transcriptomics";
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
     System.out.println("Name: "+ name);
     System.out.println("Email: "+email);
     System.out.println("Slack_username: "+slack_username);
     System.out.println("Biostack: "+biostack);
     System.out.println("Twitter_handle: " +twitter_handle);
     System.out.println("Hamming_distance: "+hamming_distance);
     
     
 }
}
