import java.util.*;
class Sorting
{
	public static void main(String[] args)
	{
		int[] numbers = {9,5,7,1,3};
		System.out.println("Before sort: " +Arrays.toString(numbers));
		
		bubbleSort(numbers);
		System.out.println("After sort: " + Arrays.toString(numbers));
	}
	
	public static void bubbleSort(int[] list)
	{
		int temp;
		// compare i index to i+ and if greater swap them
		for (int i = 0; i < list.length-1; i++)
		{
			for(int j = 0; j< list.length-i-1; j++)
			{
				if(list[j] > list[j+1])
				{
					temp = list[j+1];
					list[j+1] = list[j];
					list[j] = temp;
				}
			}
		}
	}
}