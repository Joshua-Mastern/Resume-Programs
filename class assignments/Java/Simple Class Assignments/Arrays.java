import java.util.Scanner;

public class Arrays
{
	public static void main(String[] args)
	{
		int intArray[];
		intArray = new int[8];
		int sum = 0;
		
		Scanner in = new Scanner(System.in);
		
		for(int i=0;i<intArray.length;i++)
		{
			System.out.println("Enter an integer ");
			intArray[i] = in.nextInt();
		}
		
		for(int i=0; i < intArray.length; i++)
		{
			sum = sum + intArray[i];
		}
		System.out.println(sum);
	}
}