import streamlit as st
from sr.extraction import lead_data

st.set_page_config(layout="wide")

def main():

    df_row = lead_data()
    st.dataframe(df_row)


if __name__ == ' __main__ ':
    main()


