from load_csv import load
from aff_life import aff_life


def main():
    aff_life(load("life_expectancy_years.csv"))


if __name__ == "__main__":
    main()
