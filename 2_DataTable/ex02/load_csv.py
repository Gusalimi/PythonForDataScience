import pandas as pd


def load(path: str) -> pd.DataFrame:
    if (not isinstance(path, str)):
        print("Path is not a string")
        return None
    if (path == ''):
        print("Path is empty")
        return None
    if (not path.endswith('.csv')):
        print("Path does not end with .csv")
        return None
    try:
        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions {df.shape}")
        return df
    except Exception:
        print("Error while reading csv file")
        return None
