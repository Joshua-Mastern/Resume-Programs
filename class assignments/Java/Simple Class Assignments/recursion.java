import java.util.*;
import java.lang.Math;

class Recursion
{
	public static int total = 0;
	public static void main(String[] args)
	{
		/*
		System.out.println("F(1.5,3) is: "+F(1.5,3));
		System.out.println("F(.7,5) is: "+ F(.7,5));
		System.out.println("F(.9,10) is: "+F(.9,10));
		

		//PrintReverse(53856);
		Hanoi(2, 'A','B','C');
		System.out.println("2 discs takes: " + total+ "moves");
		total = 0;
		
		Hanoi(3, 'A','B','C');
		System.out.println("3 discs takes: " + total+ "moves");
		total = 0;
		
		Hanoi(4, 'A','B','C');
		System.out.println("4 discs takes: " + total+ "moves");
		total = 0;
		
		Hanoi(5, 'A','B','C');
		System.out.println("5 discs takes: " + total+ "moves");
		total = 0;
		
		
		/*Hanoi(64, 'A','B','C');
		System.out.println("64 discs takes: " + total+ "moves");
		total = 0;
		
		//Hanoi(343, 'A','B','C');
		//System.out.println("343 discs takes: " + total+ "moves");
		//total = 0;
		
		/*Hanoi(100, 'A','B','C');
		System.out.println("100 discs takes: " + total+ "moves");
		total = 0;*/
		//reduceTime(Math.pow(2,100));
		
		for(int i = 0;i<100; i++)
			System.out.println(i + " -> " + F(i));
	}
	
	
	/*
	public static int F(int n)
	{
		if(n<=0)
			return 0;
		return F(n/10)+n%10;
	}*/
	
	public static int F(int n)
	{
			if(n<=0)
				return 0;
			return n*F(n-1);
	}
	
	public static void Hanoi(int n, char from, char to, char spare)
	{
		if(n == 1)
		{
			System.out.println(from + "->" + to);
			total++;
			return;
		}
		Hanoi(n-1, from , spare, to);
		Hanoi(1, from, to, spare);
		Hanoi(n-1, spare, to, from);
	}
	//find the digit in one's place and print
	//find the digit in ten's place and print
	//find the digit in hundred's place and print
	//keep going until you have exhausted size of numer
	
	//base case is when I have the last digit
	//general case
	/*
	public static void PrintReverse(int n)
	{
		//base case
		if(n<10)
		{
			System.out.print(n);
			return;
		}
		
		//general case
		System.out.print(n%10);
		PrintReverse(n/10);
	}*/
	
	/*
	public static int F(int n)
	{
		if(n<=0)
			return 0;
		return n * F(n-1);
	}
	
	public static int F(double x, int n)
	{
		if(n<=0)
			return 0;
		return n + F(x, n-1);
	}*/
	
	public static void reduceTime(double n)
	{
		System.out.println((n/(365*24*60*60))+" years");
		n= n%(365*24*60*60);
		System.out.println(n/(24*60*60)+" days");
		n = n%(24*60*60);
		System.out.println(n/(60*60)+" hours");
		n = n%(60*60);
		System.out.println(n/(60)+" minutes");
		n = n%60;
		System.out.println(n+" seconds");
	}
	
}