import numpy as np
import pandas as pd


def quickstart():
    # Series
    # s = pd.Series([1, 3, 5, np.nan, 6, 8])
    # print(s)

    # DataFrame
    # dates = pd.date_range("20130101", periods=6)
    # print(dates)

    # DataFrame
    df2 = pd.DataFrame(
        {
            "A": 1.0,
            "B": pd.Timestamp("20130102"),
            "C": pd.Series(1, index=list(range(4)), dtype="float32"),
            "D": np.array([3] * 4, dtype="int32"),
            "E": pd.Categorical(["test", "train", "test", "train"]),
            "F": "foo",
        }
    )
    print(df2)
    # print(df2.dtypes)
    # print(df2.head(1))
    # print(df2.tail(1))
    # print(df2.index)
    print(df2.to_json())


quickstart()
