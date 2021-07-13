import pandas as pd
import matplotlib.pyplot as plt


def test_run():
    df = pd.read_csv("./datasets/GRND3.SA.csv")

    print(df["Adj Close"])

    df["Adj Close"].plot()
    plt.show()


test_run()
