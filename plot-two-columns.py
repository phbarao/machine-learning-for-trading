import pandas as pd
import matplotlib.pyplot as plt


def test_run():
    df = pd.read_csv("datasets/ITUB3.SA.csv")

    df[["Close", "Adj Close"]].plot()
    plt.show()


test_run()
