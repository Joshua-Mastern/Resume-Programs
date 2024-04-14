/* ***************************************************
 * Joshua Brack
 * 10/23/2019
 * Queue.java
 *
 * Combined with the generics linked list class, this file creates a Queue class.
 *************************************************** */
public class Queue<qT>
{
	private List<qT> l;
	
	//constructors
	public Queue()
	{
		l = new List<qT>();
	}
	
	public Queue(Queue<qT> q)
	{
		l = new List<qT>(q.l);
		l.First();
	}
	
	//size
	public int Size()
	{
		return l.GetSize();
	}
	
	//peek
	public qT Peek()
	{
		l.First();
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
	
	//enqueue an item
	public void Enqueue(qT data)
	{
		l.Last();
		l.InsertAfter(data);
	}
	
	//delete an item from end of list and return item
	public qT Dequeue()
	{
		l.First();
		qT temp = l.GetValue();
		l.Remove();
		return temp;
	}
	
	//add
	public Queue<qT> Add(Queue<qT> q)
	{
		Queue<qT> t = new Queue<qT>(); 
		t.l = this.l.Add(q.l);
		return t;
	}
	
	//equals
	public boolean Equals(Queue<qT> q)
	{
		return (this.l.Equals(q.l));
	}
	
	//print the stack
	public String toString()
	{
		return l.toString();
	}
	
	
}