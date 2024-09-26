from load_csv import load
from aff_pop import aff_pop


def main():
    aff_pop(load("population_total.csv"))


if __name__ == "__main__":
    main()
