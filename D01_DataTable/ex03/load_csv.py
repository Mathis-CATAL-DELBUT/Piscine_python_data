import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    This function loads a csv file from the path and returns it as a DataFrame.
    """
    try:
        csv = pd.read_csv(path, index_col=0)
        print("Loading dataset of dimensions", csv.shape)
        return csv
    except FileNotFoundError:
        return None
    except PermissionError:
        return None
    except Exception:
        return None
