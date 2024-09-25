import matplotlib.pyplot as plt
import pandas as pd


def aff_life(df: pd.DataFrame):
    """
    This function plots the life expectancy projections for France.
    """
    x = df.loc["France"]

    france = x.index.astype(int)

    plt.plot(france, x.values, label="France")

    plt.xlim(1800 - 10, 2100 + 10)
    plt.xticks(range(1800, 2100, 40))

    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.title("France Life expectancy Projections")

    plt.show()
