from datetime import datetime

def menu():
    while True:
        stocksymbol = input("Enter the stock symbol: ")
        if len(stocksymbol) not in range(1,8) or not stocksymbol.isupper() or not stocksymbol.isalpha():
            print("Input must 1-7 capitalized alphabetic characters.")
            continue
        else:
            break
    print()
    choice = 0
    while True:
        print("Chart Type")
        print("1. Line")
        print("2. Bar")
        try:     
            choice = int(input("Select a time series function: (1-2) "))
            if choice < 1 or choice > 2:
                raise ValueError
        except ValueError:
            print("Input must be an int between 1-2.")
        else:
            break
    if choice == 1:
        charttype = "Line"
    if choice == 2:
        charttype = "Bar"
    print()
    choice = 0
    while True: 
        print("Time Series Function")
        print("1. Intraday")
        print("2. Daily")
        print("3. Weekly")
        print("4. Monthly")

        
        try:     
            choice = int(input("Select a time series function: (1-4) "))
            if choice < 1 or choice > 4:
                raise ValueError
        except ValueError:
            print("Input must be an int between 1-4.")
        else:
            break
    function = ""
    if choice == 1:
        function = "TIME_SERIES_INTRADAY"
    elif choice == 2:
        function = "TIME_SERIES_DAILY_ADJUSTED"
    elif choice == 3:
        function = "TIME_SERIES_WEEKLY"
    elif choice == 4:
        function = "TIME_SERIES_MONTHLY"
    print()
    while True:
        try:
            startdate = datetime.strptime(input("Enter the beginning date in YYYY-MM-DD format: "), '%Y-%m-%d' )
            enddate = datetime.strptime(input("Enter the end date in YYYY-MM-DD format: "), '%Y-%m-%d')
            if startdate > enddate:
                raise ValueError("Start date is after end date.")
        except ValueError as e:
            print(e)
        else:
            break
    print (f"Stock symbol: {stocksymbol}, Chart Type: {charttype}, Time Series: {function}, Start Date:{startdate}, End Date: {enddate}")
    
menu()
