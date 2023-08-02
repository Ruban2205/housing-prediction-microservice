from utils.user_interface import load_css_file
import requests
import time
import streamlit as st


def main():
    """
    UI Part of the entire application.
    """
    st.set_page_config(
        page_title="House Realtor App",
        page_icon="🧊",
        menu_items={
            "About": "# House Price Prediction",
        },
    )
    load_css_file(".streamlit/main.css")

    st.markdown(
        "<h1 style='text-align: center;'>House <span style='color: #9eeade;'>Realtor-X</span></h1>",
        unsafe_allow_html=True,
    )
    st.subheader("Artificial Intelligent System")

    area = st.number_input(
        "Area of house", min_value=40, max_value=2000, value=600, step=1
    )
    bedrooms = st.number_input(
        "No of bedrooms", min_value=1, max_value=5, value=2, step=1
    )
    bathrooms = st.number_input(
        "No of bathrooms", min_value=1, max_value=5, value=1, step=1
    )
    stories = st.number_input(
        "No of stories", min_value=1, max_value=5, value=3, step=1
    )
    mainroad = st.text_input("Presence of mainroad", value="no")
    guestroom = st.text_input("Presence of guestroom", value="no")
    basement = st.text_input("Presence of basement", value="no")
    hotwaterheating = st.text_input("Presence of water heater", value="no")
    airconditioning = st.text_input("Presence of airconditioner", value="no")
    parking = st.number_input(
        "No of parking slots", min_value=1, max_value=6, value=3, step=1
    )
    prefarea = st.text_input("Presence of pref area", value="no")
    semi_furnished = st.text_input("Semi Furnished ", value="no")
    unfurnished = st.text_input("Unfurnished", value="no")

    if st.button("Predict house price 💰"):
        with st.spinner("Predicting price..."):
            time.sleep(1)
            url = f"https://house-prediction-api.azurewebsites.net/inference/?area={str(area)}&bedrooms={str(bedrooms)}&bathrooms={str(bathrooms)}&stories={str(stories)}&mainroad={str(mainroad)}&guestroom={str(guestroom)}&basement={str(basement)}&hotwaterheating={str(hotwaterheating)}&airconditioning={str(airconditioning)}&parking={str(parking)}&prefarea={str(prefarea)}&semi_furnished={str(semi_furnished)}&unfurnished={str(unfurnished)}"
            response = requests.get(url)
            response_json = response.json()

            st.header(f'The house would cost ${response_json["result"] : ,.2f}')

    with st.expander("House Price Prediction"):
        st.markdown(
            '<p style="font-size: 30px;"><strong>Welcome to the House  \
            <span style="color: #9eeade;">Realtor-X</span> App!</strong></p>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p style = "font-size : 20px; color : white;">This application was \
            built  to predict the <strong>price</strong> of a house \
                based on its records and attributes. </p>',
            unsafe_allow_html=True,
        )
        st.markdown(
            "[Learn more](https://github.com/mahimairaja/housing-prediction-azure-microservice)"
        )


if __name__ == "__main__":
    main()
