import pandas as pd


def convert_k_m(value):
    if isinstance(value, str):
        if "k" in value:
            return float(value.replace("k", "")) * 1000
        elif "M" in value:
            return float(value.replace("M", "")) * 1000000
    return value


def load(path: str) -> pd.DataFrame:
    try:
        csv = pd.read_csv(path, index_col=0)
        print("Loading dataset of dimensions", csv.shape)
        csv = csv.applymap(convert_k_m)
        return csv
    except FileNotFoundError:
        return None
    except PermissionError:
        return None
    except Exception:
        return None
