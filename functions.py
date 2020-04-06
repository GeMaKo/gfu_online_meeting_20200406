import pandas as pd


def create_ratio_features(df):
    df_ret = pd.DataFrame()
    df_ret["rooms_per_household"] = df["total_rooms"] / df["households"]
    df_ret["bedrooms_per_room"] = df["total_bedrooms"] / df["total_rooms"]
    df_ret["population_per_household"] = df["population"] / df["households"]
    return df_ret
