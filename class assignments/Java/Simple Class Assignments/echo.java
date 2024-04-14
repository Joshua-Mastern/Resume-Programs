import java.util.Scanner;

class Echo
{
	public static void main(String [] args)
	{
		int x;
		x = 0;
		// int x = 0;
		Scanner s = new Scanner(System.in);
		
		while (s.hasNextLine())
		{
			String line = s.nextLine();
			System.out.println(line);
		}		
	}
}