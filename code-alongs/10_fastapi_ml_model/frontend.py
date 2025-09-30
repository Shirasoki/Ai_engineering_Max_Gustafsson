import streamlit as st
from helpers import read_api_endpoint, post_api_endpoint
import pandas as pd

iris_data = read_api_endpoint("/api")
df = pd.DataFrame(iris_data.json())



def layout():
    st.markdown("# Classify Iris Flower")
    
    with st.form("iris_data"):
        sepal_length = st.number_input("Sepal Length (cm)", min_value=4.0, max_value=8.5, value=6.0, step=0.1)
        sepal_width = st.number_input("Sepal Width (cm)", min_value=2.0, max_value=4.5, value=3.0, step =0.1)
        petal_length = st.number_input("Petal Length (cm)", min_value=1.0, max_value=7.0, value=4.0, step=0.1)
        petal_width = st.number_input("Petal Width (cm)", min_value=0.1, max_value=2.5, value=1.0, step=0.1)

        submitted = st.form_submit_button("Predict Flower")
    
    if submitted:
        payload = {
            "SepalLengthCm": sepal_length,
            "SepalWidthCm": sepal_width,
            "PetalLengthCm" : petal_length,
            "PetalWidthCm" : petal_width
        }

        response = post_api_endpoint(payload, endpoint="/api/predict")
        predicted_flower = response.json().get("predicted_flower")
        st.markdown(predicted_flower)

    print(f"{sepal_length = }")
    print(f"submitted = {submitted}")
                

    st.markdown("## Raw data")
    #st.markdown(df)


if __name__ == "__main__":
    layout()


# TODO, try to predict a flower based on user input and display the result in streamlit
