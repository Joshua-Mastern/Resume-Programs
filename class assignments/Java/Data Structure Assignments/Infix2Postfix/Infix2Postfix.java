/* ***************************************************
 * Joshua Brack
 * 11/6/2019
 * Infix2Postfix.java
 *
 * Takes a mathematic expression as string, convert it to postfix and then evaluate the postfix.
 *************************************************** */
import java.util.*;

class Infix2Postfix
{
	public static void main (String[] args)
	{
		Scanner input = new Scanner(System.in);
		Queue<String> infixQ = new Queue<String>();
		Queue<String> postfixQ = new Queue<String>();
		Stack<String> evaluation = new Stack<String>();
		
		while(input.hasNextLine())
		{
			//read standard input		
			String line = input.nextLine();
			infixQ = line2InfixQ(line);
			//create postfix version from infix
			postfixQ = infixQ2PostfixQ(infixQ);
			//evaluate postfix expression
			evaluation = evalPost(postfixQ);
			//print output; infix expression\npostfix expression\nevalutaion\nevalutaion\n
			System.out.print(infixQ+"\n"+postfixQ+"\n"+evaluation+"\n\n");
		}
	}
	
	public static Queue<String> line2InfixQ(String line)
	{
		//empty queue
		Queue<String> infixQ = new Queue<String>();
		
		//for every char in string line
			//infixQ.enqeue()
		for (int i = 0; i < line.length(); i++)
		{
			infixQ.Enqueue(Character.toString(line.charAt(i)));
		}
		return infixQ;
	}
	
	public static Queue<String> infixQ2PostfixQ(Queue<String> infixQ)
	{
		Queue<String> infixQL = new Queue<String>();
		infixQL=infixQL.Add(infixQ);
		Queue<String> postfixQL = new Queue<String>();
		Stack<String> operS = new Stack<String>();
		String token = null;
		String op = null;
		
		while(!infixQL.IsEmpty())
		{
			token = infixQL.Dequeue();
			if(Character.isDigit(token.charAt(0)))
			{
				postfixQL.Enqueue(token);
			}
			else if( token.equals(")"))
			{
				op = operS.Pop();
				while(!op.equals("("))
				{
					postfixQL.Enqueue(op);
					op = operS.Pop();
				}
			}
			else
			{
				op = operS.Peek();
				while(stack_priority(op) >= infix_priority(token))
				{
					op = operS.Pop();
					postfixQL.Enqueue(op);
					op = operS.Peek();
				}
				operS.Push(token);
			}
		}
		
		while(!operS.IsEmpty())
		{
			op = operS.Pop();
			postfixQL.Enqueue(op);
		}
		
		return postfixQL;
	}
	
	public static int stack_priority(String op)
	{
		if(op == null)
			return 0;
		if(op.equals("^"))
			return 2;
		else if(op.equals("*"))
			return 2;
		else if(op.equals("/"))
			return 2;
		else if(op.equals("+"))
			return 1;
		else if(op.equals("-"))
			return 1;
		else
			return 0;
	}
	public static int infix_priority(String token)
	{
		if(token == null)
			return 0;
		else if(token.equals("("))
			return 4;
		else if(token.equals("^"))
			return 3;
		else if(token.equals("*"))
			return 2;
		else if(token.equals("/"))
			return 2;
		else if(token.equals("+"))
			return 1;
		else if(token.equals("-"))
			return 1;
		else
			return 0;
	}
	
	public static Stack<String> evalPost(Queue<String> postfixQ)
	{
		//we have to create a new queue with the same values as the object we're passing in to avoid overiding the object we passed in.
		Queue<String> postfixQL = new Queue<String>();
		postfixQL= postfixQL.Add(postfixQ);
		
		Stack<String> evalS = new Stack<String>();
		
		while(!postfixQL.IsEmpty())
		{
			if(Character.isDigit(postfixQL.Peek().charAt(0)))
			{
				evalS.Push(postfixQL.Dequeue());
			}
			else
			{
				//I defined b before a, so that it would be more intuitive as I did operations like -,/ and ^ 
				//(where the commutative property doesn't apply)
									
				float b = Float.valueOf(evalS.Pop());
				
				float a = Float.valueOf(evalS.Pop());
				
				if(postfixQL.Peek().equals("+"))
				{
					float temp = a+b;
					evalS.Push(String.valueOf(temp));
					postfixQL.Dequeue();
				}else if (postfixQL.Peek().equals("-"))
				{
					float temp = a-b;
					evalS.Push(String.valueOf(temp));
					postfixQL.Dequeue();
				}else if (postfixQL.Peek().equals("/"))
				{
					float temp = a/b;
					evalS.Push(String.valueOf(temp));
					postfixQL.Dequeue();
				}else if (postfixQL.Peek().equals("*"))
				{
					float temp = a*b;
					evalS.Push(String.valueOf(temp));
					postfixQL.Dequeue();
				}else if (postfixQL.Peek().equals("^"))
				{
					float temp = a;
					for(float i = 1;i<b;i++)
						temp = temp*a;
					evalS.Push(String.valueOf(temp));
					postfixQL.Dequeue();
				}
			}
		}
		return evalS;
	}
				
}