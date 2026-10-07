import matplotlib.pyplot as plt
import numpy as np

RADAR_ATTRIBUTES = [
    "surface_m2",
    "rooms",
    "bathrooms",
    "floor",
    "distance_to_transport_m",
    "price",
]


def plot_scatter(df):
    plt.figure()
    plt.scatter(df["surface_m2"], df["price"])
    plt.xlabel("Suprafata (m2)")
    plt.ylabel("Pret")
    plt.title("Suprafata vs pret")
    plt.grid(True)


def plot_box_violin(df):
    fig, (ax_box, ax_violin) = plt.subplots(1, 2, figsize=(10, 5))
    ax_box.boxplot(df["price"])
    ax_box.set_title("Boxplot preturi")
    ax_box.set_ylabel("Pret")
    ax_violin.violinplot(df["price"], showmeans=True, showmedians=True)
    ax_violin.set_title("Violin plot preturi")
    ax_violin.set_ylabel("Pret")


def plot_radar(df, apartments):
    labels = RADAR_ATTRIBUTES
    mins = df[labels].min()
    maxs = df[labels].max()

    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
    angles += angles[:1]

    fig, ax = plt.subplots(subplot_kw={"polar": True}, figsize=(7, 7))
    for name, apt in apartments.items():
        values = ((apt[labels] - mins) / (maxs - mins)).astype(float).tolist()
        values += values[:1]
        ax.plot(angles, values, label=f"{name} ({apt['price']:.0f})")
        ax.fill(angles, values, alpha=0.15)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)
    ax.set_ylim(0, 1)
    ax.set_title("Radar: apartament minim, mediu, maxim (valori normalizate 0-1)")
    ax.legend(loc="upper right", bbox_to_anchor=(1.3, 1.1))
