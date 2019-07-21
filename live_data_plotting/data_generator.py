
# for this plotting both python files neeed ot be run parallelly

import random 
import csv 
import time
import os


x_value = 0
total_1 = 1000
total_2 = 1000

field_names = ['x_value', 'total_1', 'total_2']

with open('auto_gen.csv', 'w') as csv_file:
	csv_writer = csv.DictWriter(csv_file, fieldnames=field_names)
	csv_writer.writeheader()

try:
	while 1:
		with open('auto_gen.csv', 'a') as csv_file:
			csv_writer = csv.DictWriter(csv_file, fieldnames=field_names)

			data = {
				'x_value': x_value,
				'total_1': total_1,
				'total_2': total_2
			}

			csv_writer.writerow(data)
			print(x_value, '\t', total_1, '\t', total_2)

			x_value += 1
			total_1 += random.randint(-6, 8)
			total_2 += random.randint(-5, 6)

		time.sleep(1)
except:
	os.remove('dauto_gen.csv')# after compliting file will be deleted
	print('File deleted')


