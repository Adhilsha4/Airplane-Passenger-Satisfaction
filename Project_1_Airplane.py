import streamlit as st
import pickle
from PIL import Image
import warnings

warnings.filterwarnings('ignore')
st.set_page_config(page_title="Air Passenger App", layout="wide")

# --- Page 1: Home ---
def home_page():
    st.markdown(
        """
        <h1 style='text-align: center; color: #FFFFFF; text-shadow: 2px 2px 4px #000000; font-weight: bold;'>
            AIRPLANE PASSENGER SATISFACTION
        </h1>
        """,
        unsafe_allow_html=True
    )

    img = Image.open('Airplane_4.jpg')
    st.image(img, width=1000)

    st.markdown(
        """
        <h2 style='color: #FFFFFF; text-shadow: 1px 1px 2px #000000;'>✈️ Introduction</h2>
        <p style='text-align: justify; font-size: 16px; color: #FFFFFF; text-shadow: 1px 1px 2px #000000;'>
            In today’s fast-paced world, there are several modes of transportation — <b>Roadways, Railways, Waterways</b>, and <b>Airways</b>. 
            Among these, <b>Air travel</b> is the <b>fastest and most premium</b> mode of transport. However, it involves strict procedures 
            like passport checks, visa requirements, ticketing, and boarding protocols.
        </p>
        <p style='text-align: justify; font-size: 16px; color: #FFFFFF; text-shadow: 1px 1px 2px #000000;'>
            Due to these complex procedures and strict airline rules, many passengers often feel <b>tired or frustrated</b>. As a result, 
            passengers prefer airline services that are <b>more efficient and comfortable</b>.
        </p>
        <p style='text-align: justify; font-size: 16px; color: #FFFFFF; text-shadow: 1px 1px 2px #000000;'>
            <b>Passengers consider the following factors when choosing an airline:</b>
        </p>
        <ul style='font-size: 16px; color: #FFFFFF; text-shadow: 1px 1px 2px #000000;'>
            <li>Ticketing and Boarding Services</li>
            <li>Baggage Handling</li>
            <li>Seat Comfort and Legroom</li>
            <li>In-flight Wi-Fi</li>
            <li>Onboard Services</li>
            <li>Airport Facilities</li>
        </ul>
        <p style='text-align: justify; font-size: 16px; color: #FFFFFF; text-shadow: 1px 1px 2px #000000;'>
            To understand passenger experiences better, airlines collect <b>feedback</b> to measure satisfaction and improve their services.
        </p>

        <hr style='border: 1px solid #ffffff;'>

        <h2 style='color: #FFFFFF; text-shadow: 1px 1px 2px #000000;'>🎯 Project Objective</h2>
        <p style='text-align: justify; font-size: 16px; color: #FFFFFF; text-shadow: 1px 1px 2px #000000;'>
            This project aims to predict whether a passenger is <b>Satisfied</b> or <b>Dissatisfied</b> with their flight experience 
            using a <b>Machine Learning model</b>.
        </p>
        <p style='font-size: 16px; color: #FFFFFF; text-shadow: 1px 1px 2px #000000;'><b>The model helps to:</b></p>
        <ul style='font-size: 16px; color: #FFFFFF; text-shadow: 1px 1px 2px #000000;'>
            <li>Identify what factors most influence satisfaction</li>
            <li>Predict satisfaction based on passenger responses</li>
            <li>Help airlines improve decision-making and customer experience</li>
        </ul>
        """,
        unsafe_allow_html=True
    )


# --- Page 2: Input Features ---
def input_features_page():
    st.title("Input Features")
    st.markdown(
        "<h1 style='text-align: center; color: #87CEEB;'><b>AIRPLANE PASSENGER SATISFACTION</b></h1>",
        unsafe_allow_html=True
    )
    img = Image.open('Passenger_Image.jpg')
    st.image(img, width=1200)

    feature_col1, feature_col2 = st.columns(2)

    with feature_col1:

# ----------------------------------------------------------------------------------------------------------------------------------------------------------
        # Label to value mapping
        gender_map = {"Select an option...": None, "Female": 0, "Male": 1}

        # Create the selectbox with labels
        selected_gender_label = st.selectbox("Gender of the Passenger", list(gender_map.keys()))

        # Get the mapped value for prediction
        ge = gender_map[selected_gender_label]

        # Show warning if no valid selection
        if ge is None:
            st.warning("Please select a valid gender.")
        else:
            st.success(f"Gender selected: {selected_gender_label} (Mapped to: {ge})")
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        ag = st.slider('Age of the Passenger', 10, 100)
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # Label to value mapping
        customer_map = {"Select an option...": None, "First-time": 0, "Returning": 1}

        # Create the selectbox with labels
        selected_customer_type_label = st.selectbox("Type of Airline Customer", list(customer_map.keys()))

        # Get the mapped value for prediction
        tc = customer_map[selected_customer_type_label]

        # Show warning if no valid selection
        if tc is None:
            st.warning("Please select a valid Type of Airline Customer.")
        else:
            st.success(f"Customer Experience selected: {selected_customer_type_label} (Mapped to: {tc})")
