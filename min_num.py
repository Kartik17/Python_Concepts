__author__ = 'Kartik'
__title__ = 'Minimum Number of a List'

import time
import matplotlib.pyplot as plt
import numpy as np
import timeit
from timeit import Timer
import random

def plot_graph(x_list, y_list, x_name, y_name, algo_name):
	print('Start Plotting')

	fig = plt.figure()
	ax = fig.add_subplot(111)

	ax.plot(x_list,y_list)
	ax.set_xbound(lower = min(x_list), upper = max(x_list))
	ax.set_ybound(lower = min(y_list), upper = max(y_list))
	ax.set_xlabel(x_name)
	ax.set_ylabel(y_name)
	ax.set_title(algo_name + 'Time comparison')

	plt.show()

def min_no(check_list):
	try:
		if len(check_list) == 0:
			raise Exception('Length of list is 0')
		min_num = check_list[0]
		for no in check_list:
			if min_num > no:
				min_num = no
		print('Minimum Number {}'.format(min_num))
	except:
		print('Exception Raised')


if __name__ == '__main__':
	time_list = []
	x_list = list(range(100,100000,10000))
	t1 = Timer("min_no(check)", "from __main__ import min_no , check")

	for j in x_list:
		check = random.sample(range(0,10000000),j)
		time_list.append(t1.timeit(number = 10))

	plot_graph(np.array(x_list), time_list, 'Size of List', 'Completion time', 'Minimum Number')

