def find_min_max(df):
    cheapest = df.loc[df["price"].idxmin()]
    most_expensive = df.loc[df["price"].idxmax()]
    return cheapest, most_expensive


def count_above(df, threshold):
    return int((df["price"] > threshold).sum())


def price_stats(df):
    return df["price"].mean(), df["price"].std()


def find_closest_to_mean(df):
    mean_price = df["price"].mean()
    return df.loc[(df["price"] - mean_price).abs().idxmin()]
