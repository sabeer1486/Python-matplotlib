from matplotlib import pyplot as plt
import numpy as np

plt.style.use("fivethirtyeight")

# Median Developer Salaries by Age
ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

x_indexes = np.arange(len(ages_x))
width = 0.25

# Median Developer Salaries by Age
dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]
plt.bar(x_indexes - width, dev_y, color='#444444', label='All Devs', width=width)


# Median Python Developer Salaries by Age
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]
plt.bar(x_indexes, py_dev_y, color='#008fd5', label='Python', width=width)


# Median JavaScript Developer Salaries by Age
js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]
plt.bar(x_indexes + width, js_dev_y, color='#e5ae38', label='Java Script', width=width)

plt.legend()

plt.xticks(ticks=x_indexes, labels=ages_x)

plt.title('Median salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('salary (USD)')
plt.grid(True)

plt.tight_layout()

plt.savefig('bar_plot_1.png')

plt.show()
