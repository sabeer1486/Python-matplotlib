from matplotlib import pyplot as plt
import pandas as pd

# plt.style.use('fivethirtyeight')

data = pd.read_csv('fill_between_data.csv')

ages_x = data['Ages']
all_devs = data['All_Devs']
py_dev_y = data['Python']
js_dev_y = data['JavaScript']

plt.plot(ages_x, all_devs, linestyle='--', color='k', label='All_dev')
plt.plot(ages_x, py_dev_y, color='b', label='python')

overall_median = 57287

plt.fill_between(ages_x, py_dev_y, all_devs, where=(py_dev_y>=all_devs), 
				interpolate=True, alpha=0.25, color='b', label='Above All_dev')
plt.fill_between(ages_x, py_dev_y, all_devs, where=(all_devs>=py_dev_y), 
				interpolate=True, alpha=0.2, color='r' , label='Above Python_dev')

plt.legend()
plt.xlabel('Ages')
plt.ylabel('Median salary by ages')
plt.tight_layout()
plt.grid(True)
plt.savefig('filled_between_plot.png')

plt.show()

