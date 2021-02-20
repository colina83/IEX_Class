import pandas as pd
from iexfinance.stocks import get_historical_data
import time
from pylab import mpl,plt
import numpy as np



class IEXfin:
    """
    historical data - Extracts all data from IEX, using the stock ticker provided by the user for a time period

    plot_rolling_average - This will plot the price (EOD), and the rolling average for 42 and 252 days

    dave_to_HDF5 - Getting data from IEX is expensive, so if you need to work on the data later, this function saves
    object data frame in the folder data, so you can do further testing with that lightweight file.
    """
    def __init__(self,api_key,date_value,ticker):
        self.api_key = api_key
        self.date_value = date_value
        self.ticker = ticker


    # Returns a Data Frame
    def historical_data(self):
        self.data_series = get_historical_data(self.ticker,output_format = "pandas",
                                               token = self.api_key, start = self.date_value)
        return self.data_series

    def plot_rolling_average(self):
            #We are going to plot the close price, obviously, pros and cos to using this price
        data = self.historical_data()
        data_plot = pd.DataFrame(data['close'])
        data_plot['close'] = pd.to_numeric(data_plot['close'])
        data_plot.rename(columns={'close':'price'}, inplace = True)
        #Calculates rolling Average
        data_plot["SMA1"] = data_plot['price'].rolling(42).mean()
        data_plot["SMA2"] = data_plot['price'].rolling(252).mean()
        #Plots Rolling Average
        plt.style.use('seaborn')
        mpl.rcParams['savefig.dpi'] = 300
        mpl.rcParams['font.family'] = 'serif'
        data_plot.plot(title = f"{self.ticker} - 42 & 252 days SMA's", figsize = (10,6))
        plt.show()
        #Market position
        data_plot['position'] = np.where(data_plot['SMA1'] > data_plot['SMA2'], 1, -1)
        data_plot.dropna(inplace=True)
        data_plot['position'].plot(ylim=[-1.1,1.1], title = f'{self.ticker} position -Long and Short', figsize = (10,6))
        plt.show()
        ## Calculates the performance of the strategy, with a histogram, performance of the strategy relative to
        ## the base investment
        data_plot['returns'] = np.log(data_plot['price']/data_plot['price'].shift(1))
        data_plot['returns'].hist(bins = 35,figsize=(10,6))
        plt.show()
        ## Calculate the returns for the strategy
        data_plot['strategy'] = data_plot["position"].shift(1) * data_plot['returns']
        data_plot[['returns','strategy']].sum()
        data_plot[['returns', 'strategy']].sum()
        data_plot[['returns','strategy']].sum().apply(np.exp)
        data_plot[['returns','strategy']].cumsum().apply(np.exp).plot(figsize = (10,6))
        plt.show()

    def save_to_HDF5(self):
        h5 = pd.HDFStore('data/{}_{}.h5'.format(self.ticker,int(time.time())),'w')
        h5['df'] = self.historical_data()
        h5.close()
        print(f"Your File is saved, please go to the data folder")

