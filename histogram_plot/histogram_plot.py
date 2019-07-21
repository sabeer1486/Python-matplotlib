from matplotlib import pyplot as plt
import pandas as pd

# plt.style.use('fivethirtyeight')

data = pd.read_csv('histogram_plot_data.csv')

responder_ids = data['Responder_id']
respondents_age = data['Age']

bins = [0,10,20,30,40,40,50,60,70,80,90,100]

plt.hist(respondents_age, bins=bins, edgecolor='k', color='g')

median_age = 29
color = "#fc4f30"

plt.axvline(median_age, color=color, label="Median age")

plt.legend()
plt.title('Ages of Respondents')
plt.xlabel('Ages')
plt.ylabel('Total Respondents')
plt.tight_layout(True)
plt.savefig('histogram_plot.png')
# plt.grid(True)

plt.show()