# ------------------------------------------------------------------------------------------------------------------------------------------------------------
        # Label to value mapping
        purpose_map = {"Select an option...": None, "Business": 0, "Personal": 1}

        # Create the selectbox with labels
        selected_Purpose_flight_label = st.selectbox("Purpose of the flight", list(purpose_map.keys()))

        # Get the mapped value for prediction
        pf = purpose_map[selected_Purpose_flight_label]

        # Show warning if no valid selection
        if pf is None:
            st.warning("Please select a valid Purpose.")
        else:
            st.success(f"Purpose selected: {selected_Purpose_flight_label} (Mapped to: {pf})")
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
        class_map = {"Select an option...": None, "Business": 0, "Economy": 1, "Economy Plus": 2}

        # Create the selectbox with labels
        selected_Travel_Class_label = st.selectbox("Travel class in the airplane for the passenger seat", list(class_map.keys()))

        # Get the mapped value for prediction
        pc = class_map[selected_Travel_Class_label]

        # Show warning if no valid selection
        if pc is None:
            st.warning("Please select a Travel Class.")
        else:
            st.success(f"Class selected: {selected_Travel_Class_label} (Mapped to: {pc})")
# ----------------------------------------------------------------------------------------------------------------------------------------------------
        fd = st.number_input("Enter Flight Distance", min_value=0)

        if fd == 0:
            st.warning("Flight distance must be greater than 0.")
        else:
            st.success(f"Flight Distance: {fd}")
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        dd = st.number_input('Flight departure delay in minutes')
        ad = st.number_input('Flight arrival delay in minutes')
        da = st.radio('Satisfaction level with the convenience of the flight departure and arrival times', [1, 2, 3, 4, 5])
        ob = st.radio('Satisfaction level with the online booking experience', [1, 2, 3, 4, 5])
        cs = st.radio('Satisfaction level with the check-in service ', [1, 2, 3, 4, 5])
        oe = st.radio('Satisfaction level with the online boarding experience', [1, 2, 3, 4, 5])


    with feature_col2:
        gl = st.radio('Satisfaction level with the gate location in the airport', [1, 2, 3, 4, 5])
        os = st.radio('Satisfaction level with the on-boarding service in the airport', [1, 2, 3, 4, 5])
        sc = st.radio('Satisfaction level with the comfort of the airplane seat', [1, 2, 3, 4, 5])
        lr = st.radio('Satisfaction level with the leg room of the airplane seat', [1, 2, 3, 4, 5])
        ca = st.radio('Satisfaction level with the cleanliness of the airplane', [1, 2, 3, 4, 5])
        fo = st.radio('Satisfaction level with the food and drinks on the airplane', [1, 2, 3, 4, 5])
        fs = st.radio('Satisfaction level with the in-flight service', [1, 2, 3, 4, 5])
        ws = st.radio('Satisfaction level with the in-flight Wifi service', [1, 2, 3, 4, 5])
        fe = st.radio('Satisfaction level with the in-flight entertainment', [1, 2, 3, 4, 5])
        bh = st.radio('Satisfaction level with the baggage handling from the airline', [1, 2, 3, 4, 5])

    features = [ge, ag, tc, pf, pc, fd, dd, ad, da, ob, cs, oe, gl, os, sc, lr, ca, fo, fs, ws, fe, bh]

    if st.button('Predict'):
        model = pickle.load(open('best_model.pkl', 'rb'))
        pred = model.predict([features])
        st.session_state.prediction_result = (
            'The Passenger is Satisfied' if pred == 1 else 'The Passenger is Dissatisfied'
        )
        st.success("✅ Prediction complete! Navigate to the Prediction tab.")

# --- Page 3: Prediction ---
def prediction_page():
    st.title("Prediction")
    result = st.session_state.get('prediction_result')
    if result:
        if 'Satisfied' in result:
            st.success(f"✅ {result}")
        else:
            st.error(f"❌ {result}")
    else:
        st.warning("⚠️ No prediction available. Please go to Input Features and click Predict.")

    st.markdown("---")
    first, second = st.columns([1, 2])

    with first:
        st.write("Data Source:")
        st.link_button("Kaggle", "https://www.kaggle.com/datasets/mysarahmadbhat/airline-passenger-satisfaction")
        st.write('Colab Link:')
        st.link_button("Colab", "https://colab.research.google.com/drive/1-IRGunjzX02lPyrVvUcBwGjQlgcx9_KW?usp=sharing")
    with second:
        st.write('EDA Presentation Link:')
        st.link_button("EDA", "https://1drv.ms/p/c/14d148a719232e87/EZ1dpjJkLs5KlGsAz2gy_tIBj95Vg8LVe8blvblCTI57Kw?e=nhgMS2")
        st.write('Project Presentation Link:')
        st.link_button("Presentation", "https://1drv.ms/p/c/14d148a719232e87/EdP1uRZGWFRMqqNqq6bWO6QBPeMpJ8awL8QWFEg32Ly0JQ?e=5IFE5kS")

# --- Navigation ---
pages = [
    st.Page(home_page, title="Home"),
    st.Page(input_features_page, title="Input Features"),
    st.Page(prediction_page, title="Prediction")
]

with st.sidebar:
    selected = st.navigation(pages, position="sidebar", expanded=True)

selected.run()
