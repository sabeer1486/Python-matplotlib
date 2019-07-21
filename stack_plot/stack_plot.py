from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

days = [1, 2, 3, 4, 5, 6, 7, 8, 9]

emp_1 = [8, 6, 5, 5, 4, 2, 1, 1, 0]
emp_2 = [0, 1, 2, 2, 2, 4, 4, 4, 4]
emp_3 = [0, 1, 1, 1, 2, 4, 3, 3, 19]

plt.stackplot(days, emp_1, emp_2, emp_3, labels=['emp_1', 'emp_2', 'emp_3'])

plt.legend(loc=(0.06, 0.03))
plt.xlabel('days')
plt.tight_layout()
plt.savefig('stack_plot.png')

plt.show()
