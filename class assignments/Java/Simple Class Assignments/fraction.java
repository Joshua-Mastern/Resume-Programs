import java.util.Random;
class Fraction
{
	private int num;
	private int den;
	
	public Fraction()
	{
		num = 0;
		den = 1;
	}
	public Fraction(int x)
	{
		num = x;
		den = 1;
	}
	
	public Fraction(int x, int y)
	{
		num = x;
		den = y;
	}
	
	// Accesser and mutator for den
	public int getNum()
	{
		return num;
	}
	
	public void setNum(int value)
	{
		num = value;
	}

	// Accesser and mutator for den
	public int getDen()
	{
		return den;
	}
	
	public void setDen(int value)
	{
		if(value!= 0)
			den = value;
	}
	
	public String toString()
	{	
		reduce();
		return num + "/" + den + " (" + getReal()+ ")";
	}
	
	private double getReal()
	{
		return (double)num/den;
	}
	
	private void reduce()
	{
		int gcf = 1;
		int min = Math.min(Math.abs(num), Math.abs(den));
		
		for (int i = 2; i <= min; i++)
		{
			if (num % i == 0 && den% i == 0)
				gcf = i;
		}
		num /= gcf;
		den /= gcf;
		
		if(num == 0)
			den = 1;	
	}
	
	public Fraction add(Fraction other)
	{
		int newNum = (this.num*other.den) + (this.den*other.num);	
		int newDen = this.den*other.den;
		Fraction sum = new Fraction(newNum, newDen);
		
		return sum;
	}
}

class FractionTest
{
	public static void main(String[] args)
	{
		//create a fraction
		Random r = new Random();
		int [] arr = new int [10];
		Fraction [] fractions = new Fraction [10];
		
		for (int i = 0; i < fractions.length; i++)
		{
			fractions[i] = new Fraction(r.nextInt(100), r.nextInt(100));
		}
		
		for (int i = 0; i < fractions.length; i++)
			System.out.println(fractions[i]);
	}
}