import java.util.*;
class fibonacci
{
	public static void main(String[] args)
	{
		//code testing
		for(int i = 0; i < 11; i++)
			System.out.print(fib(i)+" ");
	}
	
	public static int fib(int n)
	{
		if(n == 0)
			return 0;
		else if(n == 1)
			return 1;
		
		return fib(n-1)+fib(n-2);
	}
}