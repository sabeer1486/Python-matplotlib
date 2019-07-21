from matplotlib import pyplot as plt
from collections import Counter
import pandas as pd

plt.style.use("fivethirtyeight")

data = pd.read_csv('bar_plot_2_data.csv')
lang_responses = data['LanguagesWorkedWith']

language_counter = Counter()

for response in lang_responses:
	language_counter.update(response.split(';'))

languages = []
popularity = []

for item in language_counter.most_common(15):
	languages.append(item[0])
	popularity.append(item[1])

languages.reverse()
popularity.reverse()

plt.barh(languages, popularity)


plt.title('Most Popular Languages')
# plt.ylabel('Porgramming Languages')
plt.xlabel('No.of people Use')

plt.tight_layout()

plt.savefig('bar_plot_2.png')

plt.show()
