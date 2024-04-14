/* ***************************************************
 * Joshua Brack
 * 10/23/2019
 * Stack.java
 *
 * Combined with the generics linked list class, this file creates a Stack class.
 *************************************************** */
public class Stack<sT>
{
	private List<sT> l;
	
	//constructors
	public Stack()
	{
		l = new List<sT>();
	}
	
	public Stack(Stack<sT> s)
	{
		l = new List<sT>(s.l);
		l.First();
	}
	
	//size
	public int Size()
	{
		return l.GetSize();
	}
	
	//peek
	public sT Peek()
	{
		return l.GetValue();
	}
	
	//IsEmpty
	public boolean IsEmpty()
	{
		return l.IsEmpty();
	}
	
	//IsFull
	public boolean IsFull()
	{
		return l.IsFull();
	}
	
	//push the stack
	public void Push(sT data)
	{
		l.First();
		l.InsertBefore(data);
	}
	
	//pop the top off
	public sT Pop()
	{
		//insures we are removing the top of list
		l.First();
		sT temp = l.GetValue();
		l.Remove();
		return temp;
	}
	
	//add
	public Stack<sT> Add(Stack<sT> s)
	{
		Stack<sT> t = new Stack<sT>(); 
		t.l = this.l.Add(s.l);
		t.l.First();
		return t;
	}
	//equals
	public boolean Equals(Stack<sT> s)
	{
		return (this.l.Equals(s.l));
	}
	//print the stack
	public String toString()
	{
		return l.toString();
	}
	
	
}