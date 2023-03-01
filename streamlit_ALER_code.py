

import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# Load the data
data = pd.read_excel('ALER_ASTE_BANDITE.xlsx')

# Create the linear regression model
model = LinearRegression()
model.fit(data[['manh_distance', 'bus_time', 'base', 'sqm_value']], data['price'])

# Define the Streamlit app
def app():
    st.title('House Price Prediction')
    st.markdown('Enter the details of the house below to predict its price.')

    # Create the input fields
    manh_distance = st.slider('walking distance to City centre', min_value=1, max_value=15, value=2)
    bus_time = st.number_input('Bus time to City centre', min_value=10, max_value=60, value=11)
    base = st.number_input('Auction base', min_value=50000, max_value=350000, value=68000)
    sqm_value = st.number_input('OMI value', min_value=800, max_value=5000, value=2500)

    # Predict the price
    price = model.predict([[manh_distance, bus_time, base, sqm_value]])

    # Display the result
    st.subheader('Predicted Price')
    st.write('${:,.2f}'.format(price[0]))

# Run the app
if __name__ == '__main__':
    app()
