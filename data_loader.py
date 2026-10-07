import pandas as pd


def load_apartments(path="apartments.json"):
    return pd.read_json(path)
