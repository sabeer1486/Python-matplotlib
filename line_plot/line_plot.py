from matplotlib import pyplot as plt
import pandas as pd

# comic style
# plt.xkcd() 

data = pd.read_csv('line_plot_data.csv')
ages_x = data['Ages']
all_dev_salary = data['All_Devs']
py_dev_salary = data['Python']
js_dev_salary = data['JavaScript']
         
plt.plot(ages_x, all_dev_salary, label='All dev', marker='.', color='k', linewidth='2')
plt.plot(ages_x, py_dev_salary, label='Python', color='b', marker='.')
plt.plot(ages_x, js_dev_salary, label='Java Script', color='y', marker='.')

plt.legend()

plt.title('Median salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('salary (USD)')
plt.grid(True)

plt.tight_layout()

plt.savefig('line_plot.png')

plt.show()
