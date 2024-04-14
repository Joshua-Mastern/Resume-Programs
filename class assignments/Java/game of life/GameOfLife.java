import java.io.*;

class GameOfLife
{	
	private static int size;
	private static int gen;
	
	public static void main(String[] args)
	{
		gen = ((args.length == 0) ? 10 : Integer.parseInt(args[0]));
		boolean[][] board = readFile();
		for(int i = 0; i<gen; i++)
		{
			printBoard(board, i);
			board = computeNext(board);
			try
			{
				Thread.sleep(1000);
			}
			catch(Exception e)
			{
				System.out.println(e);
			}
		}
		
	}
	
	public static boolean[][] readFile()
	{
		int i = 0;
		boolean[][] board = null;
		try
		{
			BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
			String line;
			
			while((line = br.readLine()) != null)
			{
				if(i == 0)
				{
					size = line.length();
					board = new boolean[size][size];
				}
				fillBoard(board, i, line);
				i++;
			}
			br.close();
		}
		catch(Exception e)
		{
			System.out.println(e);
		}
		return board;
	}
	
	public static void fillBoard(boolean[][] brd, int row, String line)
	{
		for(int i = 0; i < line.length(); i++)
			brd[row][i] = (line.charAt(i) == '*') ? true : false;
				
	}
	
	public static void printBoard(boolean[][] brd, int gen)
	{	
		try
		{
			new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();
		}
		catch(Exception e)
		{
			System.out.println(e);
		}
	
		System.out.println("Generation " + gen + "\n\n");
		for(int i = 0; i < brd.length; i++)
		{
			for (int j = 0; j < brd[i].length; j++)
			{
				//System.out.print(brd[i][j] + " ");
				System.out.print(brd[i][j] ? '*' : " ");
			}
			System.out.println();
		}
	}
	
	public static boolean[][] computeNext(boolean[][] old)
	{
		boolean[][] newbrd = new boolean[old.length][old.length];
		
		for(int i =1; i < old.length - 1; i++)
		{
			for(int j = 1; j < old[i].length - 1; j++)
			{
				int neighbors = countNeigh(old, i, j);
				
				if(old[i][j])
				{
					newbrd[i][j] = (neighbors == 2 || neighbors == 3);
				}
				else
				{
					newbrd[i][j] = (neighbors == 3);
				}
			}
		}
		
		return newbrd;
	}
	
	public static int countNeigh(boolean[][] brd, int a, int b)
	{
		int neigh = 0;
		for(int i = -1; i <= 1; i++)
			for(int j = -1; j <= 1; j++)
				if(!(i == 0 && j == 0) && brd[a + i][b + j])
					neigh++;
		
		return neigh;
	}
	
}