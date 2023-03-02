
import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# Load the data
data = pd.read_excel('ALER_ASTE_BANDITE.xlsx')

# Create the linear regression model
model = LinearRegression()
model.fit(data[['manh_distance', 'bus_time', 'base', 'sqm_value','size']], data['price'])

# Define the Streamlit app
def app():
    st.title('Modello di Machine Learning di previsione prezzo aste XQUARE ')
    st.markdown('Compilare i campi richiesti per ottenere la previsione di prezzo.')

    # Create the input fields
    manh_distance = st.slider('Distanza a piedi dal Centro in KM', min_value=1, max_value=15, value=2)
    bus_time = st.number_input('Distanza con i mezzi pubblici da Centro in minuti', min_value=10, max_value=60, value=11)
    base = st.number_input('Base asta', min_value=30000, max_value=350000, value=68000)
    sqm_value = st.number_input('Valore medio OMI della zona', min_value=800, max_value=5000, value=2500)
    size = st.number_input('Consistenza',min_value=30, max_value= 300 , value = 120)
    # Predict the price
    price = model.predict([[manh_distance, bus_time, base, sqm_value,size]])

    # Display the result
    st.subheader('Prezzo di aggiudicazione')
    st.write('€{:,.2f}'.format(price[0]))

# Run the app
if __name__ == '__main__':
    app()

