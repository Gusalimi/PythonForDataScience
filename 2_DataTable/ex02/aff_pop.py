from load_csv import load
import matplotlib.pyplot as plt


def convert_to_int(value):
    """Converts a string to an int, works with k and M numbers."""
    if 'k' in value:
        return int(float(value.replace('k', '')) * 1000)
    elif 'M' in value:
        return int(float(value.replace('M', '')) * 1000000)
    else:
        return int(float(value))


def main():
    data = load("population_total.csv")
    if (data is None):
        return
    france = data.loc[data['country'] == "France"].iloc[:, 1:-50]
    belgium = data.loc[data['country'] == "Belgium"].iloc[:, 1:-50]
    france = france.map(convert_to_int)
    belgium = belgium.map(convert_to_int)

    plt.plot(belgium.columns.values, belgium.values.flatten(), label="Belgium")
    plt.plot(france.columns.values, france.values.flatten(), label="France")

    plt.title("Population Projections")
    plt.legend()

    plt.ylabel("Population")
    plt.xlabel("Year")

    plt.xticks(france.columns[::40])
    custom_ticks = [20e6, 40e6, 60e6]
    yticks_millions = [f"{int(ytick / 1e6)}M" for ytick in custom_ticks]
    plt.yticks(custom_ticks, yticks_millions)

    plt.show()


if __name__ == "__main__":
    main()
