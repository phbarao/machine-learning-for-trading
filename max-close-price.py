import pandas as pd


def get_max_close(symbol):
    df = pd.read_csv(f"./datasets/{symbol}.csv")

    return df["Close"].max()


def test_run():
    for symbol in ["ABEV3.SA", "GRND3.SA", "ITUB3.SA", "RADL3.SA", "WEGE3.SA"]:
        print("Max close")
        print(symbol, get_max_close(symbol))


test_run()
