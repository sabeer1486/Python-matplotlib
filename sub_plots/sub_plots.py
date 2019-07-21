from matplotlib import pyplot as plt
import pandas as pd

# comic style
# plt.xkcd() 

data = pd.read_csv('line_plot_data.csv')
ages_x = data['Ages']
all_dev_salary = data['All_Devs']
py_dev_salary = data['Python']
js_dev_salary = data['JavaScript']

fig, ax = plt.subplots(nrows=2, ncols=2, sharex=True, sharey=True)
         
ax[0,0].plot(ages_x, all_dev_salary, label='All dev', color='k', linewidth='2', linestyle='--')
ax[0,1].plot(ages_x, py_dev_salary, label='Python', color='b')
ax[1,0].plot(ages_x, js_dev_salary, label='Java Script', color='y')
ax[1,1].plot(ages_x, js_dev_salary, label='Java', color='#FFA500')

ax[0,0].legend()
ax[0,0].set_title('Median salary (USD) by Age')
ax[0,0].set_ylabel('salary (USD)')
ax[0,0].grid()

ax[0,1].legend()
ax[0,1].set_title('Median salary (USD) by Age')
ax[0,1].grid()

ax[1,0].legend()
ax[1,0].set_ylabel('salary (USD)')
ax[1,0].set_xlabel('Ages')
ax[1,0].grid()

ax[1,1].legend()
ax[1,1].set_xlabel('Ages')
ax[1,1].grid()

plt.tight_layout()

fig.savefig('sub_plot.png')

plt.show()
