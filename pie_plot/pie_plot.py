from matplotlib import pyplot as plt
import pandas as pd
from collections import Counter

plt.style.use('fivethirtyeight')

# same bar plot data is used here
data = pd.read_csv("pie_plot_data.csv")

ids = data['Responder_id']
lang_responses = data['LanguagesWorkedWith']

lang_counter = Counter()

for response in lang_responses:
	lang_counter.update(response.split(';'))

languages = []
popularity = []

for item in lang_counter.most_common(5):
	languages.append(item[0])
	popularity.append(item[1])

explode = [0, 0, 0, 0.1, 0]
plt.pie(popularity, labels=languages, shadow=True, explode=explode, 
		startangle=90, autopct='%1.1f%%', wedgeprops={'edgecolor': 'black'})


plt.title('Language Popularity Pie')
plt.tight_layout()
plt.savefig('pie_plot.png')
plt.show()

