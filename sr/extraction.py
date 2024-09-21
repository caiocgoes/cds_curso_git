import pandas as pd
import numpy as np
import streamlit as st

def lead_data():
    return pd.read_csv("data/bikes_completed.csv")
