import pandas as pd
import matplotlib.pyplot as plt


def projection_life(expectancy: pd.DataFrame, gross: pd.DataFrame):
    """
    This function plots the life expectancy against the gross
    domestic product for the year 1900.
    """
    x = gross.loc[:, "1900"]
    y = expectancy.loc[:, "1900"]

    plt.scatter(x, y, color="blue", label="1900")
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life expectancy")
    plt.title("1900")

    plt.xscale("log")

    ticks = [300, 1000, 10000]
    labels = ["300", "1k", "10k"]
    plt.xticks(ticks, labels)

    plt.xlim(300, 10000)

    plt.show()
