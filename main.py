# Add a text input widget to the sidebar
import streamlit as st
# pip install pandas
import pandas as pd

df = pd.read_csv('car_data.csv')
st.title('Car Data')
st.write(df)

# with st.sidebar:
  # st.write("Here is sidebar")

# Add a text input widget to the sidebar
car_name = st.sidebar.text_input("Enter car name:")
# Display a greeting message using the input from the sidebar
#st.write(f"Input the Car Name: {user_input}!")

#multiselect
options = st.sidebar.multiselect('Choose:',['Manual','Automatic'], default = ['Manual', 'Automatic'])
# st.write('You selected:', option)

# price
values = st.sidebar.slider('Choose a range of selling price:',0,20, (0,20))
#st.write('Choose a range of selling price: ', values)

# year = st.slider('Choose a range of year:', 2000, 2001, 2)
year = st.sidebar.slider('Choose a range of years: ', 2000, 2024, (0,20))
#st.write('Choose a range of years: ', year)
button = st.sidebar.button('Submit')

# st.button filter ex:
filtered_df = df.copy()
if car_name:
    filtered_df = filtered_df[filtered_df['Car_Name'].str.contains(car_name,case = False)]
    print(filtered_df.head())
# if options:
#     filtered_df = filtered_df[filtered_df['Transmission'].isin(options)]
# if year:
#     filtered_df = filtered_df[(filtered_df['Year'] >= year[0]) & (filtered_df['Year'] <= year[1])]
# if values:
#     filtered_df = filtered_df[(filtered_df['Selling_Price'] >= values[0]) & (filtered_df['Selling_Price'] <= values[1])]
@st.cache
if button:
    st.write(filtered_df)