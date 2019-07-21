
# first run the data_generator python file

from matplotlib import pyplot as plt
import pandas as pd
from matplotlib.animation import FuncAnimation
from threading import Thread
import os

def animate(i):
	data = pd.read_csv('auto_gen.csv')
	x_vals = data['x_value']
	y1_vals = data['total_1']
	y2_vals = data['total_2']

	plt.cla()
	plt.plot(x_vals, y1_vals, label='Channel 1')
	plt.plot(x_vals, y2_vals, label='Channel 2')
	plt.legend(loc='upper left')
	plt.grid(True)
	plt.tight_layout()

ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.show()

