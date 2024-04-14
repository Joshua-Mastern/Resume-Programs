/* ***************************************************
 * <your name>
 * <the date>
 * <the file name>
 *
 * <a simple, short program/class description>
 *************************************************** */

// the Node class
class Node<mT>
{
	private mT data;
	private Node<mT> link;

	// constructor
	public Node()
	{
		this.data = null;
		this.link = null;
	}

	// accessor and mutator for the data component
	public mT getData()
	{
		return this.data;
	}

	public void setData(mT data)
	{
		this.data = data;
	}

	// accessor and mutator for the link component
	public Node<mT> getLink()
	{
		return this.link;
	}

	public void setLink(Node<mT> link)
	{
		this.link = link;
	}
}

// the List class
public class List<mT>
{
	public static final int MAX_SIZE = 50;

	private Node<mT> head;
	private Node<mT> tail;
	private Node<mT> curr;
	private int num_items;

	// constructor
	// remember that an empty list has a "size" of -1 and its "position" is at -1
	public List()
	{
		this.head = this.tail = this.curr = null;
		this.num_items = 0;
	}

	// copy constructor
	// clones the list l and sets the last element as the current
	public List(List<mT> l)
	{
		Node<mT> n = l.head;

		this.head = this.tail = this.curr = null;
		this.num_items = 0;

		while (n != null)
		{
			this.InsertAfter(n.getData());
			n = n.getLink();
		}
	}

	// navigates to the beginning of the list
	public void First()
	{
		this.curr = this.head;
	}

	// navigates to the end of the list
	// the end of the list is at the last valid item in the list
	public void Last()
	{
		this.curr = this.tail;
	}

	// navigates to the specified element (0-index)
	// this should not be possible for an empty list
	// this should not be possible for invalid positions
	public void SetPos(int pos)
	{
		if (!this.IsEmpty() && pos >= 0 && pos < this.num_items)
		{
			this.curr = this.head;

			// move curr to the specified position
			for (int i=0; i<pos; i++)
				this.curr = this.curr.getLink();
		}
	}

	// navigates to the previous element
	// this should not be possible for an empty list
	// there should be no wrap-around
	public void Prev()
	{
		if (!this.IsEmpty() && this.curr != this.head)
		{
			Node<mT> n = this.head;

			// move n to the previous element
			while (n.getLink() != this.curr)
				n = n.getLink();

			this.curr = n;
		}
	}

	// navigates to the next element
	// this should not be possible for an empty list
	// there should be no wrap-around
	public void Next()
	{
		if (!this.IsEmpty() && this.curr != this.tail)
			this.curr = this.curr.getLink();
	}

	// returns the location of the current element (or -1)
	public int GetPos()
	{
		if (this.IsEmpty())
			return -1;

		Node<mT> n = this.head;
		int i = 0;

		// traverse the list to get the current position
		while (n != this.curr)
		{
			n = n.getLink();
			i++;
		}

		return i;
	}

	// returns the value of the current element (or -1)
	public mT GetValue()
	{
		if (this.IsEmpty())
			return null;
		else
			return this.curr.getData();
	}

	// returns the size of the list
	// size does not imply capacity
	public int GetSize()
	{
		return this.num_items;
	}

	// inserts an item before the current element
	// the new element becomes the current
	// this should not be possible for a full list
	public void InsertBefore(mT data)
	{
		if (!this.IsFull())
		{
			// if the list is empty, just insert after
			if (this.IsEmpty())
				this.InsertAfter(data);
			else
			{
				// if we're at the beginning, just create a new head that points to the current one
				if (this.curr == this.head)
				{
					this.head = new Node<mT>();
					this.head.setData(data);
					this.head.setLink(curr);
					this.curr = this.head;
					this.num_items++;
				}
				// otherwise, navigate to the previous node and insert after
				else
				{
					this.Prev();
					this.InsertAfter(data);
				}
			}
		}
	}

	// inserts an item after the current element
	// the new element becomes the current
	// this should not be possible for a full list
	public void InsertAfter(mT data)
	{
		if (!this.IsFull())
		{
			Node<mT> n = new Node<mT>();

			n.setData(data);

			// if the list is empty, everything points to the single node
			if (this.IsEmpty())
				this.head = this.tail = this.curr = n;
			else
			{
				// if we're at the end, just tack the new node on
				if (this.curr == this.tail)
				{
					this.curr.setLink(n);
					this.curr = this.tail = n;
				}
				// otherwise, change the links to insert the node
				else
				{
					n.setLink(this.curr.getLink());
					this.curr.setLink(n);
					this.curr = n;
				}
			}

			this.num_items++;
		}
	}

	// removes the current element (collapsing the list)
	// this should not be possible for an empty list
	public void Remove()
	{
		if (!this.IsEmpty())
		{
			// if we're at the beginning, reset the head
			if (this.curr == this.head)
			{
				this.head = this.curr = this.curr.getLink();

				// if we just removed the last node in the list
				if (this.head == null)
					this.tail = null;
			}
			// otherwise, go back a node and reroute around the node to be removed
			else
			{
				this.Prev();
				// and rearrange the pointer to remove this node
				this.curr.setLink(this.curr.getLink().getLink());
				// we handle removing the tail vs. other internal nodes a bit differently
				if (this.curr.getLink() == null)
					this.tail = this.curr;
				this.Next();
			}
			this.num_items--;
		}
	}

	// replaces the value of the current element with the specified value
	// this should not be possible for an empty list
	public void Replace(mT data)
	{
		if (!this.IsEmpty())
			this.curr.setData(data);
	}

	// returns if the list is empty
	public boolean IsEmpty()
	{
		return (this.head == null);
	}

	// returns if the list is full
	public boolean IsFull()
	{
		return (this.num_items == MAX_SIZE);
	}

	// returns if two lists are equal (by value)
	public boolean Equals(List<mT> l)
	{
		// the lists are not equal if they're of different sizes
		if (this.num_items != l.num_items)
			return false;

		Node<mT> p = this.head;
		Node<mT> q = l.head;

		// iterate through each list
		while (p != null)
		{
			// if any pair of elements differ, the lists are not equal
			if (p.getData() != q.getData())
				return false;
			p = p.getLink();
			q = q.getLink();
		}

		return true;
	}

	// returns the concatenation of two lists
	// l should not be modified
	// l should be concatenated to the end of *this
	// the returned list should not exceed MAX_SIZE elements
	// the last element of the new list is the current
	public List<mT> Add(List<mT> l)
	{
		// copy the first list
		List<mT> t = new List<mT>(this);
		Node<mT> n = l.head;

		// iterate through the second list and copy each element to the new list
		while (n != null && !t.IsFull())
		{
			t.InsertAfter(n.getData());
			n = n.getLink();
		}

		return t;
	}

	// returns a string representation of the entire list (e.g., 1 2 3 4 5)
	// the string "NULL" should be returned for an empty list
	public String toString()
	{
		// "NULL" if the list is empty
		if (this.head == null)
			return "NULL";
		else
		{
			Node<mT> n = this.head;
			String s = "";

			// otherwise iterate through the list and display each element separated by a space
			while (n != null)
			{
				s += n.getData() + " ";
				n = n.getLink();
			}

			return s;
		}
	}
}
