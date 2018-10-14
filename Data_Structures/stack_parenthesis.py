__author__ = 'Kartik'

import random


class Stack():
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def pop(self):
		return self.items.pop()

	def push(self, item):
		return self.items.append(item)

	def peek(self):
		return self.items[-1]

	def size(self):
		return len(self.items)

def parCheck(stack, par_str):
	par_list = list(par_str)
	balanced = True
	i = 0

	while i < len(par_list) and balanced:
		last_push = par_list[i] 
		if par_list[i] in '({[':
			stack.push(par_list[i])
		else:
			if stack.isEmpty():
				balanced = False
			else:
				first_out = stack.pop()
				if first_out != last_push:
					balanced = False
		i += 1

	if stack.isEmpty() and balanced:
		return balanced
	else:
		return balanced



if __name__ =='__main__':
	s = Stack()
	check = "()([])()()"

	print(parCheck(s,check))
	