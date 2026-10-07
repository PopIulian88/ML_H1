import matplotlib.pyplot as plt

from analysis import count_above, find_closest_to_mean, find_min_max, price_stats
from data_loader import load_apartments
from plots import plot_box_violin, plot_radar, plot_scatter


def main():
    df = load_apartments("apartments.json")

    cheapest, most_expensive = find_min_max(df)
    print("Apartamentul cel mai ieftin:")
    print(cheapest.to_string())
    print("\nApartamentul cel mai scump:")
    print(most_expensive.to_string())

    threshold = float(input("\nIntroduceti pragul de pret: "))
    print(f"Apartamente cu pret peste {threshold:.0f}: {count_above(df, threshold)}")

    mean, std = price_stats(df)
    print(f"\nPret mediu: {mean:.2f}")
    print(f"Abatere standard: {std:.2f}")

    average = find_closest_to_mean(df)

    plot_scatter(df)
    plot_box_violin(df)
    plot_radar(df, {"Minim": cheapest, "Mediu": average, "Maxim": most_expensive})
    plt.show()


if __name__ == "__main__":
    main()
