import csv
print("imported csv")
import plotext as plt
print("imported plotext")
import time

with open("transactions.csv", "r") as f:
            reader = csv.reader(f)
            data = list(reader)
            # remove the third row
            data.pop(2)
            # take the amount in the first row
            amounts = [int(i[0]) for i in data]
            # take the date in the second row (format: dd/mm/yyyy)
            plt.date_form('Y/m/d')
            dates = [i[1] for i in data]
            # remove the hour fros dates
            dates = [i.split(" ")[0] for i in dates]
            # remplace the - by / for the graph
            dates = [i.replace("-", "/") for i in dates]
            prices = amounts
            plt.plot(dates, prices)

            plt.title("Wallet Records")
            plt.xlabel("Date")
            plt.ylabel("Amount of transaction")
            plt.show()
            time.sleep(5)