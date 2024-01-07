from load_csv import load
import matplotlib.pyplot as plt


def main():
    data = load("life_expectancy_years.csv")
    if (data is None):
        return
    france = data.loc[data['country'] == "France"].iloc[:, 1:]

    plt.plot(france.columns.values, france.values[0])

    plt.title("France Life expectancy Projections")

    plt.ylabel("Life expectancy")
    plt.xlabel("Year")
    plt.xticks(france.columns[::40])

    plt.show()


if __name__ == "__main__":
    main()
