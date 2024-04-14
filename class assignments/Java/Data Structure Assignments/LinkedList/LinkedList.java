/* ***************************************************
 * Joshua Brack
 *10/9/1019
 * List.java
 *
 * List program redesigned to use a linkedList
 *************************************************** */

// the Node class
class Node
{
	private int data;
	private Node link;

	// constructor
	public Node()
	{
		this.data = 0;
		this.link = null;
	}

	// accessor and mutator for the data component
	public int getData()
	{
		return this.data;
	}

	public void setData(int data)
	{
		this.data = data;
	}

	// accessor and mutator for the links component
		
	
	public Node getLink()
	{
		return this.link;
	}

	public void setLink(Node link)
	{
		this.link = link;
	}
}

// the List class
public class List
{
	public static final int MAX_SIZE = 50;

	private Node head;
	private Node tail;
	private Node curr;
	private int num_items;

	// constructor
	// remember that an empty list has a "size" of -1 and its "position" is at -1
	public List()
	{
		head = new Node();
		tail = curr = head;
		num_items = -1;
	}

	// copy constructor
	// clones the list l and sets the last element as the current
	public List(List l)
	{
		num_items = l.num_items;
		//head set to new node
		//head data set to l.head data
		head = new Node();
		head.setData(l.head.getData());
		
		//curr new node
		//head set link to curr
		curr = head;
		
		//lcurrHold node to hold l.curr so we are free to change l.curr
		//l.curr = l.head
		Node lcurrHold = l.curr;
		l.curr = l.head.getLink();
		
		//for the length of l
			//make newNode = newNode
				//make data of newNode equal to l.curr data
			//make curr link to newNode
			//make curr newNode
		while(l.curr != null)
		{
			Node newNode = new Node();
			newNode.setData(l.curr.getData());
			
			curr.setLink(newNode);
			curr = newNode;
			l.curr = l.curr.getLink();
		}
					
		//set tail to current
		tail = curr;
		
		//set l.curr = lcurrHold
		l.curr = lcurrHold;
		
	}

	// navigates to the beginning of the list
	public void First()
	{
		curr = head;
	}

	// navigates to the end of the list
	// the end of the list is at the last valid item in the list
	public void Last()
	{
		curr = tail;
	}

	// navigates to the specified element (0-index)
	// this should not be possible for an empty list
	// this should not be possible for invalid positions
	public void SetPos(int pos)
	{
		if(!IsEmpty() && (pos < (num_items+1) && pos > 0))
		{
			curr = head;
			for(int i = 0; i<pos; i++)
				curr = curr.getLink();
		}
	}

	// navigates to the previous element
	// this should not be possible for an empty list
	// there should be no wrap-around
	public void Prev()
	{
		//Create a newNode to serve as temp var
		Node newNode = new Node();
		newNode = head;
		
		//cylce newNode to be equal to current's pos - 1
		for(int i = 0;i < (GetPos()-1); i++)
				newNode = newNode.getLink();
		
		//set curr equal to newNode
		curr = newNode;
		
	}

	// navigates to the next element
	// this should not be possible for an empty list
	// there should be no wrap-around
	public void Next()
	{
		if(!IsEmpty() && curr !=tail)
			curr = curr.getLink();
	}

	// returns the location of the current element (or -1)
	public int GetPos()
	{
		if(IsEmpty())
			return -1;
		else
		{
			//new node to cycle through linkedlist in search of curr
			Node newNode = new Node();
			newNode = head;
			int pos = 0;
			
			while(curr!= null && newNode != curr)
			{
				newNode = newNode.getLink();
				pos ++;
			}
			
			return pos;
		}
	}

	// returns the value of the current element (or -1)
	public int GetValue()
	{
		if(IsEmpty())
			return -1;
		else
			return curr.getData();
	}

	// returns the size of the list
	// size does not imply capacity
	public int GetSize()
	{
		return (num_items+1);
	}

	// inserts an item before the current element
	// the new element becomes the current
	// this should not be possible for a full list
	public void InsertBefore(int data)
	{
		if(!IsFull())
		{
			if(IsEmpty())
			{
				curr.setData(data);
				num_items++;
			}
			else if(curr == head)
			{
				curr = new Node();
				curr.setData(data);
				curr.setLink(head);
				head = curr;
				num_items++;
				
			}else
			{
				Prev();
				InsertAfter(data);
			}
		}
			
	}

	// inserts an item after the current element
	// the new element becomes the current
	// this should not be possible for a full list
	public void InsertAfter(int data)
	{
		if(!IsFull())
		{
			if(IsEmpty())
				curr.setData(data);
			else if(curr == tail)
			{
				curr = new Node();
				curr.setData(data);
				tail.setLink(curr);
				tail = curr;
			}else
			{
				//perform insertion
				Node newNode = new Node();
				newNode.setData(data);
				newNode.setLink(curr.getLink());
				curr.setLink(newNode);
					
				curr = newNode;
			}
			
			num_items++;
		}
	}

	// removes the current element (collapsing the list)
	// this should not be possible for an empty list
	public void Remove()
	{
		if(!IsEmpty())
		{
			if(num_items == 0)
			{
				head = new Node();
				curr = tail=head;
			}else if(curr == head)
			{
				Next();
				head = curr;
			}else if (curr == tail)
			{
				Prev();
				curr.setLink(null);
				tail = curr;
			}else
			{	
				//hold the current so we can use prev and next without loosing current
				Next();
				Node tempNextCurr = curr;
				//use prev twice
				Prev();Prev();
				
				curr.setLink(tempNextCurr);
				
				Next();
			}
			num_items--;
		}
	}

	// replaces the value of the current element with the specified value
	// this should not be possible for an empty list
	public void Replace(int data)
	{
		if(!IsEmpty())
			curr.setData(data);
	}

	// returns if the list is empty
	public boolean IsEmpty()
	{
		return (num_items == -1);
		
	}

	// returns if the list is full
	public boolean IsFull()
	{
		return ((num_items+1) >= MAX_SIZE);
	}

	// returns if two lists are equal (by value)
	public boolean Equals(List l)
	{
		if(GetSize() != l.GetSize())
			return false;
		
		Node tempThis = head;
		Node templ = l.head;
		while(tempThis != null)
		{
			if(tempThis.getData() != templ.getData())
				return false;
			tempThis = tempThis.getLink();
			templ = templ.getLink();
		}
		return true;
	}

	// returns the concatenation of two lists
	// l should not be modified
	// l should be concatenated to the end of *this
	// the returned list should not exceed MAX_SIZE elements
	// the last element of the new list is the current
	public List Add(List l)
	{
		
		//copy the first list
		List t = new List(this);
		
		// add on each item in the second list
		Node tempCurr = l.head;
		while(tempCurr != null)
		{
			t.InsertAfter(tempCurr.getData());
			tempCurr = tempCurr.getLink();
		}
			
		return t;
	}

	// returns a string representation of the entire list (e.g., 1 2 3 4 5)
	// the string "NULL" should be returned for an empty list
	public String toString()
	{
		if(IsEmpty())
			return "NULL";
		else
		{
			Node holdCurr = curr;
			curr = head;
			String s = "";
			
			while(curr != null)
			{
				s += curr.getData() + " ";
				curr= curr.getLink();
			}
			curr = holdCurr;
			return s;
		}
	}
}
