__author__ = 'Kartik'
__title__ = 'Linked List'

class Node():
	def __init__(self,item):
		self.next = None
		self.data = item

	def get_data(self):
		return self.data

	def set_data(self,item):
		self.data = item

	def set_next(self,next_item):
		self.next = next_item

	def get_next(self):
		return self.next



class LinkedList():
	
	def __init__(self):
		self.head = None
		self.tail = None

	def add(self, item):
		temp = Node(item)
		if self.head == None:
			temp.set_next(None)
			self.head = temp
			self.tail = temp
		else:
			temp.set_next(self.head)
			self.head = temp

	def show(self):
		current = self.head
		
		while current is not None:
			print(current.get_data())
			current = current.get_next()

	def isEmpty(self):
		return self.head == None

	def search(self,item):
		current = self.head
		found = False

		if self.isEmpty():
			raise Exception('Empty List')
		else:
			while current is not None and not found:
				if current.get_data() == item:
					found =True
				else:
					current = current.get_next()
		return found

	def append_ll(self,item):
		if self.isEmpty():
			self.add(item)
		else:
			temp = Node(item)
			temp.set_next(None)
			self.tail.set_next(temp)
			self.tail = temp


	def remove(self, item):
		previous = None
		current = self.head
		found = False

		if self.isEmpty():
			raise Exception('Nothing to Remove')
		else:
			while current is not None and not found:
				if current.get_data() == item:
					if current.get_next() == self.tail:
						previous.set_next(None)
						self.tail = previous
					elif current != self.tail and current != self.head:
						previous.set_next(current.get_next())
						current.set_next(None)
					elif current == self.head:
						self.head = current.get_next()
						current.set_next = None
					found = True
				else:
					previous = current
					current = current.get_next()



if __name__ == '__main__':
	ll = LinkedList()
	ll.add(7)
	ll.append_ll(110)
	ll.append_ll(88)
	ll.add(100)
	ll.remove(1)

	ll.show()

	print(ll.search(6))


