from load_csv import load
import matplotlib.pyplot as plt


def main():
    life_expectancy = load("life_expectancy_years.csv")
    income = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    if (life_expectancy is None or income is None):
        return
    life_expectancy = life_expectancy['1900']
    income = income['1900']

    plt.scatter(income, life_expectancy)

    plt.title("1900")
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life expectancy")

    plt.xscale('log')
    plt.xticks([300, 1000, 10000], ["300", "1k", "10k"])

    plt.show()


if __name__ == "__main__":
    main()
