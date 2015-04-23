#!/usr/bin/python
# -*- coding: utf-8 -*


def main():
	val1=  {3150: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
	0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 3063: [0.0, 176.8, 175.3, 177.0, 179.0, 
	5.6, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.9, 0.0, 0.0, 0.0, 0.0, 1.9, 0.0]}

	val2= {3150: [(7.37, 'MB'), (7.371, 'MB'), (7.37, 'MB'), (7.37, 'MB'), (7.37, 'MB'), (7.37, 'MB'), 
	(7.37, 'MB'), (7.37, 'MB'), (7.37, 'MB'), (7.37, 'MB'), (7.37, 'MB'), (7.37, 'MB'), (7.37, 'MB'), 
	(7.37, 'MB'), (7.37, 'MB'), (7.37, 'MB'), (7.37, 'MB'), (7.37, 'MB'), (7.37, 'MB')], 
	3063: [(5.53, 'GB'), (5.53, 'GB'), (5.53, 'GB'), (5.53, 'GB'), (5.53, 'GB'), (5.53, 'GB'), (5.53, 'GB'), 
	(5.53, 'GB'), (5.53, 'GB'), (5.53, 'GB'), (5.531, 'GB'), (5.53, 'GB'), (5.53, 'GB'), (5.53, 'GB'), 
	(5.53, 'GB'), (5.53, 'GB'), (5.53, 'GB'), (5.53, 'GB'), (5.53, 'GB')]}

	mem_max(val2)

	# x= [(a,new_b) for a,b in tuple_list]

# 	dct = dict(tuple)
# val = dct.get(key) 

def mem_max(input_mem):

	for (k,v) in input_mem.items():
		# print k, v
		# print k, dict(v), '*********************'
		x= [n for n,u in v]
		print x
		print calculate_sum(x)
		print calculate_avg(x)

def calculate_sum(input):
	return sum(input)

def calculate_avg(input):
	return reduce(lambda x, y: x + y, input) / len(input)


if __name__=='__main__':
	main()