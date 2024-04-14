import java.util.Random;

class RandomArray
{
	private static final int MIN = 10;
	private static final int MAX = 99;
	
	public static void main(String [] args)
	{
		Random r = new Random();
		int [] grades = new int [50];
		
		for (int i = 0; i < grades.length; i++)
			grades[i] = r.nextInt(MAX+1-MIN) + MIN;
		
		printArray(grades);
		int sum = sumArray(grades);
		System.out.println("The sum is " + sum);
	}
	
	public static void printArray(int [] arr)
	{
		for(int i = 0; i < arr.length; i++)
		{
			System.out.print(arr[i]+ ", ");
		}
	}
	
	public static int sumArray(int [] arr)
	{
		int total = 0;
		for(int i = 0; i < arr.length; i++)
		{
			total = total+ arr[i];
		}
		return total;
	}
}