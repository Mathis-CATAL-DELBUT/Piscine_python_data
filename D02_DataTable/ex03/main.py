from load_csv import load
from projection_life import projection_life


def main():
    projection_life(
        load("life_expectancy_years.csv"),
        load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv"),
    )


if __name__ == "__main__":
    main()
