import pandas as pd
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

plt.style.use('seaborn')
pd.set_option('display.max_columns', None)

data = pd.read_csv('data_time.csv')
price_date = data['Date']
print(data.head(1))

data['Date'] = pd.to_datetime(data['Date'])
data.sort_values(data, inplace=True)


price_close = data['Close']

plt.plot_date(price_date,price_close, linestyle='solid')
plt.gcf().autofmt_xdate()

#date_format = mpl_dates.DateFormatter('%b %d, %Y')

#plt.gca().xaxis.set_major_formatter(date_format)




plt.title('Bitcoin Prices')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.tight_layout()

plt.show()

