import pandas as pd
import csv
from datetime import date
import matplotlib.pyplot as plt

pd.options.mode.chained_assignment = None # getting rid of a warning message

FILE = "n.csv"  # Path to the file i use


class FCI:
    def __init__(self, balance, date):  # Initialize the class
        self.balance = balance
        self.date = date

    def add(self):  # Adds new balance with date, set changes to 0 that are later calculated
        lst = [self.balance, 0, self.date]
        with open(FILE, "a", newline='') as f:
            temp = csv.writer(f)
            temp.writerow(lst)

    @staticmethod
    def show_all():  # shows the entire file
        with open(FILE, "r") as f:
            temp = csv.reader(f)
            for i in temp:
                print(i)

    @staticmethod
    def show_current_balance():
        df = pd.read_csv(FILE)
        ind = len(df["balance"]) - 1
        print(df["balance"][ind])

    @staticmethod
    def calculate_changes():  # calculates and edits the changes in balance

        df = pd.read_csv(FILE)

        counter_change = 1
        counter1_balance = 0
        counter2_balance = 1

        try:
            for i in df["change"]:
                df["change"][counter_change] = df["balance"][counter2_balance] - df["balance"][counter1_balance]

                counter1_balance += 1
                counter2_balance += 1
                counter_change += 1

                df.to_csv(FILE, index=False)

        except KeyError:
            print("out of indexes")

    @staticmethod
    def show_graph():

        df = pd.read_csv(FILE)

        x = df["date"]
        y = df["balance"]
        plt.plot(x, y)
        plt.title("Gráfico de rendimientos")
        plt.xlabel("Fecha")
        plt.ylabel("Balance")
        plt.show()

    @staticmethod
    def test():
        pass