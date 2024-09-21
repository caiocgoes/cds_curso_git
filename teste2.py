import pandas as pd
import numpy as np
import streamlit as st

def lead_data():
    return pd.read_csv("data/processed/bikes_completed.csv")

def main():

    df = lead_data()
    st.dataframe(df)


if __name__ == ' __main__ ':
    main()


