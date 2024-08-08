import matplotlib as plt
import streamlit as st
import pandas as pd

st.title("Simple Dashboard")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Data :")
    st.write(df)

    st.subheader("Data Summary :")
    st.write(df.describe())

    st.subheader('Filter Data :')
    columns = df.columns.tolist()
    selected_column = st.selectbox('Select Column', columns)
    unique_values = df[selected_column].unique()
    selected_value = st.selectbox('Select Value', unique_values)

    filtered_df = df[df[selected_column] == selected_value]
    st.write(filtered_df)

    st.subheader("Plot Data :")
    x_column = st.selectbox('Select X Axis', columns)
    y_column = st.selectbox('Select Y Axis', columns)

    if st.button('Generate Chart'):
        st.line_chart(filtered_df.set_index(x_column)[y_column])
else:
    st.write("Waiting for file upload...")