class MyGrade
{
	public static void main(String [] args)
	{
		double score = 87.5;
		char letter_grade;
		letter_grade = getMyGrade(score);
		System.out.println("Your score is " + score + "which is a/an " + letter_grade);
	}
	
	public static char getMyGrade(double x)
	{
		if (x > 89.5)
			turn 'A';
		else if (x > 79.5)
			return 'B';
		else if (x > 69.5)
			return 'C';
		else if (x > 59.5)
			return 'D';
		else
			return 'F';
	}
}