__author__ = 'Kartik'

class Queue():
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def enqueue(self,item):
		return self.items.insert(0,item)

	def dequeue(self):
		return self.items.pop()

	def size(self):
		return len(self.items)

	def show(self):
		return self.items

def hot_potato(namelist,num):
	queue = Queue()
	removed_list = []
	try:
		for name in namelist:
			queue.enqueue(name)
	except:
		print('Size Zero')
	
	while queue.size() > 1:
		for i in range(num):
			queue.enqueue(queue.dequeue())

		removed_name = queue.dequeue()
		removed_list.append(removed_name)


	return removed_list, queue.items


if __name__ == '__main__':
	namelist = ['A','B','D','T','Q','K','S','L']
	num = 6

	removed_list, winner = hot_potato(namelist, num)

	print('Namelist: {}'.format(namelist))
	print('The Winner of Hot Potato is {}, removed list is {}'.format(winner, removed_list))