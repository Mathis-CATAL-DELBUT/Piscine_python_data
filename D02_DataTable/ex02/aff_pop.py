import pandas as pd
import matplotlib.pyplot as plt


def aff_pop(df: pd.DataFrame):
    """
    This function plots the population projections for France and Belgium.
    """
    if "France" not in df.index or "Belgium" not in df.index:
        print("Donnees indisponibles pour la France et la Belgique")
        return

    france = df.loc["France", "1800":"2050"]
    belgium = df.loc["Belgium", "1800":"2050"]

    years = france.index.astype(int)

    plt.plot(years, belgium.values, label="Belgium", color="blue")
    plt.plot(years, france.values, label="France", color="green")

    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")

    plt.xlim(1800 - 10, 2050 + 10)
    plt.xticks(range(1800, 2051, 40))
    plt.yticks([20_000_000, 40_000_000, 60_000_000], ["20M", "40M", "60M"])
    plt.legend(loc="lower right")
    plt.show()
