import datetime
from datetime import date
import IEXClass as IEX


def key():
    api_key = input('Paste your API from IEX, there is no user input validation, please copy your API from IEX to the terminal: ')
    return api_key.strip()

def ticker():


    while True:
        ticker = input('Enter a ticker (Stock Symbol - Example TSLA is Tesla)  between 1 to 5 letters: ')
        if len(ticker) > 0 and len(ticker) <= 6:
            break
        if ticker.isalpha() == False:
            print('Please use letters ')
        else:
            print('ticker is usually 1 to 4 letter name i.e TSLA ')

    return ticker.upper()

def user_input_date():
    """
    :return: The Date that will be input in the class
    """
    print("Please enter a DATE for your analysis, a time series will be created starting with that date")
    print()
    print("My recommendation is that you don't use more than 5 years of data, and that you use more than 1 year of data")

    ##Ask for user input, please note that you should only use 10 years, but feel free to modify
    current_year = date.today().year

    while True:
        try:
            year = int(input('Enter a year (4 digits, i.e 2015): '))
            if year >= current_year - 10 and year <= current_year - 2:
                break
            else:
                print(f"Honestly, you should not be using SMA for more than 10 years,also maximum year is the current {current_year} ")
        except ValueError:
            print("Please ensure that you type a number")

    while True:
        try:
            month = int(input('Enter a month - Remember that the year has 12 months: '))
            if month <= 12 and month > 0:
                break
            else:
                print(f"Please use a number between 1 and 12")
        except ValueError:
            print("Please ensure that you type a number")

    while True:
        try:
            day = int(input('Enter a day: '))
            if day<32 and day>0:
                break
            else:
                print(f"Really, a month has a minimum of 28 days and maximum 31 days")
        except ValueError:
            print("Please ensure that you type a number")

    date_value = datetime.date(year,month,day)

    return date_value

if __name__ == "__main__":
    api_key = key()
    ticker = ticker()
    date_value = user_input_date()
    a = IEX.IEXfin(api_key,date_value,ticker)
    a.plot_rolling_average()
    a.save_to_HDF5()






