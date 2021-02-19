# Classy-IEX  Day 2
# OOP,Pandas, Numpy


Simple Python Class to generate a backtesting trading strategy using 2 SMA's, leveraging an existing python library to get data from IEX cloud platform, and in specific  one method
```bash
$ from iexfinance.stocks import get_historical_data
```
As usual I have to showcase what I have learned during the day:

- Object Oriented Programming - Creating a class that extracts data, in to a Data Frame, generates rolling average plot
- Numpy: A little bit of Numpy to do a simple vectorization
- DataFrames - To use pandas library, the defacto method for handling data
- ✨Matplotlib - Trying seaborn plots, which are very easy to create



##  How do I get data for using this class?
 If you want to generate the rolling average plot and the position plot, you need data, unfortunately IEX is a bit expensive, ($19 USD per month), certainly, the data and interface is amazing plus there are hundreds of libraries that can do the heavy lifting in particular if API's is not your thing, anyway, if you sign in for an account you get some credits and you can plot your data a couple of times

     *Just get your key and make sure you have it ready
     prior runnning the script*


## Instructions

1. Clone the repository

2. Please use Python3, upgrade if necessary

3. Install dependencies:

```bash
$ pip3 install -r requirements.txt
```

## Usage

1. Ensure you have your API ready , it looks something like this : pk_46ad823316a34d53a904fbbd63d67f28
	  Just so it is clear, the key above doesn't work, is just an example

2. Please note that you don't have to edit the `IEXclass.py`, actually, you don't have to modify any file, everything is automated

3. Please run the following command on your terminal, and just ensure you are on the correct folder.

```python
python main.py
```
4. A couple of points, obviously, I have automated and did some input validation, however, there are several things you should know - API_Key : Please have your API ready so you can simply copy paste your key, Ticker: This is the Stock Symbol, obviously please have in mind a particular stock before you run the script , if you are really using this plot as an indicator for backtesting trading strategy, then you know that more than 5 years of data is not  really useful, so try to stay within the 4 to 5 years timeframe

## Methods
The concept of backtesting trading is very common, and in fact due to the simplicity of the method is very use for technical stock analysis

1.  historical_data - Provides you with the dataframe containing the stock prices for the time that you initialize the series

```python
def historical_data(self):
```

2.  plot_rolling_average- Plots a 52 week and a 252 week rolling average , based on that relationship , there is a calculation that generates a signal, simply speaking the rule is to go long if the SMA (42 weeks) is above the longer SMA(252) weeks and a short position for the opposite result, this generates a 1 for a long position and -1 for a short position, and it's graphically display

```python
def plot_rolling_average(self):
```

3. Data is expensive, so if you want to play around with your data is certainly a good idea to keep a copy

```python
def save_to_HDF5(self):
```
The technical analysis, is probably the complex part, for that you might want to use a performance graph for a full SMA strategy,
additionaly, if you are analysing a company recently listed in the stock exchange the get_historical data script
will return the oldest data they have, so bear in mind that for the SMA 252 is not a great fit.

