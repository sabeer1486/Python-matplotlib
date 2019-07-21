from matplotlib import pyplot as plt
from datetime import datetime
import pandas as pd
from matplotlib import dates as mpl_dates

plt.style.use('seaborn')

data = pd.read_csv('time_plot_data.csv')


# need to covert Date coloumn into the date_format
data['Date'] = pd.to_datetime(data['Date'])
data.sort_values('Date', inplace=True)

price_date = data['Date']
price_close = data['Close']

plt.plot_date(price_date, price_close, linestyle='solid')

plt.gcf().autofmt_xdate()
date_format = mpl_dates.DateFormatter('%b, %d %y')
plt.gca().xaxis.set_major_formatter(date_format)

plt.title('Bitcoin Prices')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.tight_layout(True)
plt.savefig('time_plot.png')

plt.show()
